document.addEventListener('DOMContentLoaded', function() {
    function showNext(sectionId) {
        var sections = document.querySelectorAll('form > div');
        sections.forEach(function(section) {
            section.classList.add('hidden');  // Hide all sections
        });

        var nextSection = document.getElementById(sectionId);
        nextSection.classList.remove('hidden');  // Show the current section
    }

    function toggleHomeStationVisibility() {
        var checkbox = document.getElementById("deployerTDYToggle");
        var homeStationField = document.getElementById("homeStationField");

        if (checkbox.checked) {
            homeStationField.classList.add('visible'); // Shows the input field
            homeStationField.classList.remove('hidden');
        } else {
            homeStationField.classList.remove('visible'); // Hides the input field
            homeStationField.classList.add('hidden');
        }
    }

    function toggleDeviceDropOffVisibility() {
        var checkbox = document.getElementById("deviceDropOffToggle");
        var deviceDropOffFields = document.getElementById("deviceDropOffFields");

        if (checkbox.checked) {
            deviceDropOffFields.classList.add('visible'); // Shows the input fields
            deviceDropOffFields.classList.remove('hidden');
        } else {
            deviceDropOffFields.classList.remove('visible'); // Hides the input fields
            deviceDropOffFields.classList.add('hidden');
        }
    }

    function showFields(reason) {
        var iPhoneFields = document.getElementById('iPhoneFields');
        var accountAccessFields = document.getElementById('accountAccessFields');
        var computerReimageFields = document.getElementById('computerReimageFields');
        var addDeviceFields = document.getElementById('addDeviceFields');
        var generalQuestionsFields = document.getElementById('generalQuestionsFields');

        if (reason === 'iPhone') {
            iPhoneFields.classList.remove('hidden');
            accountAccessFields.classList.add('hidden');
            computerReimageFields.classList.add('hidden');
            addDeviceFields.classList.add('hidden');
            generalQuestionsFields.classList.add('hidden');
        } else if (reason === 'Account Access') {
            accountAccessFields.classList.remove('hidden');
            iPhoneFields.classList.add('hidden');
            computerReimageFields.classList.add('hidden');
            addDeviceFields.classList.add('hidden');
            generalQuestionsFields.classList.add('hidden');
        } else if (reason === 'Computer Reimage') {
            computerReimageFields.classList.remove('hidden');
            iPhoneFields.classList.add('hidden');
            accountAccessFields.classList.add('hidden');
            addDeviceFields.classList.add('hidden');
            generalQuestionsFields.classList.add('hidden');
        } else if (reason === 'Add device to domain/network') {
            addDeviceFields.classList.remove('hidden');
            iPhoneFields.classList.add('hidden');
            accountAccessFields.classList.add('hidden');
            computerReimageFields.classList.add('hidden');
            generalQuestionsFields.classList.add('hidden');
        } else if (reason === 'General Questions') {
            generalQuestionsFields.classList.remove('hidden');
            addDeviceFields.classList.add('hidden');
            iPhoneFields.classList.add('hidden');
            accountAccessFields.classList.add('hidden');
            computerReimageFields.classList.add('hidden');
        } else {
            iPhoneFields.classList.add('hidden');
            accountAccessFields.classList.add('hidden');
            computerReimageFields.classList.add('hidden');
            addDeviceFields.classList.add('hidden');
            generalQuestionsFields.classList.add('hidden');
        }
    }

    document.getElementById('reasonForVisit').addEventListener('change', function() {
        showFields(this.value);
    });

    document.getElementById('deployerTDYToggle').addEventListener('change', toggleHomeStationVisibility);
    document.getElementById('deviceDropOffToggle').addEventListener('change', toggleDeviceDropOffVisibility);

    function generateCubes(numCubes) {
        const heroSection = document.querySelector('.hero');
        for (let i = 0; i < numCubes; i++) {
            let cube = document.createElement('div');
            cube.className = 'cube';
            cube.style.top = `${Math.random() * 100}%`; // Random position from top of the hero section
            cube.style.left = `${Math.random() * 100}%`; // Random position from left of the hero section
            heroSection.appendChild(cube);
        }
    }

    generateCubes(8);

    function goHome() {
        window.location.href = "/";
    }

    document.getElementById('resetButton').addEventListener('click', goHome);

    document.querySelectorAll('button[data-next]').forEach(function(button) {
        button.addEventListener('click', function() {
            showNext(button.getAttribute('data-next'));
        });
    });

    // Update checkbox values to 'yes' or 'no'
    document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            checkbox.value = checkbox.checked ? 'yes' : 'no';
        });
        checkbox.value = 'no';  // Initialize unchecked checkboxes to 'no'
    });
});
