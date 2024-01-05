# Manual Testing for base.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the base template of the Django application renders correctly and displays all required elements.

### Preconditions:
- The Django web application is running.
- The base template is used as the layout for web pages.

### Test Steps:

1. Open a web browser.

2. Navigate to different pages of the web application that use the base template.

**Expected Results:**
- The base template should render without errors on all pages.
- The template should consistently display the following elements accurately across all pages:
  - Navigation bar with the application name and navigation links.
  - Display of user authentication status (e.g., "Logout," "Login," "Register," or "Profile").
  - Display of flash messages (e.g., success, warning, or error messages).
  - Footer with copyright information.

### Postconditions:
- The base template should render correctly on all pages.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Navigation Links

**Test Description:** This test case checks the functionality of navigation links in the base template.

### Preconditions:
- The base template is loaded.

### Test Steps:

1. Click on each navigation link in the navigation bar, such as "Home," "Bloggers," "Contact," "Logout," "Login," "Register," "Profile," and "Create Post" (if applicable).

**Expected Results:**
- Clicking on each navigation link should navigate to the respective page or perform the respective action.
- The navigation links should work as expected based on user authentication status.

### Postconditions:
- Navigation links in the base template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Flash Messages

**Test Description:** This test case verifies the display and functionality of flash messages in the base template.

### Preconditions:
- The base template is loaded.

### Test Steps:

1. Perform actions that trigger flash messages (e.g., registration, login, logout, form submissions, etc.).

**Expected Results:**
- Flash messages should appear at the top of the page to provide feedback to the user.
- Flash messages should display with different styles based on their type (e.g., success, warning, error).
- Flash messages should automatically close after a certain time period.

### Postconditions:
- Flash messages in the base template should be displayed and dismissed correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Responsive Design

**Test Description:** This test case checks the responsiveness of the base template on various screen sizes.

### Preconditions:
- The base template is loaded.

### Test Steps:

1. Open the web application on different devices or resize the web browser window to various screen sizes (e.g., desktop, tablet, mobile).

**Expected Results:**
- The base template should adapt and display correctly on different screen sizes.
- Navigation bar elements should collapse into a mobile-friendly menu on smaller screens.

### Postconditions:
- The base template should be responsive and display correctly on different screen sizes.

### Test Status:
- [X] Pass
- [ ] Fail



<hr>
---------------------------------------------------------------------------------------------------------


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
---------------------------------------------------------------------------------------------------------


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


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for author_list.html Template

## Test Case ID: TC001

### Test Case Title: Blogger List Page Rendering

**Test Description:** This test case ensures that the blogger list page template renders correctly, displaying a list of bloggers, their profiles, and recent posts.

