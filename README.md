# Project Title

<img src="static/images/" ><br>
<hr>

This is a simple Django Blog application that allows user to create, edit, and manage blog posts. It also includes user authentication and comment functionality. Bellow is guide through the setup and usage of this application.
<hr>


## Table of contents
  * [Overview](#overview)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope-hr-)
    + [Structure](#structure-hr-)
    + [Skeleton](#skeleton-hr-)
    + [Surface](#surface-hr-)
      - [Color Scheme & Fonts](#color-scheme-and-fonts)
      - [Visual Effects](#visual-effects)
  * [Agile Methodology](#agile-methodology)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Client bookints management](#client-bookings-management)
      - [Staff bookings management](#staff-bookings-management)
      - [Create bookings](#create-bookings)
      - [Menu](#menu)
      - [Information](#information)
    + [Potential Future Features](#pontential-future-features)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
    + [FORK THE REPOSITORY](#fork-the-repository)
    + [CLONE THE REPOSITORY](#clone-the-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)


## Overview
Django Blog is a robust and customizable blog application built using the Django web framework. It provides the foundation for creating and managing a fully functional blog website with ease. This overview provides a comprehensive understanding of the key features, benefits, and usage of Django Blog.

<br><br>
The deployed project can be accessed at [this link](....).
<br><br>

## UX


**User Stories:** <br>

<img src="static/images/" ><br>

**Project Goal:**<br>
The goal for the project is to create a website with good UX/UI in mind that is usefull to users, members and post authors. The website should convey an emotional response in the user.

**Project Objectives:**<br>
* To create a simple and intuitive website that with the help of UX conveys an positive emotional response in the user;
* To develop a user-friendly blog application that simplifies the process of creating, editing, and managing blog posts.
* Implement user authentication to allow authorized users, such as authors and administrators, to log in and access the admin panel for content management.
* Develop a robust system for creating, editing, and deleting blog posts, along with the ability to categorize posts and tag them for easy navigation.
*  Incorporate a comment system that allows readers to engage with the content by leaving comments on blog posts.
*  Implement user authentication and authorization to ensure that only authorized users can access and manage the blog's content. Additionally, apply security best practices to protect user data.
* Include SEO-friendly features such as customizable meta tags, clean URLs, and sitemaps to improve the blog's search engine visibility.
* Design the application with scalability in mind, allowing it to handle a growing number of blog posts, users, and concurrent visitors.
*  Ensure that the blog application is responsive and adapts seamlessly to various devices, including desktop computers, tablets, and mobile phones.
*  Create comprehensive documentation that provides clear instructions for setting up, configuring, and using the Django Blog application.
* Implement testing procedures to identify and fix bugs and ensure the application's stability and reliability.
* Integrating third-party services or APIs for additional functionality, such as social media sharings.
<br><br>

### Scope<hr>
**Simple and Intuitive UX**<br>
* Create a website that follows the graphical profile and theme of the blog.
* Create a header and a footer.
* Create a navbar that is visible throughout the website.
* Ensure that all user changes are notified to the user visually.
* Ensure that the user keeps their orientation during their navigation througout the website.

**Features for Upgraded Experience**<br>
* Create user profiles for authors that include details such as their name, profile picture, and a brief bio.
This information is displayed alongside their blog posts.
* Create a Profile page for the user to see list and number of posts created by the user,their social media shares and likes.
* Implement a messaging system that allows users to send messages to the authors. 

**Users % Staff Members Different Accounts**<br>
* Allow access to Admin  only for admin type of users;
* Allow access to Manage Posts page only for authors/staff members type of users;

**Responsiveness**<br>
* Create a responsive website that works on every device and screen size.<br><br>

### Structure<hr>
The website is designed with a focus on user experience and is divided into 8 distinct pages, each serving a specific purpose. The content displayed on these pages varies based on whether the user is authenticated and whether they are a client or staff member. Here are the details:

* **Register/Login:** These pages allow users to create an account or authenticate into an existing one, providing access to various exclusive features.
* **Logout:** This is implemented as a modal dialog that allows users to securely log out of their accounts.
* **Home:** Accessible to all users, this page showcases the restaurant's ambiance, popular dishes, opening & closing times and contact info.
* **Post Detail:** This page displays the blog post detail information. An "Like/Unlike" and "Comment" feature is available only to logged-in users.
* **Contact:** This page enables users to contact blog administator.
* **Authors:** This page displays list of blog authors with profile picture, bio information and list of posts published by the author.
* **Profile:** Exclusive to authenticated users, this page enables both users and blog authors to manage their personal informations.
* **Create post:** Accessible only to authenticated users, this page allows users to apply for author permission and create a post.


#### Flowchart
The project flowchart was created using <b>LucidChart</b>.<br><br>
[![N|Solid](static/images/)](static/images/)<br><br>



### Features
* Use a WYSIWYG (What You See Is What You Get) editor to allow authors to format their posts with headings, lists, images, and other rich media.
* Create author profiles with bio information, profile pictures, and links to their other published posts.
* Organize blog posts into categories to help readers find content related to specific topics or interests.
* Implement a tagging system to associate keywords with blog posts, enhancing searchability and content discovery.
* Enable a comment system for readers to provide feedback, ask questions, and engage in discussions related to the blog post.
* Add social media sharing buttons to make it easy for readers to share blog posts on their social networks.
* Display the author's name prominently on each blog post to give credit and build trust with readers.
* Provide tools for authors and administrators to moderate and manage comments, ensuring a positive and respectful discussion environment.
* Implement a pagination system to the page.
* Ensure that your blog is responsive and works seamlessly on various devices, including smartphones and tablets.
* Create user profiles for registered users, allowing them to edit their personal information.

### Potential Future Features
* Implementing a "Save Favorite Posts" feature on the blog website allows registered users to bookmark and easily access their preferred articles. This feature can enhance user experience and engagement.
* Create a view that retrieves and displays the list of a user's favorite posts. Customize the presentation to include titles, excerpts, or thumbnails of the saved posts.
* Suggest related posts at the end of each blog post to encourage readers to explore more content on your blog.
* If user have user profiles, include a section where users can manage their saved posts within their profiles.
* Allow authors to schedule posts to be published at a specific date and time, helping maintain a consistent posting schedule.
* Allow users to subscribe to receive email notifications when new blog posts are published.
* Email confirmation permission when new user is registered.
* Password reset function where the user will get an email with a reset-password-link in case current password is forgotten.

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, a custom breakpoint of max-width of 768px.

## Testing
The testing documentation can be found at [TESTING.md](TESTING.md) 

# Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

### Requirements (Prerequisites)
Tools and packages required to successfully install this project:

* asgiref==3.7.2
* cloudinary==1.36.0
* coverage==7.3.2
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==3.2.23
* django-allauth==0.58.2
* django-crispy-forms==1.14.0
* django-jazzmin==2.6.0
* django-social-share==2.3.0
* django-summernote==0.8.20.0
* django-widget-tweaks==1.5.0
* gunicorn==21.2.0
* oauthlib==3.2.2
* Pillow==10.1.0
* psycopg2==2.9.9
* PyJWT==2.8.0
* python3-openid==3.2.0
* pytz==2023.3.post1
* requests-oauthlib==1.3.1
* sqlparse==0.4.4

**Database**<br>
The project uses ElephantSQL as PostgreSQL relational database for storing the data.<br>

1. Create Pipfile 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku
    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku
    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page], press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>


# Credits
* Code Institute for the deployment terminal.
* Code Institute Project Scope [Code Institute](h).
* Further studies with []().
* Bootstrap documentation [documentation](https://getbootstrap.com).
* Database setup with []().
* Automated testing with []().
* README layout from [Christian Göran](https://github.com/christiangoran/dome-restaurant-repo/blob/main/README.md).
* 

## Acknowledgements
* Code Institute for providing a great course and support.<br>
* My mentor Gareth McGirr for great guidance and support.<br>
* Slack community for solving roadblocks together and helping each other unconditionally.<br>












