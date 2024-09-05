document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.getElementById('likeButton');
    const likeIcon = document.getElementById('likeIcon');
    const likeCount = document.getElementById('likeCount');
    let liked = false;

    likeButton.addEventListener('click', function() {
        if (!liked) {
            likeIcon.classList.add('liked');
            likeCount.textContent = parseInt(likeCount.textContent) + 1;
            liked = true;
        } else {
            likeIcon.classList.remove('liked');
            likeCount.textContent = parseInt(likeCount.textContent) - 1;
            liked = false;
        }
    });
});