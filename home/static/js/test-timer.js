document.addEventListener('DOMContentLoaded', function() {
    const overlay = document.getElementById('overlay');
    const startButton = document.getElementById('startButton');
    let timer; // Declare timer variable outside the event listener scope
    let timerPaused = false; // Flag to track if the timer is paused

    // Show the overlay when the page loads
    overlay.style.display = 'block';

    // Add click event listener to the start button
    startButton.addEventListener('click', function() {
        // Hide the start button once clicked
        startButton.style.display = 'none';

        // Hide the overlay
        overlay.style.display = 'none';

        // Timer logic starts here
        let countdownTime;

        // Check if the URL path corresponds to '/practice'
        if (window.location.pathname === '/practice/') {
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            countdownTime = 1000 * 60 * parseInt(urlParams.get('time_limit'));

            if (isNaN(countdownTime)) {
                // If countdown time is not provided in the query string, set a default time
                countdownTime = 1000 * 60 * 60; // Default to 60 minutes
            }

            // Create a stop timer button
            const stopTimerButton = document.getElementById('timer-icon');

            // Add event listener to stop timer button
            stopTimerButton.addEventListener('click', function() {
                if (!timerPaused) {
                    clearInterval(timer); // Stop the timer
                    document.getElementById('timer-icon').classList.remove('fa-stop');
                    document.getElementById('timer-icon').classList.add('fa-play');
                } else {
                    // Resume the timer
                    timer = startTimer(countdownTime);
                    document.getElementById('timer-icon').classList.remove('fa-play');
                    document.getElementById('timer-icon').classList.add('fa-stop');
                }
                timerPaused = !timerPaused; // Toggle timerPaused flag
            });
        } else {
            // Default countdown time for other paths (e.g., '/test')
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const countdownOption = urlParams.get('skill');

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
        }

        // Start the timer
        timer = startTimer(countdownTime);
    });

    // Function to start the timer
    function startTimer(countdownTime) {
        let eventDate = new Date().getTime() + countdownTime;

        return setInterval(() => {
            const actualTime = new Date().getTime();
            let difference = eventDate - actualTime;

            // Update the eventDate if it's in the past
            if (difference < 0) {
                clearInterval(timer);
                difference = 0; // Set difference to 0 to prevent negative countdown
            }

            const minutes = Math.floor(difference / (1000 * 60)); // Calculate minutes
            const seconds = Math.floor((difference % (1000 * 60)) / 1000); // Calculate seconds

            // Update the UI with the countdown values
            const minDozens = Math.floor(minutes / 10);
            const minUnity = Math.floor(minutes % 10);
            const secDozens = Math.floor(seconds / 10);
            const secUnity = Math.floor(seconds % 10);

            document.getElementById('min-dozens').innerHTML = minDozens;
            document.getElementById('min-unity').innerHTML = minUnity;
            document.getElementById('sec-dozens').innerHTML = secDozens;
            document.getElementById('sec-unity').innerHTML = secUnity;

            // Remove blur class from timer elements
            document.getElementById('min-dozens').classList.remove('timer-blur');
            document.getElementById('min-unity').classList.remove('timer-blur');
            document.getElementById('sec-dozens').classList.remove('timer-blur');
            document.getElementById('sec-unity').classList.remove('timer-blur');

            if (difference <= 1000) { // Check if difference is less than or equal to 1000 milliseconds (1 second)
                // Display "Time's up!" message and trigger click on the submit button
                clearInterval(timer);
                document.getElementById('submitTestButton').click();
            }
        }, 200);
    }
});