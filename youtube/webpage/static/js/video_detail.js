
document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.getElementById('like-button');
    const likeIcon = document.getElementById('like-icon');
    const likeCount = document.getElementById('like-count');

    likeButton.addEventListener('click', function() {
        const isLiked = likeButton.getAttribute('data-liked') === 'true';

        if (!isLiked) {
            // Add like animation
            likeIcon.classList.add('animate-like');
            setTimeout(() => likeIcon.classList.remove('animate-like'), 300);

            // Increment the like count
            likeCount.textContent = parseInt(likeCount.textContent) + 1;
            likeButton.setAttribute('data-liked', 'true');

            // Change the like button color
            likeButton.style.color = "linear-gradient(45deg, orange, blue, purple, red)";

        } else {
            // Remove like and revert back
            likeCount.textContent = parseInt(likeCount.textContent) - 1;
            likeButton.setAttribute('data-liked', 'false');
            likeButton.style.color = "#606060";
        }
    });
});

