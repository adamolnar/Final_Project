# Manual Testing for index.html Template

## Test Case ID: TC001

### Test Case Title: Blog Page Rendering

**Test Description:** This test case ensures that the blog page template renders correctly, displaying blog posts, tags, categories, and additional content.

### Preconditions:
- The Django application is up and running.
- Sample blog posts, tags, and categories are available in the database.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the blog page, e.g., [index.html](https://final-project-ada-02b27917ae0c.herokuapp.com/).

**Expected Results:**
- The blog page should load without errors.
- The page should display a header with the site logo and tagline.
- The page should contain a section for the main post (full width).
- The main post section should display the title, content, author, and publication date of the latest blog post.
- Tags and categories should be displayed on the page.
- The "About Us" section should provide information about the blog.

### Postconditions:
- The blog page should be displayed correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Tags and Categories Display

**Test Description:** This test case verifies that the tags and categories are displayed correctly on the blog page.

### Preconditions:
- The blog page is loaded.

### Test Steps:

1. Check the "Tags" section of the page.

**Expected Results:**
- The "Tags" section should display a list of clickable tags.
- Each tag should link to the corresponding tag filter page.

2. Check the "Categories" section of the page.

**Expected Results:**
- The "Categories" section should display a list of clickable categories.
- Each category should link to the corresponding category filter page.

### Postconditions:
- Tags and categories should be displayed correctly and link to the expected pages.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Secondary Blog Posts

**Test Description:** This test case verifies that secondary blog posts are displayed correctly below the main post.

### Preconditions:
- The blog page is loaded.

### Test Steps:

1. Check the section with secondary blog posts.

**Expected Results:**
- Secondary blog posts (posts 2 and 3) should be displayed.
- Each post should show the title, author, and publication date.
- Clicking on a post should navigate to the full post page.

### Postconditions:
- Secondary blog posts should be displayed correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Pagination

**Test Description:** This test case checks if pagination is working as expected on the blog page.

### Preconditions:
- The blog page is loaded.

### Test Steps:

1. Check the pagination section at the bottom of the page.

**Expected Results:**
- Pagination links should be displayed, allowing navigation to previous and next pages.
- The current page number should be indicated.
- Clicking on pagination links should load the corresponding page with the correct content.

### Postconditions:
- Pagination should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Responsive Design

**Test Description:** This test case verifies the responsiveness of the blog page template on different screen sizes.

### Preconditions:
- The blog page is loaded.

### Test Steps:

1. Resize the web browser to various screen sizes, including desktop, tablet, and mobile dimensions.

**Expected Results:**
- The blog page should adapt to different screen sizes, maintaining readability and usability.
- Navigation menus, content layout, and images should adjust accordingly.

### Postconditions:
- The blog page should be responsive on various devices.

### Test Status:
- [ ] Pass
- [ ] Fail

<hr>

# Manual Testing for byte_by_byte.html Template

## Test Case ID: TC001

### Test Case Title: Landing Page Content

**Test Description:** This test case ensures that the landing page of the Byte by Byte Tech Blog displays the expected content accurately.

### Preconditions:
- The Django application is up and running.
- The user is accessing the landing page.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the landing page, e.g., [byte_by_byte.html](https://final-project-ada-02b27917ae0c.herokuapp.com/blog/byte_by_byte/).

**Expected Results:**
- The landing page should load without errors.
- The page should display the following content accurately:
  - A title: "Explore Byte by Byte Tech Blog"
  - A description welcoming users to the blog.
  - Information about what readers will find on the blog, including expert articles, tutorials, tech news, and community engagement.
  - A section explaining why to choose Byte by Byte, highlighting quality content, an education-first approach, interactive experience, and regular updates.
  - A call to action inviting users to explore the blog.
  
### Postconditions:
- The landing page content should be displayed accurately.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Responsive Design

**Test Description:** This test case verifies the responsiveness of the landing page template on different screen sizes.

### Preconditions:
- The landing page is loaded.

### Test Steps:

1. Resize the web browser to various screen sizes, including desktop, tablet, and mobile dimensions.

**Expected Results:**
- The landing page should adapt to different screen sizes, maintaining readability and usability.
- Text and images should adjust accordingly to provide a good user experience.

### Postconditions:
- The landing page should be responsive on various devices.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>


# Manual Testing for post_detail.html Template

## Test Case ID: TC001

### Test Case Title: Blog Post Page Rendering

**Test Description:** This test case ensures that the blog post page template renders correctly, displaying the blog post's content, author, comments, and social sharing buttons.

### Preconditions:
- The Django application is up and running.
- A sample blog post with comments and social sharing options is available in the database.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of a specific blog post, e.g., [post_detail.html](https://final-project-ada-02b27917ae0c.herokuapp.com/post/jumpstart-your-python-journey/).

**Expected Results:**
- The blog post page should load without errors.
- The page should display the following elements accurately:
  - Post image (if available).
  - Post tags as badges.
  - Post title.
  - Post author's name and a link to their profile.
  - Post creation date.
  - Edit, publish, and delete buttons (if the current user is the post author).
  - Post content with proper formatting.
  - Number of likes with a heart icon.
  - Total comments count with a comments icon.
  - Social sharing buttons for WhatsApp, Twitter, Facebook, and LinkedIn.
  - Comment section displaying existing comments with author, date, and content.
  - Comment update and delete buttons (for the comment author).

### Postconditions:
- The blog post page should display all elements accurately.

### Test Status:
- [ ] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Commenting on the Blog Post

**Test Description:** This test case checks the functionality of adding comments to a blog post.

### Preconditions:
- The blog post page is loaded.

### Test Steps:

1. Check the comment section at the bottom of the page.

**Expected Results:**
- Authenticated users should see a comment form.
- Submitting a comment should add it to the comment section.
- An alert message should confirm the successful addition of a comment (if applicable).

2. If not authenticated, verify the alert message instructing the user to register.

**Expected Results:**
- An alert message should inform unauthenticated users about the need to register to leave a comment.

### Postconditions:
- Commenting on the blog post should work as expected.

### Test Status:
- [ ] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Responsive Design

**Test Description:** This test case verifies the responsiveness of the blog post page template on different screen sizes.

### Preconditions:
- The blog post page is loaded.

### Test Steps:

1. Resize the web browser to various screen sizes, including desktop, tablet, and mobile dimensions.

**Expected Results:**
- The blog post page should adapt to different screen sizes, maintaining readability and usability.
- Text, images, and buttons should adjust accordingly to provide a good user experience.

### Postconditions:
- The blog post page should be responsive on various devices.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Social Sharing Buttons

**Test Description:** This test case checks the functionality of social sharing buttons on the blog post page.

### Preconditions:
- The blog post page is loaded.

### Test Steps:

1. Click on each social sharing button (WhatsApp, Twitter, Facebook, LinkedIn).

**Expected Results:**
- Clicking on a social sharing button should open a new window or pop-up with the corresponding social media platform.
- The post title and URL should be pre-populated for sharing.

### Postconditions:
- Social sharing buttons should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail