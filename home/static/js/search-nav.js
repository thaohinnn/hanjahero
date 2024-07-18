document.querySelector('.search-form').addEventListener('submit', function(event) {
    // Optional: Prevent default form submission
    event.preventDefault();

    // Get the search query
    const query = document.querySelector('.search-form input[name="query"]').value;

    // Example action: log query to console or redirect to search results page
    console.log('Search query:', query);

    // Example redirect (if needed)
    window.location.href = `/search?query=${encodeURIComponent(query)}`;
});
