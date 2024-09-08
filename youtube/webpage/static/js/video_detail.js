document.getElementById('like-button').addEventListener('click', function() {
    const likeButton = this;
    const likeIcon = document.getElementById('like-icon');
    const likeCount = document.getElementById('like-count');

    // Toggle the like status
    let isLiked = likeButton.getAttribute('data-liked') === 'true';
    
    // Perform the animation
    likeIcon.classList.add('animate-like');

    // Send the like/unlike request via AJAX
    fetch(likeButton.form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ liked: !isLiked })
    })
    .then(response => response.json())
    .then(data => {
        // Update the like count and toggle the liked status
        likeCount.textContent = data.likes;
        likeButton.setAttribute('data-liked', data.is_liked ? 'true' : 'false');

        // Reset animation after it's done
        setTimeout(() => likeIcon.classList.remove('animate-like'), 500);
    })
    .catch(error => console.error('Error:', error));
});