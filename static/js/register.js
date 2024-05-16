document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');
    const submitBtn = document.getElementById('submitBtn');

    // Add event listeners to input fields to clear error messages when user starts filling them
    const inputFields = form.querySelectorAll('input, select');
    inputFields.forEach(inputField => {
        inputField.addEventListener('input', function () {
            const errorId = this.id + '_error';
            const errorMessage = document.getElementById(errorId);
            errorMessage.textContent = ''; // Clear the error message
        });
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        // Check if form fields are empty
        const firstName = document.getElementById('first_name').value;
        const lastName = document.getElementById('last_name').value;
        const dateOfBirth = document.getElementById('date_of_birth').value;
        const gender = document.getElementById('gender').value;
        const phoneNumber = document.getElementById('phone_number').value;
        const email = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Display error messages if fields are empty
        if (!firstName) {
            displayErrorMessage('first_name_error', 'Please enter your first name.');
            return;
        }
        if (!lastName) {
            displayErrorMessage('last_name_error', 'Please enter your last name.');
            return;
        }
        if (!dateOfBirth) {
            displayErrorMessage('date_of_birth_error', 'Please select your date of birth.');
            return;
        }
        if (!gender) {
            displayErrorMessage('gender_error', 'Please select your gender.');
            return;
        }
        if (!phoneNumber) {
            displayErrorMessage('phone_number_error', 'Please enter your phone number.');
            return;
        }
        if (!email) {
            displayErrorMessage('username_error', 'Please enter your email address.');
            return;
        }
        if (!password) {
            displayErrorMessage('password_error', 'Please enter your password.');
            return;
        }

        // If all fields are filled, submit the form
        this.submit();
    });

    function displayErrorMessage(fieldId, message) {
        const errorMessage = document.getElementById(fieldId);
        errorMessage.textContent = message;
        errorMessage.style.color = 'red';
    }
});
