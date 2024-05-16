// Function to open modal and generate checkboxes for formats
function openModal(skillNumber) {
    generateCheckboxes(skillNumber); // Generate checkboxes for formats
    $('#myModalLarge').modal('show'); // Show modal
}

// Function to generate checkboxes for the selected skill
function generateCheckboxes(skill) {
    const checkboxesContainer = document.getElementById('checkboxContainer');
    checkboxesContainer.innerHTML = ''; // Clear previous content

    const formats = format_by_skill[skill];
    formats.forEach(formatNumber => {
        const formatDescription = format[formatNumber - 1][formatNumber];

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.value = formatNumber;
        checkbox.id = `format_${formatNumber}`;

        const label = document.createElement('label');
        label.htmlFor = `format_${formatNumber}`;
        label.style.display = 'inline'; // Make the label display inline
        label.style.lineHeight = '2.2'; // Adjust line height of each checkbox line

        // Add space between checkbox and text
        label.innerHTML = '&nbsp;' + formatDescription;

        checkboxesContainer.appendChild(checkbox);
        checkboxesContainer.appendChild(label);
        checkboxesContainer.appendChild(document.createElement('br'));
    });
}
