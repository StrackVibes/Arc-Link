import os
import random
import pandas as pd
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import logging
from dotenv import load_dotenv
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

# Load environment variables from a .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('SubmissionLogger')
handler = TimedRotatingFileHandler('logs/submissions.log', when="midnight", interval=1)
handler.suffix = "%Y-%m-%d"
logger.addHandler(handler)

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def load_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                logging.error(f"Failed to refresh token: {e}")
                creds = None
        if not creds:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                logging.error(f"Failed to authorize credentials: {e}")
                return None
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email(subject, message_text, to):
    creds = load_credentials()
    if not creds:
        return "Failed to load credentials."
    
    if not to:
        logging.error("Recipient address is empty.")
        return "Recipient address required."

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = 'me'
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_body = {'raw': raw_message}
        
        sent_message = service.users().messages().send(userId='me', body=message_body).execute()
        logging.info(f'Message Id: {sent_message["id"]}')
        return "Email sent successfully!"
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        return "Failed to send email."

def get_random_quote():
    try:
        df = pd.read_csv('quotes.csv', delimiter=';')
        random_quote = df.sample().iloc[0]
        quote_text = random_quote['QUOTE']
        quote_author = random_quote['AUTHOR']
        return f"{quote_text} - {quote_author}"
    except Exception as e:
        logging.error(f"Failed to load quotes: {e}")
        return "No quote available."

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.respond_with_file('index.html', 'text/html')
        elif self.path == '/script.js':
            self.respond_with_file('script.js', 'application/javascript')
        elif self.path == '/styles.css':
            self.respond_with_file('styles.css', 'text/css')
        elif self.path == '/favicon.ico':
            self.respond_with_file('favicon.ico', 'image/x-icon')
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))
            message_body = "You have a new kiosk submission:\n\n"

            log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},"

            for key, value in data.items():
                message_body += f"{key.capitalize().replace('_', ' ')}: {value[0]}\n"
                log_entry += f"{key.capitalize()}: {value[0]},"
            
            log_entry = log_entry.rstrip(',')
            logger.info(log_entry)

            recipient_email = "inshane09@gmail.com"
            logging.info(f"Recipient email: {recipient_email}")
            
            email_status = send_email("New Kiosk Submission", message_body, recipient_email)
            
            random_quote = get_random_quote()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response_html = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="refresh" content="5;url=/" />
                <title>Submission Received</title>
                <style>
                    body {{ font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }}
                    h1 {{ color: #4CAF50; }}
                    p.quote {{ font-style: italic; color: #555; margin-top: 50px; }}
                </style>
            </head>
            <body>
                <h1>Thank you for submitting your information!</h1>
                <p>Please have a seat. Someone will be with you shortly.</p>
                <div style="position: absolute; bottom: 10px; width: 100%; left: 0;">
                    <p class="quote">{random_quote}</p>
                </div>
            </body>
            </html>
            '''
            self.wfile.write(response_html.encode('utf-8'))
            logging.info(email_status)
        else:
            self.send_error(501, "Not Supported")

    def respond_with_file(self, file_path, content_type):
        try:
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting httpd server on {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
