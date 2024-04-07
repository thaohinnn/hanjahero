let isHighlightMode = false;
let highlightedText = '';
let highlightButton = document.getElementById('highlight-button');

function toggleHighlightMode() {
    isHighlightMode = !isHighlightMode;
    if (isHighlightMode) {
        document.addEventListener('mouseup', highlightText);
        document.addEventListener('keydown', keydownHandler);
        highlightButton.style.transform = 'scale(2)'; // Increase button size
    } else {
        document.removeEventListener('mouseup', highlightText);
        document.removeEventListener('keydown', keydownHandler);
        highlightButton.style.transform = 'scale(1)'; // Reset button size
    }
}

function highlightText() {
    const selection = window.getSelection();
    highlightedText = selection.toString();
    const range = selection.getRangeAt(0);
    const span = document.createElement('span');
    span.className = 'highlight';
    range.surroundContents(span);
}

function keydownHandler(event) {
    toggleHighlightMode(); // Turn off highlight mode on any key press
}
