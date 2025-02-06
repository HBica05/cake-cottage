// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', () => {
    // Select the comment form by its ID
    const commentForm = document.querySelector('#comment-form');

    // Check if the comment form exists on the page
    if (commentForm) {
        // Add an event listener to the form to handle the submit event
        commentForm.addEventListener('submit', async (event) => {
            // Prevent the default form submission behavior (which would reload the page)
            event.preventDefault();
            
            // Get the comment content from the input field
            const content = document.querySelector('#comment-content').value;
            
            // Get the recipe ID from a custom data attribute on the form
            const recipeId = commentForm.dataset.recipeId;

            // Send the comment data to the server using the Fetch API
            const response = await fetch(`/recipes/${recipeId}/comment/`, {
                method: 'POST', // Use POST method to submit the comment
                body: new URLSearchParams({
                    // Send the comment content and the CSRF token in the request body
                    content: content,
                    csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
                }),
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, // Set the request content type
            });