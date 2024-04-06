document.addEventListener('DOMContentLoaded', function() {
    // Check if the tour has been completed
    const tourCompleted = localStorage.getItem('tourCompleted');

    // If the tour has not been completed, initialize and start the tour
    if (!tourCompleted) {
        // Initialize the tour
        const tour = new Tour({
            steps: [
                {
                    element: ".brand-logo",
                    title: "Welcome to our website!",
                    content: "This is our logo. Click on it to go back to the homepage.",
                },
                {
                    element: ".timer-wrapper",
                    title: "Timer",
                    content: "This is the timer. It shows how much time you have left.",
                },
                {
                    element: "#note-button",
                    title: "Take Notes",
                    content: "Click on the icon to write down your notes. Click on it again to exit the notes.",
                },
                {
                    element: "#highlight-button",
                    title: "Highlighter",
                    content: "This is the highlighter tool. Click on the pen, and highlight the text. Click the icon or press any key to stop.",
                },
                {
                    element: "#fullscreen-button",
                    title: "Fullscreen",
                    content: "Click here to enable full screen.",
                },
                {
                    element: ".btn-submit",
                    title: "Submit",
                    content: "When you are done, you can click here to submit right away.",
                }
            ],
            backdrop: true,
            backdropPadding: 10
        });

        // Initialize the tour
        tour.init();

        // Start the tour
        tour.start();
    }

    // Mark the tour as completed after it finishes
    tour.on('end', function() {
        localStorage.setItem('tourCompleted', true);
    });
});