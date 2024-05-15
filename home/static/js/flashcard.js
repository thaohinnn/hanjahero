var currentIndex = 0;
var flashcards = document.querySelectorAll('.carousel-item');
var wordCounter = document.getElementById('wordCounter');


function shuffleFlashcards() {
    currentIndex = 0;
    for (var i = flashcards.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        flashcards[i].parentNode.insertBefore(flashcards[j], flashcards[i]);
    }
    updateWordCounter();
}

function toggleMeaning(card) {
    var front = card.querySelector('.front');
    var back = card.querySelector('.back');

    if (front.style.display === 'none') {
        front.style.display = 'block';
        back.style.display = 'none';
    } else {
        front.style.display = 'none';
        back.style.display = 'block';
    }
}

// Initial word counter update
updateWordCounter();

function fetchRandomFlashcards() {
    // AJAX request to fetch random flashcard sets from the backend
    $.ajax({
        url: '/flashcard-set/<int:pk>',
        type: 'GET',
        success: function(response) {
            // Update the content of the "Other Flashcards Suggestions" section with the fetched data
            $('#randomFlashcards').html(response);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching random flashcard sets:', error);
        }
    });
}

// Call the function to fetch and display random flashcard sets when the page loads
$(document).ready(function() {
    fetchRandomFlashcards();
});


document.addEventListener('DOMContentLoaded', function() {
    var flashcardsContainer = document.querySelector('.flashcards-container');
    if (flashcardsContainer) {
        flashcardsContainer.addEventListener('click', function() {
            this.style.filter = 'none'; // Remove blur effect
        });
    } else {
        console.error('Element with class "flashcards-container" not found.');
    }
});
