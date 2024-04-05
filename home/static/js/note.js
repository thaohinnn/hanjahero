function toggleNoteBox() {
    const noteBox = document.getElementById('note-box');
    if (noteBox.classList.contains('show')) {
        noteBox.classList.remove('show');
    } else {
        noteBox.classList.add('show');
    }
}