
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/StrackVibes/Arc-Link">
    <img src="favicon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Kiosk Submission Project</h3>

  <p align="center">
    A project to manage kiosk submissions and email notifications!
    <br />
    <a href="https://github.com/StrackVibes/Arc-Link"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/StrackVibes/Arc-Link/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://i.ibb.co/4M3gJ4R/Screenshot-2024-05-30-004254.png)

This project is designed to handle kiosk submissions and send email notifications using Google Gmail API. It also displays random motivational quotes upon successful submission.

Here's why:
* Efficiently manage kiosk submissions
* Automate email notifications
* Display random quotes for motivation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Google Gmail API](https://developers.google.com/gmail/api)
* [dotenv](https://pypi.org/project/python-dotenv/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/StrackVibes/Arc-Link.git
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file
   ```dotenv
   GMAIL_USER=your-email@gmail.com
   GMAIL_PASS=your-email-password
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

To run the server, use the following command:
```sh
python3 server.py
```

Navigate to `http://localhost:8000` in your web browser to access the kiosk submission form.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Add more motivational quotes
- [ ] Enhance the UI with more styles
- [ ] Implement user authentication

See the [open issues](https://github.com/StrackVibes/Arc-Link/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/StrackVibes/Arc-Link](https://github.com/StrackVibes/Arc-Link)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/StrackVibes/Arc-Link.svg?style=for-the-badge
[contributors-url]: https://github.com/StrackVibes/Arc-Link/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StrackVibes/Arc-Link.svg?style=for-the-badge
[forks-url]: https://github.com/StrackVibes/Arc-Link/network/members
[stars-shield]: https://img.shields.io/github/stars/StrackVibes/Arc-Link.svg?style=for-the-badge
[stars-url]: https://github.com/StrackVibes/Arc-Link/stargazers
[issues-shield]: https://img.shields.io/github/issues/StrackVibes/Arc-Link.svg?style=for-the-badge
[issues-url]: https://github.com/StrackVibes/Arc-Link/issues
[license-shield]: https://img.shields.io/github/license/StrackVibes/Arc-Link.svg?style=for-the-badge
[license-url]: https://github.com/StrackVibes/Arc-Link/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/your_username
[product-screenshot]: https://i.ibb.co/4M3gJ4R/Screenshot-2024-05-30-004254.png
