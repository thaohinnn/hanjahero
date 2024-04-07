// Function to handle link generation
function generateLink(selectedSkill, selectedExam, timeLimit) {
    // Remove any existing error message
    const errorMessage = document.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.parentNode.removeChild(errorMessage);
    }

    // Get the selected format from the checkboxes, skipping any undesired values
    const selectedFormat = Array.from(document.querySelectorAll('input[type=checkbox]:checked'))
        .map(checkbox => checkbox.value)
        .filter(value => !isNaN(value)); // Filter out any non-numeric values

    if (selectedFormat.length === 0) {
        // Display error message for no selected task
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Please choose at least one task';
        errorMessage.style.color = 'red';
        errorMessage.style.marginBottom = '10px';
        errorMessage.classList.add('error-message');
        document.getElementById('startPractice').parentNode.insertBefore(errorMessage, document.getElementById('startPractice'));
        return; // Stop further execution
    }

    // Check if nothing is chosen in the time limit dropdown
    const timeLimitDropdown = document.getElementById('timeLimitBtn');
    const selectedTimeLimit = timeLimitDropdown.textContent.trim();
    if (selectedTimeLimit === 'Time limit') {
        // Display error message for no selected time limit
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Please choose a time limit';
        errorMessage.style.color = 'red';
        errorMessage.style.marginBottom = '10px';
        errorMessage.classList.add('error-message');
        document.getElementById('startPractice').parentNode.insertBefore(errorMessage, document.getElementById('startPractice'));
        return; // Stop further execution
    }

    // Extract only the numeric part of the time limit
    const numericTimeLimit = timeLimit ? timeLimit.replace(/\D/g, '') : null; // If timeLimit is null, set numericTimeLimit to null

    // Generate the link based on the selected format, skill, exam, and time limit
    // Redirect the user to the generated link
    let link = `/practice/?format=${selectedFormat.join(',')}&skill=${selectedSkill}&exam=${selectedExam}`;
    if (numericTimeLimit) {
        link += `&time_limit=${numericTimeLimit}`;
    }
    window.location.href = link;
}

// Attach click event listener to the "Start Practice Test" button in the modal
document.getElementById('startPractice').addEventListener('click', function() {
    // Get the selected skill and exam from the dataset of the clicked button
    const selectedSkill = document.getElementById('selectedSkill').dataset.skill;
    const selectedExam = document.getElementById('selectedExam').dataset.exam;

    // Call the function to generate the link with the selected skill, exam, and time limit
    const selectedTimeLimit = document.getElementById('timeLimitBtn').textContent.trim(); // Get the selected time limit
    generateLink(selectedSkill, selectedExam, selectedTimeLimit);
});

// Function to handle link generation for mock test mode
function generateMockTestLink(selectedSkill, selectedExam) {
    // Generate the link based on the selected skill and exam
    // Redirect the user to the generated link
    window.location.href = `/test/?skill=${selectedSkill}&exam=${selectedExam}`;
}

// Attach click event listener to the "START MOCK TEST" button in the modal
document.getElementById('startTestButton').addEventListener('click', function() {
    // Get the selected skill and exam from the dataset of the clicked button
    const selectedSkill = document.getElementById('selectedSkill').dataset.skill;
    const selectedExam = document.getElementById('selectedExam').dataset.exam;

    // Call the function to generate the link for mock test mode
    generateMockTestLink(selectedSkill, selectedExam);
});
