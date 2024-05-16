document.addEventListener('DOMContentLoaded', function() {
    const overlay = document.getElementById('overlay');
    const startButton = document.getElementById('startButton');
    const timeLimitField = document.getElementById('timeLimit'); // Get the hidden input field
    let timer; // Declare timer variable outside the event listener scope
    let remainingTime; // Track remaining time
    let timerPaused = true; // Initially paused until 'start' is clicked

    // Show the overlay when the page loads
    overlay.style.display = 'block';

    // Add click event listener to the start button
    startButton.addEventListener('click', function() {
        // Hide the start button once clicked
        startButton.style.display = 'none';

        // Hide the overlay
        overlay.style.display = 'none';

        let initialCountdownTime;

        // Check if the URL path corresponds to '/practice'
        if (window.location.pathname === '/practice/') {
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            initialCountdownTime = 1000 * 60 * parseInt(urlParams.get('time_limit'));

            if (isNaN(initialCountdownTime)) {
                // If countdown time is not provided in the query string, set a default time
                initialCountdownTime = 1000 * 60 * 60; // Default to 60 minutes
            }
        } else {
            // Default countdown time for other paths (e.g., '/test')
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const countdownOption = urlParams.get('skill');

            switch (countdownOption) {
                case '1':
                    initialCountdownTime = 1000 * 60 * 50; // 50 minutes
                    break;
                case '2':
                    initialCountdownTime = 1000 * 60 * 60; // 60 minutes
                    break;
                case '3':
                    initialCountdownTime = 1000 * 60 * 70; // 70 minutes
                    break;
                default:
                    initialCountdownTime = 1000 * 60 * 60; // Default to 60 minutes if no valid option is provided
                    break;
            }
        }

        timeLimitField.value = Math.round(initialCountdownTime / (1000 * 60));

        if (timerPaused) { // Initial start
            remainingTime = initialCountdownTime;
            timer = startTimer();
            timerPaused = false;
        }
    });

    // Function to start the timer
    function startTimer() {
        let eventDate = new Date().getTime() + remainingTime;

        return setInterval(() => {
            const actualTime = new Date().getTime();
            remainingTime = eventDate - actualTime;

            // Update the eventDate if it's in the past
            if (remainingTime < 0) {
                clearInterval(timer);
                remainingTime = 0; // Set remainingTime to 0 to prevent negative countdown
            }

            updateUI(remainingTime); // Call a function to update the UI

            if (remainingTime <= 1000) { // Check if remainingTime is less than or equal to 1000 milliseconds (1 second)
                clearInterval(timer);
                document.getElementById('submitTestButton').click(); // Simulate test submission
            }
        }, 200);
    }

    // Function to update the UI based on remaining time
    function updateUI(difference) {
        const minutes = Math.floor(difference / (1000 * 60)); // Calculate minutes
        const seconds = Math.floor((difference % (1000 * 60)) / 1000); // Calculate seconds

        // Update the UI with the countdown values
        document.getElementById('min-dozens').innerHTML = Math.floor(minutes / 10);
        document.getElementById('min-unity').innerHTML = Math.floor(minutes % 10);
        document.getElementById('sec-dozens').innerHTML = Math.floor(seconds / 10);
        document.getElementById('sec-unity').innerHTML = Math.floor(seconds % 10);
    }

    // Handle pause and resume functionality
    const stopTimerButton = document.getElementById('timer-icon');
    stopTimerButton.addEventListener('click', function() {
        if (!timerPaused) {
            clearInterval(timer); // Stop the timer
            stopTimerButton.classList.remove('fa-play');
            stopTimerButton.classList.add('fa-stop');
        } else {
            timer = startTimer(); // Resume the timer
            stopTimerButton.classList.remove('fa-stop');
            stopTimerButton.classList.add('fa-play');
        }
        timerPaused = !timerPaused; // Toggle timerPaused flag
    });
});