### Preconditions:
- The Django application is up and running.
- There are blogger profiles available in the database, with associated recent blog posts.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the blogger list page, e.g., [author_list.html](https://final-project-ada-02b27917ae0c.herokuapp.com/authors/).

**Expected Results:**
- The blogger list page should load without errors.
- The page should display the following elements accurately for each blogger:
  - Blogger profile image (or default image if not available).
  - Blogger name with a link to their profile page.
  - Blogger's "About Me" section, truncated to a maximum of 5 words.
  - A list of up to 3 of the blogger's latest published posts, including post images (if available) and truncated titles.

### Postconditions:
- The blogger list page should display all elements accurately.

### Test Status:
- [ ] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Responsive Design

**Test Description:** This test case verifies the responsiveness of the blogger list page template on different screen sizes.

### Preconditions:
- The blogger list page is loaded.

### Test Steps:

1. Resize the web browser to various screen sizes, including desktop, tablet, and mobile dimensions.

**Expected Results:**
- The blogger list page should adapt to different screen sizes, maintaining readability and usability.
- Blogger profiles, images, and post previews should adjust accordingly to provide a good user experience.

### Postconditions:
- The blogger list page should be responsive on various devices.

### Test Status:
- [ ] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Blogger Profile Link

**Test Description:** This test case checks the functionality of blogger profile links.

### Preconditions:
- The blogger list page is loaded.

### Test Steps:

1. Click on the profile link of each blogger.

**Expected Results:**
- Clicking on a blogger's profile link should navigate to their respective profile page.

### Postconditions:
- Blogger profile links should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Post Preview Links

**Test Description:** This test case checks the functionality of post preview links on the blogger list page.

### Preconditions:
- The blogger list page is loaded.

### Test Steps:

1. Click on the post preview links for each blogger's recent posts.

**Expected Results:**
- Clicking on a post preview link should navigate to the respective blog post's detail page.

### Postconditions:
- Post preview links should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for author_detail.html Template

## Test Case ID: TC001

### Test Case Title: Author Profile Page Rendering

**Test Description:** This test case ensures that the author profile page template renders correctly, displaying the author's profile information, message form, and recent posts.

### Preconditions:
- The Django application is up and running.
- There is an author profile available in the database with associated recent blog posts.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the author profile page, e.g., [author_detail.html](https://final-project-ada-02b27917ae0c.herokuapp.com/authors/1/), where `author_id` is the ID of the author.

**Expected Results:**
- The author profile page should load without errors.
- The page should display the following elements accurately:
  - Author's profile picture (or default image if not available).
  - Author's username and email address.
  - Last login date and time.
  - A message form with fields for sending a message to the author.
  - Recent posts by the author, including post images (if available), titles, creation dates, and "Read More" links.

### Postconditions:
- The author profile page should display all elements accurately.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Message Form Submission

**Test Description:** This test case checks the functionality of the message form on the author profile page.

### Preconditions:
- The author profile page is loaded.

### Test Steps:

1. Fill in the message form with valid data.
2. Click the "Send Message" button.

**Expected Results:**
- The form should accept valid input data without errors.
- After clicking the "Send Message" button, the message should be sent successfully, and a confirmation message should be displayed.

### Postconditions:
- The message form should work correctly, and the message should be sent to the author.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Recent Post Links

**Test Description:** This test case checks the functionality of the "Read More" links for recent posts on the author profile page.

### Preconditions:
- The author profile page is loaded.

### Test Steps:

1. Click on the "Read More" links for each recent post.

**Expected Results:**
- Clicking on a "Read More" link should navigate to the respective blog post's detail page.

### Postconditions:
- "Read More" links for recent posts should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for message_to_author.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the `message_to_author.html` template renders correctly and displays all required elements.

### Preconditions:
- The Django web application is running.
- The template is loaded within the web application.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the [message_to_author.html](https://final-project-ada-02b27917ae0c.herokuapp.com/message-author/1/) template is used.

**Expected Results:**
- The template should render without errors.
- The template should display the following elements accurately:
  - Heading displaying "Write a message to author: [Author's Name]"
  - A message form with fields for Sender Name, Sender Email, and Message.
  - A "Send Message" button.

### Postconditions:
- The template should render correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Message Submission

**Test Description:** This test case verifies the functionality of submitting a message using the template.

### Preconditions:
- The template is loaded.

### Test Steps:

1. Fill in the Sender Name, Sender Email, and Message fields in the message form.

2. Click the "Send Message" button to submit the form.

**Expected Results:**
- The form should accept valid input data without errors.

- After clicking the "Send Message" button, a success message or confirmation should be displayed, indicating that the message was sent successfully.

### Postconditions:
- The message submission functionality should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Form Validation

**Test Description:** This test case checks the validation of form fields in the template.

### Preconditions:
- The template is loaded.

### Test Steps:

1. Submit the message form with one or more of the form fields left empty.

**Expected Results:**
- Validation error messages should appear next to the empty fields, indicating that the fields are required.

### Postconditions:
- Form field validation should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Valid Email Address

**Test Description:** This test case checks the validation of the Sender Email field in the template.

### Preconditions:
- The template is loaded.

### Test Steps:

1. Enter an invalid email address format (e.g., "invalidemail") in the Sender Email field.

2. Click the "Send Message" button to submit the form.

**Expected Results:**
- A validation error message should appear next to the Sender Email field, indicating that a valid email address is required.

### Postconditions:
- Validation for the Sender Email field should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Maximum Character Limit

**Test Description:** This test case checks the maximum character limit for the Message field in the template.

### Preconditions:
- The template is loaded.

### Test Steps:

1. Enter a message that exceeds the maximum character limit in the Message field.

2. Click the "Send Message" button to submit the form.

**Expected Results:**
- A validation error message should appear next to the Message field, indicating that the message should not exceed the maximum character limit.

### Postconditions:
- Validation for the Message field should work correctly.

### Test Status:
- [ ] Pass
- [ ] Fail


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for request_author_access.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the author access request page template renders correctly and displays all required elements.

### Preconditions:
- The Django web application is running.
- The template is loaded within the web application.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the author access request page template is used [request_author_access.html](https://final-project-ada-02b27917ae0c.herokuapp.com/request-author-access/).

**Expected Results:**
- The author access request page template should render without errors.
- The template should display the following elements accurately:
  - Page Heading with the text "Request Author Access."
  - A description paragraph explaining how to request author access.
  - A form for submitting an author access request, including fields for the required information.
  - A "Submit Request" button.

### Postconditions:
- The author access request page template should render correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Form Submission

**Test Description:** This test case verifies the functionality of submitting an author access request using the author access request page template.

### Preconditions:
- The author access request page template is loaded.

### Test Steps:

1. Fill in the form fields with valid data.

2. Click the "Submit Request" button to submit the form.

**Expected Results:**
- The form should accept valid input data without errors.

- After clicking the "Submit Request" button, a success message or confirmation should be displayed, indicating that the author access request was submitted successfully.

### Postconditions:
- The form submission functionality should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Form Validation

**Test Description:** This test case checks the validation of form fields in the author access request page template.

### Preconditions:
- The author access request page template is loaded.

### Test Steps:

1. Submit the form with one or more of the form fields left empty.

**Expected Results:**
- Validation error messages should appear next to the empty fields, indicating that the fields are required.

### Postconditions:
- Form field validation should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---


<hr>
---------------------------------------------------------------------------------------------------------

# Manual Testing for Django 404.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the 404 error page template renders correctly and displays the appropriate error message.

### Preconditions:
- The Django web application is running.
- The 404 error page template is used to handle page not found errors [404.html](https://final-project-ada-02b27917ae0c.herokuapp.com/404).

### Test Steps:

1. Open a web browser.

2. Enter a non-existing URL or navigate to a page that does not exist within the web application.

**Expected Results:**
- The 404 error page should load without errors.
- The page should display the following elements accurately:
  - A large "404" text indicating the error.
  - An error message informing the user that the page they are looking for is not available.
  - A "Go to Home" link that allows the user to navigate back to the home page.

### Postconditions:
- The 404 error page template should render correctly for page not found errors.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: "Go to Home" Link

**Test Description:** This test case checks the functionality of the "Go to Home" link on the 404 error page.

### Preconditions:
- The 404 error page is loaded.

### Test Steps:

1. Click on the "Go to Home" link.

**Expected Results:**
- Clicking on the "Go to Home" link should navigate the user to the home page of the web application.

### Postconditions:
- The "Go to Home" link on the 404 error page should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Page Title and Favicon

**Test Description:** This test case checks the presence of the page title and favicon in the 404 error page.

### Preconditions:
- The 404 error page is loaded.

### Test Steps:

1. Verify the presence of the page title and favicon.

**Expected Results:**
- The page title should be "Page Not Found."
- The favicon of an owl should be displayed in the browser tab.

### Postconditions:
- The page title and favicon in the 404 error page should be as expected.

### Test Status:
- [X] Pass
- [ ] Fail



<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for blog_post_card.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the post card template renders correctly and displays the post's content, author, title, excerpt, and metadata.

### Preconditions:
- The Django web application is running.
- The post card template is used to display blog posts.

### Test Steps:

1. Open a web browser.

2. Navigate to a page that displays a blog post using the post card template.

**Expected Results:**
- The post card template should load without errors.
- The page should display the following elements accurately:
  - An image, if available, using Cloudinary with a responsive class.
  - The post author's name with a link to their profile.
  - The post title truncated to 7 words.
  - A brief excerpt from the post.
  - A "Read more →" link to view the full post.
  - Post metadata including the creation date, a like button (filled or empty), the number of likes, and a link to view comments with the comment count.

### Postconditions:
- The post card template should render correctly for displaying blog posts.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Like Button Functionality

**Test Description:** This test case checks the functionality of the like button on the post card template.

### Preconditions:
- The post card template is loaded with a post.

### Test Steps:

1. Click on the like button.

**Expected Results:**
- Clicking on the like button should toggle the heart icon between filled (liked) and empty (unliked).
- The number of likes should increment or decrement accordingly.

### Postconditions:
- The like button on the post card template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Comment Link and Count

**Test Description:** This test case checks the functionality of the comment link and comment count on the post card template.

### Preconditions:
- The post card template is loaded with a post.

### Test Steps:

1. Click on the comment link.

**Expected Results:**
- Clicking on the comment link should navigate the user to the full post page.
- The comment count should be displayed next to the comment icon.

### Postconditions:
- The comment link and comment count on the post card template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for comment_delete.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the Confirm Delete Comment page template renders correctly, displaying the confirmation message, and the "Delete" and "Back to Feed" buttons.

### Preconditions:
- The Django web application is running.
- The Confirm Delete Comment page template is loaded with a comment deletion confirmation message.

### Test Steps:

1. Open a web browser.

2. Navigate to a page that displays the Confirm Delete Comment page using the template.

**Expected Results:**
- The Confirm Delete Comment page template should load without errors.
- The page should display the following elements accurately:
  - A confirmation message informing the user about the deletion action.
  - Two buttons, "Delete" and "Back to Feed," with proper styling.

### Postconditions:
- The Confirm Delete Comment page template should render correctly for confirming comment deletion.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Delete Button Functionality

**Test Description:** This test case checks the functionality of the "Delete" button on the Confirm Delete Comment page.

### Preconditions:
- The Confirm Delete Comment page template is loaded.

### Test Steps:

1. Click on the "Delete" button.

**Expected Results:**
- Clicking on the "Delete" button should submit a POST request to delete the comment.
- The comment should be deleted, and the user should be redirected to the appropriate page.

### Postconditions:
- The "Delete" button on the Confirm Delete Comment page template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Back to Feed Button Functionality

**Test Description:** This test case checks the functionality of the "Back to Feed" button on the Confirm Delete Comment page.

### Preconditions:
- The Confirm Delete Comment page template is loaded.

### Test Steps:

1. Click on the "Back to Feed" button.

**Expected Results:**
- Clicking on the "Back to Feed" button should navigate the user back to the feed or homepage of the application.

### Postconditions:
- The "Back to Feed" button on the Confirm Delete Comment page template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------


# Manual Testing for comment_update.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the Comment Update Page template renders correctly, displaying the form for updating a comment and the "Save" button.

### Preconditions:
- The Django web application is running.
- The Comment Update Page template is loaded with a comment update form.

### Test Steps:

1. Open a web browser.

2. Navigate to a page that displays the Comment Update Page using the template.

**Expected Results:**
- The Comment Update Page template should load without errors.
- The page should display the following elements accurately:
  - A heading that says "Update your comment."
  - A form for updating a comment with appropriate form fields.
  - A "Save" button for saving the updated comment.

### Postconditions:
- The Comment Update Page template should render correctly for updating comments.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Comment Update Form Functionality

**Test Description:** This test case checks the functionality of the comment update form on the Comment Update Page.

### Preconditions:
- The Comment Update Page template is loaded.

### Test Steps:

1. Fill in the comment update form with valid data.

2. Click the "Save" button.

**Expected Results:**
- The form should accept valid input data without errors.

- After clicking the "Save" button, the updated comment should be saved successfully, and the user should be redirected to the appropriate page.

### Postconditions:
- The comment update form on the Comment Update Page template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail



<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for draft_post_author.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the Draft Posts Page template renders correctly, displaying the username, draft posts, and pagination controls (if applicable).

### Preconditions:
- The Django web application is running.
- The Draft Posts Page template is loaded with draft posts and pagination controls (if there are multiple pages of draft posts).

### Test Steps:

1. Open a web browser.

2. Navigate to a page that displays the Draft Posts Page using the template.

**Expected Results:**
- The Draft Posts Page template should load without errors.
- The page should display the following elements accurately:
  - A heading that says "Draft Posts by [username]" where [username] is the username whose draft posts are being shown.
  - A list of draft posts, each displayed in a card format.
  - Pagination controls (if there are multiple pages of draft posts) for navigating between pages.
  - If there are no draft posts, an alert message should be displayed indicating there are no draft posts to show.

### Postconditions:
- The Draft Posts Page template should render correctly for displaying draft posts.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Pagination Controls Functionality

**Test Description:** This test case checks the functionality of the pagination controls on the Draft Posts Page.

### Preconditions:
- The Draft Posts Page template is loaded with multiple pages of draft posts.

### Test Steps:

1. Click on the "next" link in the pagination controls to go to the next page of draft posts (if available).

2. Click on the "previous" link in the pagination controls to go to the previous page of draft posts (if available).

3. Click on the "last" link in the pagination controls to go to the last page of draft posts (if available).

4. Click on the "first" link in the pagination controls to go to the first page of draft posts (if available).

**Expected Results:**
- Clicking on the pagination controls should navigate to the corresponding page of draft posts.
- The pagination controls should accurately display the current page number and the total number of pages.
- If there are no previous or next pages, the respective "previous" and "next" links should be disabled.

### Postconditions:
- The pagination controls on the Draft Posts Page template should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for post_delete.html Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the Post Deletion Page template renders correctly, displaying the confirmation message for deleting a post and the "Delete" and "Cancel" buttons.

### Preconditions:
- The Django web application is running.
- The Post Deletion Page template is loaded with a confirmation message for deleting a specific post.

### Test Steps:

1. Open a web browser.

2. Navigate to a page that displays the Post Deletion Page using the template.

**Expected Results:**
- The Post Deletion Page template should load without errors.
- The page should display the following elements accurately:
  - A heading that says "Delete post."
  - A confirmation message that says "Are you sure that you want to delete the post '[post title]'?" where '[post title]' is the title of the post to be deleted.
  - A "Delete" button for confirming the deletion.
  - A "Cancel" button for canceling the deletion and returning to the post detail page.

### Postconditions:
- The Post Deletion Page template should render correctly for post deletion confirmation.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Post Deletion Confirmation

**Test Description:** This test case checks the functionality of the "Delete" and "Cancel" buttons on the Post Deletion Page.

### Preconditions:
- The Post Deletion Page template is loaded with a confirmation message for deleting a specific post.

### Test Steps:

1. Click on the "Delete" button to confirm the deletion of the post.

2. Click on the "Cancel" button to cancel the deletion and return to the post detail page.

**Expected Results:**
- Clicking on the "Delete" button should confirm the deletion of the post, and the post should be deleted from the database.
- Clicking on the "Cancel" button should cancel the deletion and return the user to the post detail page.

### Postconditions:
- The "Delete" and "Cancel" buttons on the Post Deletion Page should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail



<hr>
--------------------------------------------------------------------------------------------------------


# Manual Testing for post_detail.html Template

## Test Case ID: TC001

### Test Case Title: Display Post Details

**Test Description:** This test case ensures that the post detail page template displays all relevant post details, including the post image, title, author, content, likes, comments, and social sharing buttons.

### Preconditions:
- A blog post exists in the database with associated comments.
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of a specific post detail page, e.g., [post_Detail.html](https://final-project-ada-02b27917ae0c.herokuapp.com/post/jumpstart-your-python-journey/), where `post_slug` is the slug of the post.

**Expected Results:**
- The post detail page should load without errors.
- The following post details should be displayed correctly:
  - Post image (if available) or a placeholder image.
  - Post title.
  - Author's name with a link to their profile.
  - Post creation date.
  - Post content.
  - Number of likes for the post.
  - Like button (for authenticated users).
  - Total number of comments.
  - Comments section with author names, creation dates, and content.
  - Comment like buttons (for approved comments).
  - Social sharing buttons for WhatsApp, Twitter, Facebook, and LinkedIn.

### Postconditions:
- The post detail page should display all post details accurately.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Post Author Actions

**Test Description:** This test case checks the functionality of actions available to the post author (e.g., edit, publish, delete).

### Preconditions:
- The post detail page is loaded, and the current user is the post author.

### Test Steps:

1. Verify that the "Edit" button is displayed.

2. Click on the "Edit" button.

**Expected Results:**
- The user should be redirected to the post editing page.

3. Verify that the "Publish" button is displayed (if the post is not published).

4. Click on the "Publish" button.

**Expected Results:**
- The post should be published, and the "Publish" button should disappear.

5. Verify that the "Delete" button is displayed.

6. Click on the "Delete" button.

**Expected Results:**
- A confirmation message for post deletion should appear.
- After confirmation, the post should be deleted, and the user should be redirected to the home page.

### Postconditions:
- Post author actions (edit, publish, delete) should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Commenting on a Post

**Test Description:** This test case checks the functionality of commenting on a post.

### Preconditions:
- The post detail page is loaded, and the user is authenticated.

### Test Steps:

1. Verify that a comment form is displayed.

2. Enter a comment in the comment form.

3. Click the "Submit" button.

**Expected Results:**
- The comment should be successfully added to the post.
- The comment should appear in the comments section.

### Postconditions:
- Users should be able to add comments to the post.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Liking a Post

**Test Description:** This test case checks the functionality of liking a post.

### Preconditions:
- The post detail page is loaded, and the user is authenticated.

### Test Steps:

1. Verify that the "Like" button is displayed.

2. Click the "Like" button.

**Expected Results:**
- The post should be liked, and the "Like" button should change its appearance (e.g., filled heart icon).

### Postconditions:
- Users should be able to like a post.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Social Sharing

**Test Description:** This test case checks the functionality of social sharing buttons.

### Preconditions:
- The post detail page is loaded.

### Test Steps:

1. Verify that social sharing buttons for WhatsApp, Twitter, Facebook, and LinkedIn are displayed.

2. Click on each social sharing button.

**Expected Results:**
- Clicking on a social sharing button should open a new window or dialog for sharing the post on the respective social media platform.

### Postconditions:
- Social sharing buttons should allow users to share the post on social media.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for post_form.html Template

## Test Case ID: TC001

### Test Case Title: Display Create Post Form

**Test Description:** This test case verifies that the Create Post form is displayed correctly when creating a new post.

### Preconditions:
- The Django application is up and running.
- The user is logged in (authenticated).

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Create Post form is located, e.g., [post_form.html](https://final-project-ada-02b27917ae0c.herokuapp.com/post/create/).

**Expected Results:**
- The Create Post form should load without errors.
- The following form fields should be displayed correctly:
  - Post title input field.
  - Post content textarea field.
  - Image upload field.
  - Post status selection (if not updating).
  - Post categories selection (if not updating).
  - Post tags selection (if not updating).
  - "Create a post" button.

### Postconditions:
- The Create Post form should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Display Update Post Form

**Test Description:** This test case verifies that the Update Post form is displayed correctly when updating an existing post.

### Preconditions:
- The Django application is up and running.
- The user is logged in (authenticated).
- An existing post is available for updating.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Update Post form is located, where `post_slug` is the slug of the post to update.

**Expected Results:**
- The Update Post form should load without errors.
- The following form fields should be displayed correctly:
  - Post title input field filled with the existing title.
  - Post content textarea field filled with the existing content.
  - Image upload field.
  - "Update the post" button.

### Postconditions:
- The Update Post form should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Create a New Post

**Test Description:** This test case checks the functionality of creating a new post using the Create Post form.

### Preconditions:
- The Create Post form is displayed.
- The user is logged in (authenticated).

### Test Steps:

1. Fill in the required fields: Title, Content, and optionally, select a status, categories, and tags.

2. Click the "Create a post" button.

**Expected Results:**
- The new post should be created and saved in the database.
- The user should be redirected to the newly created post's detail page.

### Postconditions:
- A new post should be created successfully.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Update an Existing Post

**Test Description:** This test case checks the functionality of updating an existing post using the Update Post form.

### Preconditions:
- The Update Post form is displayed.
- The user is logged in (authenticated).
- An existing post is available for updating.

### Test Steps:

1. Modify the content of the Title and/or Content fields.

2. Click the "Update the post" button.

**Expected Results:**
- The existing post should be updated with the new content.
- The user should be redirected to the updated post's detail page.

### Postconditions:
- The existing post should be updated successfully.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

