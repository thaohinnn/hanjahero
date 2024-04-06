// Function to handle link generation
function generateLink(selectedSkill, selectedExam) {
    // Get the selected format from the checkboxes, skipping any undesired values
    const selectedFormat = Array.from(document.querySelectorAll('input[type=checkbox]:checked'))
        .map(checkbox => checkbox.value)
        .filter(value => !isNaN(value)); // Filter out any non-numeric values

    if (selectedFormat.length === 0) {
        // Display error message
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Please choose at least one task';
        errorMessage.style.color = 'red';
        errorMessage.style.marginBottom = '10px';
        document.getElementById('startPractice').parentNode.insertBefore(errorMessage, document.getElementById('startPractice'));
        return; // Stop further execution
    }

    // Generate the link based on the selected format, skill, and exam
    // Redirect the user to the generated link
    window.location.href = `/mock-test2/?format=${selectedFormat.join(',')}&skill=${selectedSkill}&exam=${selectedExam}`;
}

// Attach click event listener to the "Start Practice Test" button in the modal
document.getElementById('startPractice').addEventListener('click', function() {
    // Get the selected skill and exam from the dataset of the clicked button
    const selectedSkill = document.getElementById('selectedSkill').dataset.skill;
    const selectedExam = document.getElementById('selectedExam').dataset.exam;

    // Call the function to generate the link with the selected skill and exam
    generateLink(selectedSkill, selectedExam);
});

// Function to handle link generation for mock test mode
function generateMockTestLink(selectedSkill, selectedExam) {
    // Generate the link based on the selected skill and exam
    // Redirect the user to the generated link
    window.location.href = `/mock-test2/?skill=${selectedSkill}&exam=${selectedExam}`;
}

// Attach click event listener to the "START MOCK TEST" button in the modal
document.getElementById('startTestButton').addEventListener('click', function() {
    // Get the selected skill and exam from the dataset of the clicked button
    const selectedSkill = document.getElementById('selectedSkill').dataset.skill;
    const selectedExam = document.getElementById('selectedExam').dataset.exam;

    // Call the function to generate the link for mock test mode
    generateMockTestLink(selectedSkill, selectedExam);
});
