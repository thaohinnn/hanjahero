document.addEventListener('DOMContentLoaded', function() {
    // Get the query string from the URL
    const queryString = window.location.search;

    // Parse the query string to extract the parameters
    const urlParams = new URLSearchParams(queryString);
    const skill = urlParams.get('skill');
    const exam = urlParams.get('exam');

    // Store the parameters in local storage
    localStorage.setItem('skill', skill);
    localStorage.setItem('exam', exam);

    // Log the retrieved parameters to the console
    console.log('Skill:', skill);
    console.log('Exam:', exam);

});
