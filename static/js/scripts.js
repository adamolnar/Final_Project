// ----------------    profile.html | toggle the visibility of the posts --------------------------

// To display four recent posts in profile.html and provide a "Show More" link to reveal additional posts
document.addEventListener('DOMContentLoaded', function() {
  // Get references to HTML elements
  var postContainer = document.getElementById('postContainer');
  var postCards = postContainer.getElementsByClassName('extrapost');
  var showMoreLink = document.getElementById('showMoreLink');

  // Set the number of initially visible posts
  var visiblePosts = 4;
  var totalPosts = postCards.length;

  // Initial display of posts
  for (var i = 0; i < totalPosts; i++) {
      if (i < visiblePosts) {
          postCards[i].style.display = 'block';
      } else {
          postCards[i].style.display = 'none';
      }
  }

  // Show all posts when the "Show More" link is clicked
  showMoreLink.addEventListener('click', function() {
      for (var i = visiblePosts; i < totalPosts; i++) {
          postCards[i].style.display = 'block';
      }

      // Hide the "Show More" link after revealing all posts
      showMoreLink.style.display = 'none';
  });
});



