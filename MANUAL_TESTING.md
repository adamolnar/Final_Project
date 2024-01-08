# Manual Testing for Base Template

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


# Manual Testing for Blog Landing Page Template

## Test Case ID: TC001

### Test Case Title: Blog Page Rendering

**Test Description:** This test case ensures that the blog page template renders correctly, displaying blog posts, tags, categories, and additional content.

### Preconditions:
- The Django application is up and running.
- Sample blog posts, tags, and categories are available in the database.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the blog page, e.g., [Home](https://final-project-ada-02b27917ae0c.herokuapp.com/).

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
- [X] Pass
- [ ] Fail

<hr>
----------------------------------------------------------------------------------------------------------

# Manual Testing for Byte by Byte Tech Page Template

## Test Case ID: TC001

### Test Case Title: Byte by Byte Page Content

**Test Description:** This test case ensures that the  page of the Byte by Byte Tech Blog displays the expected content accurately.

### Preconditions:
- The Django application is up and running.
- The user is accessing the  page.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the  page, e.g., [Byte by Byte](https://final-project-ada-02b27917ae0c.herokuapp.com/blog/byte_by_byte/).

**Expected Results:**
- The page should load without errors.
- The page should display the following content accurately:
  - A title: "Explore Byte by Byte Tech Blog"
  - A description welcoming users to the blog.
  - Information about what readers will find on the blog, including expert articles, tutorials, tech news, and community engagement.
  - A section explaining why to choose Byte by Byte, highlighting quality content, an education-first approach, interactive experience, and regular updates.
  - A call to action inviting users to explore the blog.
  
### Postconditions:
- The  page content should be displayed accurately.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Responsive Design

**Test Description:** This test case verifies the responsiveness of the page template on different screen sizes.

### Preconditions:
- The page is loaded.

### Test Steps:

1. Resize the web browser to various screen sizes, including desktop, tablet, and mobile dimensions.

**Expected Results:**
- The page should adapt to different screen sizes, maintaining readability and usability.
- Text and images should adjust accordingly to provide a good user experience.

### Postconditions:
- The page should be responsive on various devices.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for Blog Post Page Template

## Test Case ID: TC001

### Test Case Title: Blog Post Page Rendering

**Test Description:** This test case ensures that the blog post page template renders correctly, displaying the blog post's content, author, comments, and social sharing buttons.

### Preconditions:
- The Django application is up and running.
- A sample blog post with comments and social sharing options is available in the database.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of a specific blog post, e.g., [Blog Post](https://final-project-ada-02b27917ae0c.herokuapp.com/).

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
- [X] Pass
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
- [X] Pass
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
--------------------------------------------------------------------------------------------------------


# Manual Testing for Blogger List Page Template

## Test Case ID: TC001

### Test Case Title: Blogger List Page Rendering

**Test Description:** This test case ensures that the blogger list page template renders correctly, displaying a list of bloggers, their profiles, and recent posts.

### Preconditions:
- The Django application is up and running.
- There are blogger profiles available in the database, with associated recent blog posts.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the blogger list page, e.g., [Bloggers](https://final-project-ada-02b27917ae0c.herokuapp.com/authors/).

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
- [X] Pass
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
- [X] Pass
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


# Manual Testing for Author Profile Page Template

## Test Case ID: TC001

### Test Case Title: Author Profile Page Rendering

**Test Description:** This test case ensures that the author profile page template renders correctly, displaying the author's profile information, message form, and recent posts.

### Preconditions:
- The Django application is up and running.
- There is an author profile available in the database with associated recent blog posts.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of the author profile page, e.g., [Author Profile](https://final-project-ada-02b27917ae0c.herokuapp.com/authors/1/), where `author_id` is the ID of the author.

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


# Manual Testing for Send Message to Author Page Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the template renders correctly and displays all required elements.

### Preconditions:
- The Django web application is running.
- The template is loaded within the web application.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the [Send Message](https://final-project-ada-02b27917ae0c.herokuapp.com/authors/1/) template is used.

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
- [X] Pass
- [ ] Fail


<hr>
---------------------------------------------------------------------------------------------------------


# Manual Testing for Author Access Request Page Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the author access request page template renders correctly and displays all required elements.

### Preconditions:
- The Django web application is running.
- The template is loaded within the web application.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the author access request page template is used [Author Access Request](https://final-project-ada-02b27917ae0c.herokuapp.com/request-author-access/).

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

# Manual Testing for 404 Error Page Template

## Test Case ID: TC001

### Test Case Title: Template Rendering

**Test Description:** This test case ensures that the 404 error page template renders correctly and displays the appropriate error message.

### Preconditions:
- The Django web application is running.
- The 404 error page template is used to handle page not found errors [404 Error Page](https://final-project-ada-02b27917ae0c.herokuapp.com/404).

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

# Manual Testing for Post Card Template

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

# Manual Testing for Confirm Delete Comment Page Template

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


# Manual Testing for Comment Update Page Template

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

# Manual Testing for Draft Posts Page Template

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

# Manual Testing for Post Deletion Page Template

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


# Manual Testing for Post Detail Page Template

## Test Case ID: TC001

### Test Case Title: Display Post Details

**Test Description:** This test case ensures that the post detail page template displays all relevant post details, including the post image, title, author, content, likes, comments, and social sharing buttons.

### Preconditions:
- A blog post exists in the database with associated comments.
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL of a specific post detail page, e.g., [Read more](https://final-project-ada-02b27917ae0c.herokuapp.com/post/jumpstart-your-python-journey/), where `post_slug` is the slug of the post.

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
- Registered users should be able to add comments to the post.

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
- Registered users should be able to like a post.

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

# Manual Testing for Create or Update Post Template

## Test Case ID: TC001

### Test Case Title: Display Create Post Form

**Test Description:** This test case verifies that the Create Post form is displayed correctly when creating a new post.

### Preconditions:
- The Django application is up and running.
- The user is logged in (authenticated).

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Create Post form is located, e.g., [Create Post](https://final-project-ada-02b27917ae0c.herokuapp.com/post/create/).

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

# Manual Testing for Displaying Posts with Specific Tag Page Template

## Test Case ID: TC001

### Test Case Title: Correct Rendering of Posts with Tag

**Test Description:** 
This test case ensures that the custom template correctly renders posts associated with a specific tag, while integrating seamlessly with the `tag_detail.html` template.

### Preconditions:
- The Django web application is running.
- The `tag_detail.html` template is correctly integrated and functional.
- There are posts in the database associated with specific tags.

### Test Steps:

1. **Open a Web Browser:**
   - Launch a web browser of your choice.

2. **Navigate to the Page Displaying Tag-Specific Posts:**
   - Go to the section or page of the web application where posts associated with tags are displayed.

3. **Inspect Elements and Content:**
   - Verify that the `<h3>` element correctly displays the tag name.
   - Ensure that for each `post` in `associated_posts`, a `blog/blog_post_card.html` is included and rendered.

### Expected Results:
- The page should render without errors.
- The tag name should be displayed within the `<h3>` element.
- Each associated post should be correctly displayed using the `blog_post_card.html` template.
- Elements such as the navigation bar, authentication status, flash messages, and footer from `base.html` should be consistently present and functional.

### Postconditions:
- The page should maintain its layout and functionality after the test.

### Test Status:
- [X] Pass
- [ ] Fail

<hr>----------------------------------------------------------------------------------------------------

# Manual Testing for Login Page Template

## Test Case ID: TC001

### Test Case Title: Display Login Form

**Test Description:** This test case verifies that the Login form is displayed correctly.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Login page is located, e.g., [Login](https://final-project-ada-02b27917ae0c.herokuapp.com/accounts/login/).

**Expected Results:**
- The Login form should load without errors.
- The following form fields should be displayed correctly:
  - Username or Email input field.
  - Password input field.
  - "Submit" button.
- The heading "Log In" should be displayed.
- The "Welcome back to the blog. If you don't have an account please Register instead." message should be displayed with a link to registration.

### Postconditions:
- The Login form should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Login with Valid Credentials

**Test Description:** This test case checks the functionality of logging in with valid credentials.

### Preconditions:
- The Login form is displayed.
- A user account with valid login credentials exists in the system.

### Test Steps:

1. Enter valid credentials (username/email and password) in the respective fields.

2. Click the "Submit" button.

**Expected Results:**
- The user should be successfully logged in.
- The user should be redirected to the intended page (e.g., the dashboard).
- The user's session should be active.

### Postconditions:
- The user should be logged in successfully.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Login with Invalid Credentials

**Test Description:** This test case checks the behavior of the login form when incorrect credentials are provided.

### Preconditions:
- The Login form is displayed.

### Test Steps:

1. Enter invalid credentials (e.g., incorrect username/email or password) in the respective fields.

2. Click the "Submit" button.

**Expected Results:**
- The login attempt should fail.
- An error message should be displayed indicating that the login failed.
- The user should not be redirected to the intended page.
- The user's session should remain inactive.

### Postconditions:
- The login attempt should fail as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Registration Link

**Test Description:** This test case checks if the registration link is working correctly.

### Preconditions:
- The Login form is displayed.

### Test Steps:

1. Click on the "Register" link provided in the login form.

**Expected Results:**
- The user should be redirected to the registration page.
- The registration page should load correctly.

### Postconditions:
- The user should be able to navigate to the registration page.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for Sign Out (Logout) Template

## Test Case ID: TC001

### Test Case Title: Display Sign Out Confirmation

**Test Description:** This test case verifies that the Sign Out confirmation message is displayed correctly.

### Preconditions:
- The Django application is up and running.
- The user is currently authenticated and logged in.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Sign Out (Logout) page is located, e.g., [Logout](https://final-project-ada-02b27917ae0c.herokuapp.com/accounts/logout/).

**Expected Results:**
- The Sign Out confirmation message should load without errors.
- The heading "Sign Out" should be displayed.
- The confirmation message "Are you sure you want to Sign Out?" should be displayed with translation support.

### Postconditions:
- The Sign Out confirmation message should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Perform Sign Out (Logout)

**Test Description:** This test case checks the functionality of performing the Sign Out (Logout) operation.

### Preconditions:
- The Sign Out confirmation message is displayed.
- The user is currently authenticated and logged in.

### Test Steps:

1. Click the "Sign Out" button.

**Expected Results:**
- The user should be successfully logged out (signed out).
- The user's session should be terminated.
- The user should be redirected to the application's homepage or a relevant page.

### Postconditions:
- The user should be logged out successfully.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Redirect After Sign Out

**Test Description:** This test case checks if the user is redirected to the correct page after signing out.

### Preconditions:
- The Sign Out confirmation message is displayed.
- The user is currently authenticated and logged in.

### Test Steps:

1. Click the "Sign Out" button.

**Expected Results:**
- The user should be successfully logged out.
- The user should be redirected to the application's homepage or a relevant page specified after sign-out.

### Postconditions:
- The user should be logged out, and the redirection should be as expected.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for Sign-Up (Registration) Page Template

## Test Case ID: TC001

### Test Case Title: Display Sign-Up Form

**Test Description:** This test case verifies that the Sign-Up (Registration) form is displayed correctly with the required fields.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Sign-Up (Registration) page is located, e.g., [Register](https://final-project-ada-02b27917ae0c.herokuapp.com/accounts/signup/).

**Expected Results:**
- The Sign-Up (Registration) form should load without errors.
- The "Create your account" heading should be displayed with translation support.
- The form should include fields for:
  - Username
  - Email
  - Password
  - Confirm Password
- Each field should have appropriate labels, placeholders, and error handling for validation.

### Postconditions:
- The Sign-Up (Registration) form should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Submit Sign-Up Form

**Test Description:** This test case checks the functionality of submitting the Sign-Up (Registration) form.

### Preconditions:
- The Sign-Up (Registration) form is displayed.

### Test Steps:

1. Fill in the Sign-Up (Registration) form with valid data:
   - Username
   - Email
   - Password
   - Confirm Password

2. Click the "Submit" button.

**Expected Results:**
- The form should be submitted without errors.
- The user's registration should be successful.
- The user should be redirected to the application's homepage or a relevant page.

### Postconditions:
- The user should be registered successfully.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Sign-Up Form Validation

**Test Description:** This test case checks the validation of the Sign-Up (Registration) form.

### Preconditions:
- The Sign-Up (Registration) form is displayed.

### Test Steps:

1. Fill in the Sign-Up (Registration) form with invalid data:
   - Invalid email format
   - Password and Confirm Password do not match

2. Click the "Submit" button.

**Expected Results:**
- The form submission should be rejected due to validation errors.
- Validation error messages should be displayed for the respective fields with translation support.
- The user should not be registered with invalid data.

### Postconditions:
- The Sign-Up (Registration) form should display validation errors.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Sign-Up Form Redirection

**Test Description:** This test case checks if the user is redirected to the correct page after successful registration.

### Preconditions:
- The user has successfully registered.

### Test Steps:

1. After successful registration, check if the user is redirected to the application's homepage or a relevant page.

**Expected Results:**
- The user should be redirected to the home page after successful registration.

### Postconditions:
- The user should be redirected as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Existing Account Redirect to Log In

**Test Description:** This test case checks if an existing user is redirected to the Log In page instead of registering a new account.

### Preconditions:
- An existing user is already registered.

### Test Steps:

1. Access the Sign-Up (Registration) page.

**Expected Results:**
- The user should see a message indicating they already have an account and a link to the Log In page.
- Clicking on the Log In link should redirect to the Log In page.

### Postconditions:
- The user should be informed that they already have an account.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for Contact Us Page Template

## Test Case ID: TC001

### Test Case Title: Display Contact Us Form

**Test Description:** This test case verifies that the Contact Us form is displayed correctly with the required fields.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Contact Us page is located, e.g., [Contact Us](https://final-project-ada-02b27917ae0c.herokuapp.com/contact/).

**Expected Results:**
- The Contact Us form should load without errors.
- The "Contact Us" heading should be displayed.
- The form should include fields for:
  - Name
  - Email
  - Message
- Each field should have appropriate labels and placeholders.

### Postconditions:
- The Contact Us form should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Submit Contact Us Form

**Test Description:** This test case checks the functionality of submitting the Contact Us form.

### Preconditions:
- The Contact Us form is displayed.

### Test Steps:

1. Fill in the Contact Us form with valid data:
   - Name
   - Email
   - Message

2. Click the "Submit" button.

**Expected Results:**
- The form should be submitted without errors.
- The submitted information should be sent as a contact message.
- A success message should be displayed indicating that the message was sent successfully.

### Postconditions:
- The message should be sent successfully.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Contact Us Form Validation

**Test Description:** This test case checks the validation of the Contact Us form.

### Preconditions:
- The Contact Us form is displayed.

### Test Steps:

1. Fill in the Contact Us form with invalid data:
   - Invalid email format
   - Empty fields (Name, Email, Message)

2. Click the "Submit" button.

**Expected Results:**
- The form submission should be rejected due to validation errors.
- Validation error messages should be displayed for the respective fields.
- The user should not be able to submit an empty form or an invalid email.

### Postconditions:
- The Contact Us form should display validation errors.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Display Form Submission Success Message

**Test Description:** This test case checks if a success message is displayed after successfully submitting the Contact Us form.

### Preconditions:
- The Contact Us form is displayed.

### Test Steps:

1. Fill in the Contact Us form with valid data:
   - Name
   - Email
   - Message

2. Click the "Submit" button.

3. Check if a success message is displayed.

**Expected Results:**
- A success message should be displayed indicating that the message was sent successfully.

### Postconditions:
- A success message should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Form Error Handling

**Test Description:** This test case checks if the Contact Us form correctly handles form submission errors.

### Preconditions:
- The Contact Us form is displayed.

### Test Steps:

1. Submit the Contact Us form without filling in any fields or with invalid data.

2. Check if form submission errors are displayed.

**Expected Results:**
- Form submission should be rejected due to errors.
- Appropriate error messages should be displayed for the respective fields.

### Postconditions:
- Form submission errors should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>

--------------------------------------------------------------------------------------------------------

# Manual Testing for "Not a published Author" Page Template

## Test Case ID: TC001

### Test Case Title: Display "Not a published Author" Page

**Test Description:** This test case verifies that the "Not a published Author" page is displayed correctly.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the New Author with unpublished posts page is located, e.g., []().

**Expected Results:**
- The "Not a published Author" page should load without errors.
- The page content should include information about the user not being an author.

### Postconditions:
- The "Not a published Author" page should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Verify User Information Display

**Test Description:** This test case checks whether the user's information is correctly displayed on the "Not a published Author" page.

### Preconditions:
- The "Not a published Author" page is displayed.

### Test Steps:

1. Check if the user's username is displayed.

2. Check if the user's email address is displayed.

**Expected Results:**
- The user's username and email should be displayed on the page.

### Postconditions:
- The user's information should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---


## Test Case ID: TC003

### Test Case Title: Verify Last Login Information

**Test Description:** This test case checks whether the user's last login information is displayed on the "Not an Author" page.

### Preconditions:
- The "Not a published Author" page is displayed.

### Test Steps:

1. Check if the user's last login information is displayed.

**Expected Results:**
- The user's last login information should be displayed on the page.

### Postconditions:
- The last login information should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
-------------------------------------------------------------------------------------------------------

# Manual Testing for Profile Deletion Confirmation Page Template

## Test Case ID: TC001

### Test Case Title: Display Profile Deletion Confirmation Page

**Test Description:** This test case verifies that the profile deletion confirmation page is displayed correctly.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Profile Deletion Confirmation page is located.

**Expected Results:**
- The Profile Deletion Confirmation page should load without errors.
- The page should display a confirmation message with the profile name.
- A form for confirming the deletion should be present.

### Postconditions:
- The Profile Deletion Confirmation page should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Verify Profile Name Display

**Test Description:** This test case checks whether the profile name is correctly displayed on the confirmation page.

### Preconditions:
- The Profile Deletion Confirmation page is displayed.

### Test Steps:

1. Check if the profile name is displayed within the confirmation message.

**Expected Results:**
- The profile name should be displayed accurately within the confirmation message.

### Postconditions:
- The profile name should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---


## Test Case ID: TC003

### Test Case Title: Verify Submit Button

**Test Description:** This test case checks whether the submit button for confirming the deletion is correctly displayed.

### Preconditions:
- The Profile Deletion Confirmation page is displayed.

### Test Steps:

1. Check if the submit button with the label "Confirm" is present within the confirmation form.

**Expected Results:**
- The submit button with the label "Confirm" should be present and clearly visible within the confirmation form.

### Postconditions:
- The presence and visibility of the submit button should be confirmed.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------


# Manual Testing for "Edit Profile" Page Template

## Test Case ID: TC001

### Test Case Title: Display "Edit Profile" Page

**Test Description:** This test case verifies that the "Edit Profile" page is displayed correctly.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the "Edit Profile" page is located.

**Expected Results:**
- The "Edit Profile" page should load without errors.
- The page should display the "Edit Profile" heading.

### Postconditions:
- The "Edit Profile" page should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Verify Username Field

**Test Description:** This test case checks whether the username field is displayed and functional on the "Edit Profile" page.

### Preconditions:
- The "Edit Profile" page is displayed.

### Test Steps:

1. Check if the username field is displayed.

2. Try entering a new username and verify if it is accepted.

**Expected Results:**
- The username field should be displayed.
- Entering a new username should be allowed.

### Postconditions:
- The username field should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Verify About Me Field

**Test Description:** This test case checks whether the "About Me" field is displayed and functional on the "Edit Profile" page.

### Preconditions:
- The "Edit Profile" page is displayed.

### Test Steps:

1. Check if the "About Me" field is displayed.

2. Try entering text into the "About Me" field and verify if it is accepted.

**Expected Results:**
- The "About Me" field should be displayed.
- Entering text into the "About Me" field should be allowed.

### Postconditions:
- The "About Me" field should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Verify Image Upload Field

**Test Description:** This test case checks whether the image upload field is displayed and functional on the "Edit Profile" page.

### Preconditions:
- The "Edit Profile" page is displayed.

### Test Steps:

1. Check if the image upload field is displayed.

2. Try uploading an image file and verify if it is accepted.

**Expected Results:**
- The image upload field should be displayed.
- Uploading an image file should be allowed.

### Postconditions:
- The image upload field should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Verify Submission

**Test Description:** This test case checks whether the submission of the "Edit Profile" form works correctly.

### Preconditions:
- The "Edit Profile" page is displayed.

### Test Steps:

1. Fill in the "Edit Profile" form with valid data (e.g., new username, "About Me" text, and an image).

2. Click the "Submit" button.

**Expected Results:**
- The form should be submitted without errors.
- The submitted information should be updated in the user's profile.

### Postconditions:
- The form submission should work correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC006

### Test Case Title: Verify Error Handling

**Test Description:** This test case checks whether the "Edit Profile" form correctly handles errors.

### Preconditions:
- The "Edit Profile" page is displayed.

### Test Steps:

1. Try submitting the "Edit Profile" form with invalid data (e.g., a duplicate username or an invalid image file).

2. Check if error messages are displayed for the respective fields.

**Expected Results:**
- Form submission should be rejected due to errors.
- Appropriate error messages should be displayed for the respective fields.

### Postconditions:
- Form submission errors should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for Profile Page Template

## Test Case ID: TC001

### Test Case Title: Display User Profile Page

**Test Description:** This test case verifies that the User Profile page is displayed correctly.

### Preconditions:
- The Django application is up and running.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the User Profile page is located.

**Expected Results:**
- The User Profile page should load without errors.
- The page should display the user's profile information, including:
  - User's name
  - User's email
  - User's last login date
  - Profile picture (if available)
  - Create Post
  - Draft post
  - Contact admin
  - "About" section
- Recent Posts should be displayed (if available).
- Buttons to edit and delete the profile (if authorized).
- A button to view draft posts (if authorized and draft posts exist).

### Postconditions:
- The User Profile page should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC002

### Test Case Title: Verify Edit Profile Button

**Test Description:** This test case checks whether the "Edit Profile" button is displayed and functional on the User Profile page.

### Preconditions:
- The User Profile page is displayed.

### Test Steps:

1. Check if the "Edit Profile" button is displayed.

2. Click the "Edit Profile" button (if authorized) and verify if it navigates to the Edit Profile page.

**Expected Results:**
- The "Edit Profile" button should be displayed (if authorized).
- Clicking the "Edit Profile" button should navigate to the Edit Profile page (if authorized).

### Postconditions:
- The "Edit Profile" button should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC003

### Test Case Title: Verify Delete Profile Button

**Test Description:** This test case checks whether the "Delete Profile" button is displayed and functional on the User Profile page.

### Preconditions:
- The User Profile page is displayed.

### Test Steps:

1. Check if the "Delete Profile" button is displayed.

2. Click the "Delete Profile" button (if authorized) and verify if it navigates to the Delete Profile confirmation page.

**Expected Results:**
- The "Delete Profile" button should be displayed (if authorized).
- Clicking the "Delete Profile" button should navigate to the Delete Profile confirmation page (if authorized).

### Postconditions:
- The "Delete Profile" button should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC004

### Test Case Title: Verify View Draft Posts Button

**Test Description:** This test case checks whether the "View Draft Posts" button is displayed and functional on the User Profile page.

### Preconditions:
- The User Profile page is displayed.

### Test Steps:

1. Check if the "View Draft Posts" button is displayed (if authorized and draft posts exist).

2. Click the "View Draft Posts" button (if authorized and draft posts exist) and verify if it navigates to the Draft Post Author List page.

**Expected Results:**
- The "View Draft Posts" button should be displayed (if authorized and draft posts exist).
- Clicking the "View Draft Posts" button should navigate to the Draft Post Author List page (if authorized and draft posts exist).

### Postconditions:
- The "View Draft Posts" button should function correctly.

### Test Status:
- [X] Pass
- [ ] Fail

---

## Test Case ID: TC005

### Test Case Title: Verify Recent Posts

**Test Description:** This test case checks whether the Recent Posts section is displayed correctly on the User Profile page.

### Preconditions:
- The User Profile page is displayed.

### Test Steps:

1. Check if the Recent Posts section is displayed.

2. Verify if it shows recent posts (if available) with titles, creation dates, content previews, and "Read More" links.

**Expected Results:**
- The Recent Posts section should be displayed.
- Recent posts (if available) should be shown with titles, creation dates, content previews, and "Read More" links.

### Postconditions:
- The Recent Posts section should display recent posts correctly.

### Test Status:
- [X] Pass
- [ ] Fail


<hr>
--------------------------------------------------------------------------------------------------------

# Manual Testing for Success Page Template

## Test Case ID: TC001

### Test Case Title: Display Success

**Test Description:** This test case verifies that the Contact Confirmation page is displayed correctly after submitting a contact form.

### Preconditions:
- The Django application is up and running.
- A contact form has been submitted successfully.

### Test Steps:

1. Open a web browser.

2. Navigate to the URL where the Contact Confirmation page is located, e.g., [ThankYou!](https://final-project-ada-02b27917ae0c.herokuapp.com/success/).

**Expected Results:**
- The Contact Confirmation page should load without errors.
- The page should display a "Thank you!" heading.
- A success message should be displayed, confirming that the contact information and message were successfully submitted.
- A "Back Home" button with a link should be displayed.

### Postconditions:
- The Contact Confirmation page should be displayed as expected.

### Test Status:
- [X] Pass
- [ ] Fail
