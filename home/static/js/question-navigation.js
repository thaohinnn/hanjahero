function toggleNavBox() {
    const noteBox = document.getElementById('nav-box');
    if (noteBox.classList.contains('show')) {
        noteBox.classList.remove('show');
    } else {
        noteBox.classList.add('show');
    }
}

function scrollToQuestion(questionId) {
    var questionElement = document.getElementById('QuestionNo' + questionId);
    if (questionElement) {
        questionElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}
