document.addEventListener('DOMContentLoaded', function() {
    const overlay = document.getElementById('overlay');
    const startButton = document.getElementById('startButton');

    // Show the overlay when the page loads
    overlay.style.display = 'block';

    // Add click event listener to the start button
    startButton.addEventListener('click', function() {
        // Hide the start button once clicked
        startButton.style.display = 'none';

        // Hide the overlay
        overlay.style.display = 'none';

        // Timer logic starts here
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        const countdownOption = urlParams.get('skill');

        let countdownTime;

        switch (countdownOption) {
            case '1':
                countdownTime = 1000 * 60 * 50; // 50 minutes
                break;
            case '2':
                countdownTime = 1000 * 60 * 60; // 60 minutes
                break;
            case '3':
                countdownTime = 1000 * 60 * 70; // 70 minutes
                break;
            default:
                countdownTime = 1000 * 60 * 60; // Default to 60 minutes if no valid option is provided
                break;
        }

        let eventDate = new Date().getTime() + countdownTime;

        const timer = setInterval(() => {
            const actualTime = new Date().getTime();
            let difference = eventDate - actualTime;

            // Update the eventDate if it's in the past
            if (difference < 0) {
                clearInterval(timer);
                difference = 0; // Set difference to 0 to prevent negative countdown
            }

            const minutes = Math.floor(difference / (1000 * 60)); // Calculate minutes
            const seconds = Math.floor((difference % (1000 * 60)) / 1000); // Calculate seconds

            const minDozens = Math.floor(minutes / 10);
            const minUnity = Math.floor(minutes % 10);
            const secDozens = Math.floor(seconds / 10);
            const secUnity = Math.floor(seconds % 10);

            const hMinDozens = document.getElementById('min-dozens');
            const hMinUnits = document.getElementById('min-unity');
            const hSecDozens = document.getElementById('sec-dozens');
            const hSecUnits = document.getElementById('sec-unity');

            hMinDozens.innerHTML = minDozens;
            hMinUnits.innerHTML = minUnity;
            hSecDozens.innerHTML = secDozens;
            hSecUnits.innerHTML = secUnity;

            hMinDozens.classList.remove('timer-blur');
            hMinUnits.classList.remove('timer-blur');
            hSecDozens.classList.remove('timer-blur');
            hSecUnits.classList.remove('timer-blur');

            if (difference < 0) {
                document.getElementById('message').innerHTML = "Time's up!";
                clearInterval(timer);
                // Trigger click on the submit button after the timer ends
                document.getElementById('submitButton').click();
            }
        }, 200);
    });
});
