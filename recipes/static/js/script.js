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

            // If the request is successful (status code 200-299)
            if (response.ok) {
                // Parse the response JSON to get the new comment data
                const newComment = await response.json();
                
                // Find the section where comments are displayed on the page
                const commentsSection = document.querySelector('.comments');
                
                // Create a new div element to display the new comment
                const newCommentElement = document.createElement('div');
                newCommentElement.classList.add('comment'); // Add a class for styling
                
                // Set the inner HTML of the new comment element with the comment details
                newCommentElement.innerHTML = `
                    <p><strong>${newComment.user}</strong>: ${newComment.content}</p>
                    <p><small>${newComment.created_at}</small></p>
                `;
                
                // Append the new comment element to the comments section
                commentsSection.appendChild(newCommentElement);
                
                // Clear the comment input field after the form is submitted
                document.querySelector('#comment-content').value = ''; 
                
            }
        });
    }
});