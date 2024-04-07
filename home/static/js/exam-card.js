// Function to generate cards for each exam
function generateExamCards() {
    const examCardContainer = document.getElementById('examCardContainer');

    // Clear previous cards
    examCardContainer.innerHTML = '';

    // Iterate through exam list and create cards
    // Iterate through exam list and create cards
    exam_list.forEach((exam, index) => {
        const examNumber = Object.keys(exam)[0];
        const examName = Object.values(exam)[0];

        // Create exam card
        const examCard = document.createElement('div');
        examCard.classList.add('card', 'mb-3');
        examCard.style.textAlign = 'center';
        examCard.style.borderRadius = '20px';
        examCard.style.borderColor = '#fff';
        examCard.style.boxShadow = '-4px -4px 8px rgba(0, 0, 0, 0.02)';

        // Store exam number in a data attribute
        examCard.dataset.examNumber = examNumber;

        const examCardHeader = document.createElement('h1');
        examCardHeader.classList.add('card-header');
        examCardHeader.style.fontWeight = 'bolder';
        examCardHeader.textContent = examName;
        examCard.appendChild(examCardHeader);

        const examCardBody = document.createElement('div');
        examCardBody.classList.add('card-body', 'd-flex', 'flex-wrap');
        examCard.appendChild(examCardBody);

        // Iterate through skill list and create skill cards
        skill_list.forEach((skill, skillIndex) => {
            const skillNumber = Object.keys(skill)[0];
            const skillInfo = Object.values(skill)[0];

            // Create skill card
            const skillCard = document.createElement('div');
            skillCard.classList.add('card', 'mb-3', 'mr-3');
            skillCard.style.borderRadius = '20px';
            skillCard.style.borderColor = `rgba(${parseInt(colors[skillIndex % colors.length].substring(1, 3), 16)}, ${parseInt(colors[skillIndex % colors.length].substring(3, 5), 16)}, ${parseInt(colors[skillIndex % colors.length].substring(5, 7), 16)}, 0.2)`;
            skillCard.style.width = '30%';
            skillCard.style.boxShadow = 'none';

            const skillCardBody = document.createElement('div');
            skillCardBody.classList.add('card-body');
            skillCardBody.style.fontSize = '17px';
            skillCardBody.style.lineHeight = '200%';
            skillCardBody.style.whiteSpace = 'nowrap';

            // Create image element for skill
            const imgSkill = document.createElement('img');
            imgSkill.src = skillInfo.img;
            imgSkill.style.width = '40px'; // Adjust image width as needed
            skillCardBody.appendChild(imgSkill);

            // Create skill name element
            const skillTitle = document.createElement('h5');
            skillTitle.classList.add('card-title');
            skillTitle.innerHTML = `
            <span style="display: inline-block; font-weight: bolder; font-size: 20px; line-height: 2.5; color: ${colors[skillIndex % colors.length]}">${skillInfo.name}</span>
        `;
            skillCardBody.appendChild(skillTitle);

            // Create "Start Test" button
            const takeTestButton = document.createElement('button');
            takeTestButton.classList.add('btn', 'btn-oval', 'btn-secondary');
            takeTestButton.type = 'button';
            takeTestButton.textContent = 'Take Test';
            takeTestButton.style.backgroundColor = colors[skillIndex % colors.length];
            takeTestButton.style.color = '#fff';// Set button color
            takeTestButton.style.border = 'none';

            // Store exam number and skill number in data attributes
            takeTestButton.dataset.examNumber = examNumber;
            takeTestButton.dataset.skillNumber = skillNumber;

            takeTestButton.addEventListener('click', function () {
                openModal(skillNumber);
            });
            skillCardBody.appendChild(takeTestButton);

            // Add skill card body to skill card
            skillCard.appendChild(skillCardBody);

            // Add skill card to exam card body
            examCardBody.appendChild(skillCard);
        });

        // Add exam card to container
        examCardContainer.appendChild(examCard);
    });
}

// Call the function to generate exam cards
generateExamCards();

// Function to handle click event on skill and exam cards
function handleClick(event) {
    const target = event.target;

    // Check if the clicked element or its parent is a skill or exam card
    if (target.classList.contains('btn') && target.textContent === 'Take Test') {
        // Retrieve the selectedSkill and selectedExam from the clicked button's dataset
        const selectedSkill = target.dataset.skillNumber;
        const selectedExam = target.dataset.examNumber;

        // Set the selectedSkill and selectedExam in the HTML
        document.getElementById('selectedSkill').dataset.skill = selectedSkill;
        document.getElementById('selectedExam').dataset.exam = selectedExam;

        // Use the retrieved IDs as needed
        console.log('Selected Skill:', selectedSkill);
        console.log('Selected Exam:', selectedExam);
    }
}

// Attach click event listener to the container of exam cards
document.getElementById('examCardContainer').addEventListener('click', handleClick);
