let isHighlightMode = false;
let highlightedText = '';
let highlightButton = document.getElementById('highlight-button');

function toggleHighlightMode() {
    isHighlightMode = !isHighlightMode;
    if (isHighlightMode) {
        document.addEventListener('mouseup', handleMouseUp);
        document.addEventListener('keydown', keydownHandler);
        highlightButton.style.transform = 'scale(2)'; // Increase button size
    } else {
        document.removeEventListener('mouseup', handleMouseUp);
        document.removeEventListener('keydown', keydownHandler);
        highlightButton.style.transform = 'scale(1)'; // Reset button size
    }
}

function handleMouseUp() {
    if (!window.getSelection().isCollapsed) {
        highlightText();
    }
}


function highlightText() {
    const selection = window.getSelection();
    highlightedText = selection.toString();
    if (highlightedText.trim().length === 0) return; // Prevents creating empty spans

    const range = selection.getRangeAt(0);
    const span = document.createElement('span');
    span.className = 'highlight';
    span.style.backgroundColor = 'yellow'; // Optional: Directly set the background color here
    span.onclick = removeHighlight; // Attach click event to remove highlight
    range.surroundContents(span);
    selection.removeAllRanges(); // Deselect text after highlighting
}

function removeHighlight(event) {
    const span = event.target;
    const parent = span.parentNode;
    while (span.firstChild) {
        parent.insertBefore(span.firstChild, span);
    }
    parent.removeChild(span);
    parent.normalize(); // Merges adjacent text nodes into one
}


function keydownHandler(event) {
    toggleHighlightMode(); // Turn off highlight mode on any key press
}
