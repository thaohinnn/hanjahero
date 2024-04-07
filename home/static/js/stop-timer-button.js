document.addEventListener('DOMContentLoaded', function() {
    let timer; // Declare timer variable outside the event listener scope
    let timerRunning = true; // Flag to track if the timer is running
    let timerPaused = true; // Flag to track if the timer is paused

    function toggleTimer() {
        if (timerRunning && !timerPaused) {
            clearInterval(timer); // Stop the timer
            document.getElementById('timer-icon').classList.remove('fa-stop');
            document.getElementById('timer-icon').classList.add('fa-play');
            timerPaused = true; // Pause the timer
        } else {
            // Start or resume the timer
            const countdownTime = calculateTimeRemaining(); // Calculate remaining time
            timer = startTimer(countdownTime);
            document.getElementById('timer-icon').classList.remove('fa-stop');
            document.getElementById('timer-icon').classList.add('fa-play');
            timerPaused = false; // Resume the timer
        }
        timerRunning = !timerRunning; // Toggle timerRunning flag
    }

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
                toggleTimer(); // Stop the timer
            }

            // Your timer logic here...
            const minutes = Math.floor(difference / (1000 * 60)); // Calculate minutes
            const seconds = Math.floor((difference % (1000 * 60)) / 1000); // Calculate seconds

            console.log(`${minutes}:${seconds}`);

        }, 200);
    }

    // Function to calculate remaining time
    function calculateTimeRemaining() {
        // Calculate remaining time based on your application logic
        return 1000 * 60 * 60; // Default to 60 minutes
    }

    // Add event listener to the timer button
    document.getElementById('timer-button').addEventListener('click', toggleTimer);
});
