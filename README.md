# Byte by Byte

<img src="static/images/am_i_resposive.png" >

Welcome to Byte by Byte, a Django-based tech blog that delivers in-depth insights, tutorials, and articles on the latest trends and technologies in the tech world.
This application allows user to create, edit, and manage blog posts. It also includes user authentication and comment functionality. Below is guide through the setup and usage of this application.

## Table of Contents
- [Introduction](#introduction)
- [UX](#ux)
- [Flowchart](#flowchart)
- [Features](#features)
- [Potential Future Features](#potential-future-features)
- [Enhancements](#enhancements)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](TESTING.md)
- [Manual Testing](MANUAL_TESTING.md)
- [Automated Testing](TESTING.md)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction
Byte by Byte is a platform for tech enthusiasts, developers, and writers. It features a responsive design, user authentication, a comment system, and more.

Access the deployed project at [Byte by Byte](https://final-project-ada-02b27917ae0c.herokuapp.com/).

## UX
### User Stories
Catering to visitors, registered users, and authors/staff members, Byte by Byte covers a wide range of functionalities. Visitors can view and filter posts, registered users can like, comment, and create posts, while authors have extended management capabilities.

Go to [User Stories](https://github.com/users/adamolnar/projects/9/views/1).

<img src="static/images/user_stories.png">

#### Table of User Stories

| Role                | User Story                                                                                         | Done  |
|---------------------|----------------------------------------------------------------------------------------------------|-------|
| **Visitor**         | As a Site User I can view a list of posts so that I can select one to read.                        | Yes   |
|                     | As a Site User, I can view a paginated list of posts so that easily select a post to view.         | Yes   |
|                     | As a Site User I can click on a post so that I can read the full text.                             | Yes   |
|                     | As a Site User / Admin I can view comments on an individual post so that I can read the conversation. | Yes   |
|                     | As a Site User, I can send messages through the contact form, so that I can inquire about needed topic. | Yes   |
|                     | As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral | Yes   |
|                     | As a Site User I can register an account so that I can comment and like.                          | Yes   |
|                     | As a Site User I can easily navigate to post with similar content so that I can find more information about the topic I am interested in. | Yes   |
|                     | As a Site User I can filter posts on category I am interested in so that I can find relevant information faster. | Yes   |
|                     | As a Site User I can see the newest post so that I can be up to date with the blog content.       | Yes   |
|                     | As a Site User, I am presented with a wide range of options for sharing content so I can have quick access to desired content from my email or any other app. | Modified   |
|                     |"As a Site User I can find content by searching for particular words so that I have a quick or less complex way to find content."| No  |
| **Registered User** | As a Site User I can like or unlike a post so that I can interact with the content.                | Yes   |
|                     | As a Site User I can leave comments on a post so that I can be involved in the conversation.       | Yes   |
|                     | As a Site Admin I can create draft posts so that I can finish writing the content later.           | Yes   |
| **Author/Staff**    | As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. | Modified   |
|                     | As a Site Admin I can create, read, update, and delete posts so that I can manage my blog content. | Yes   |


These user stories cover a range of user types, including visitors, registered users, and authors/staff members, and address various functionalities and features of the Blog application. 

## Flowchart
The project flowchart was created using <b>LucidChart</b>.

<img src="static/images/flowchart.png" >

## Features
- User authentication: login, logout, register.
- User profiles for customization and personal information management.
- CRUD operations for blog posts and comments.
- WYSIWYG editor for rich text formatting.
- Author profiles with bio and post links.
- Responsive design using Bootstrap.
- Image uploads with Cloudinary, tagging, categorization.
- Social media sharing buttons.

## Potential Future Features
- Implementing a "Save Favorite Posts" feature.
- Scheduling posts for publication.
- Email notifications for new posts.
- Search functionality and performance optimization.

## Enhancements
### Technical Improvements
- Robust search feature for content discoverability.
- Performance optimization using caching.
- SEO enhancements for increased organic traffic.
- Full accessibility compliance.

### User Engagement and Community Features
- Enhanced user profiles with more customization.
- Community forum for user discussions.
- Interactive tutorials and quizzes.
- Encouraging user-generated content.

### Monetization Strategies
- Membership or subscription models.
- Affiliate marketing and sponsored posts.
- Advertisements targeting tech audiences.

### Analytics and Feedback
- Advanced analytics for tracking user behavior and content popularity.
- Tools for collecting user feedback.
- Regular A/B testing for feature and design enhancements.

### Security Enhancements
- Regular security audits.
- Implementation of Two-Factor Authentication (2FA) for user accounts.

## Technologies Used
- Django
- PostgreSQL
- Bootstrap
- Cloudinary
- django-summernote
- And more [requirements.txt](requirements.txt)

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

1. Create Pipfile 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku
    - Go to the Heroku website (https://www.heroku.com/) 
    - Login to Heroku and choose *Create App* 
    - Click *New* and *Create a new app*
    - Choose a name and select your location
    - Go to the *Resources* tab 
    - From the Resources list select *Heroku Postgres*
    - Navigate to the *Deploy* tab
    - Click on *Connect to Github* and search for your repository
    - Navigate to the *Settings* tab
    - Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku
    - Go to the Deploy tab.
    - Choose the main branch for deploying and enable automatic deployment 
    - Select manual deploy for building the App 

#### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/adamolnar/Final_Project?tab=readme-ov-file), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

#### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/adamolnar/Final_Project?tab=readme-ov-file), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created

## Testing
The testing documentation can be found in the [Testing Documentation](TESTING.md).

## Manual Testing 
The documentation for manual testing can be found in the [Manual Testing](TESTING.md).

## Automated Testing 
For automated testing details, refer to the [Testing Documentation](TESTING.md). 

## Credits
- Code Institute for the deployment terminal [CodeInstitute: FST101](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2/courseware/b31493372e764469823578613d11036b/ae7923cfce7f4653a3af9f51825d2eba/).
- Code Institute Project Scope [Code Institute || I Think Therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/).
- Django Tutorial [Mmdm](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models).
- Bootstrap documentation [Bootstrap Documentetion](https://getbootstrap.com).
- How to add Social Share buttons in Django [Tutorialspoint](https://www.tutorialspoint.com/how-to-add-social-share-buttons-in-django).
- 404 page [CodePen](https://codepen.io/Navedkhan012/pen/vrWQMY).
- Bootstrap blog theme [Startbootstrap](https://startbootstrap.com/previews/blog-home).
- Django blog tutorial [Dontrepeatyourself](https://dontrepeatyourself.org/post/django-blog-tutorial-part-3-users-authentication/#profile-page?utm_content=cmp-true).
- Automated testing with [Code Institute || Python Testing](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PT101+2021_T1/courseware/f20cd699fac3480b99004d1fc3f265ef/bfd6dc4d46c94af89af71f2525c66e0f/).
- Automated testing with [Realpython](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-models).
- README layout from [Christian Göran](https://github.com/christiangoran/dome-restaurant-repo/blob/main/README.md).

## Media
- Image for blog posts 'How to Write an Effective Blog Post: A Step-by-Step Guide' [The Anatomy of a Perfect Blog Post](https://www.salesforce.com/ca/blog/2016/08/anatomy-of-a-perfect-blog-post.html)
- Image for blog posts 'Django Form: From Zero to Hero - Mastering Form Handling' [Java67](https://www.java67.com/2020/06/top-5-courses-to-learn-django-and-python-for-web-development.html)
- Image for blog posts 'Navigating Impostor Syndrome as a Software Developer' [Hackernoon](https://hackernoon.com/the-impostor-syndrome-among-us)


## Acknowledgements
- Code Institute for providing a great course and support.
- My mentor Gareth McGirr for great guidance and support.
- Slack community for solving roadblocks together and helping each other unconditionally.












