### Running the tests

## Table of Contents
* [Testing](#testing)
  + [1. Base Setup](#base-setup)
  + [2. Stand Alone Pages](#stand-alone-pages)
  + [3. Authentication](#authentication)
  + [4. Contact](#contact)
  + [5. Menu](#menu)
  + [6. Bookings](#bookings)
  + [7. Deployment](#deployment)
  + [8. Documentation](#documentation)    
* [Browser Testing](#browser-testing)
* [Code Validation](#code-validation)
  + [HTML](#html)
  + [CSS](#css)
  + [JavaScript](#javascript)
  + [Python](#python)
  + [Accesibility](#accesibility)
  + [Performance](#performance)
* [Bugs](#bugs)


### Input validation and error checking


### Browser Testing
<hr>
The website was tested on different browser for assuring the features work accordingly.
* Safari
* Chrome
* Firefox
* Edge
* Opera


### Code Validation
<hr>

#### HTML

The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>
At the time of deployment the validation have the following outcome:<br><br>

<img src="static/images/" width="40%"><br><br>

The following pages have been tested:
* Home
* Detail Post
* Contact Üage
* Author List
* Login/Register
* Profile
* Author Detail Page
* 403/404/500 custom pages
<br>


#### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *style.css* has the following outcome:<br><br>

<img src="static/images/" width="40%"><br><br>
<br>

#### Javascript

...

<br>

### Python
The python code was tested using [Coding Institutes Python Linter](https://pep8ci.herokuapp.com/).<br>

**Pep8 results:**<br>
<details>
<summary>Author app</summary>

* **apps.py**<br>

<img src="static/images/" width="60%"><br><br>

* **urls.py**<br>

<img src="static/images/" width="60%"><br><br>

* **views.py**<br>

<img src="static/images" width="60%"><br><br>

* **forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **models.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_views.py**<br>

<img src="static/images/" width="60%"><br><br>

</details>
<br>

<summary>Blog app</summary>

* **apps.py**<br>

<img src="static/images/" width="60%"><br><br>

* **urls.py**<br>

<img src="static/images/" width="60%"><br><br>

* **views.py**<br>

<img src="static/images" width="60%"><br><br>

* **forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **models.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_views.py**<br>

<img src="static/images/" width="60%"><br><br>

</details>
<br>

<summary>Profile app</summary>

* **apps.py**<br>

<img src="static/images/" width="60%"><br><br>

* **urls.py**<br>

<img src="static/images/" width="60%"><br><br>

* **views.py**<br>

<img src="static/images" width="60%"><br><br>

* **forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **models.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_forms.py**<br>

<img src="static/images/" width="60%"><br><br>

* **test_views.py**<br>

<img src="static/images/" width="60%"><br><br>

</details>
<br>


### Accesibility 
The accesibility of the website was tested with [Wave](https://wave.webaim.org/)
Throughout the all pages there is an Alert due to a "Home" link in the navbar that is situated next to the company-logo that also works as a "home"-link. I decided to ignore this alert to make it easier for the user to find their way back to the starting page.


**Wave results:**
<details>
<summary>Home Page</summary>
<img src="static/images/" width="50%"><br><br>
</details>
<details>
<summary>Authors List Page</summary>
<img src="static/images/" width="50%"><br><br>
</details>
<details>
<summary>>Contact Page</summary>
<img src="static/images/" width="50%"><br><br>
</details>
<details>
<details>
<summary>Profile Page</summary>
<img src="static/images/" width="50%"><br><br>
</details>
<summary>Login Page</summary>
<img src="static/images/" width="50%"><br><br>
</details>
<br>

### Performance
The performance of the website was tested with [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

**Lighthouse reports:**<br>

<details>
<summary>Desktop</summary>

<img src="static/images/" width="60%"><br><br>

</details>

<details>
<summary>Mobile</summary>  

<img src="static/images/" width="60%"><br><br>

</details>



![PEP 8]()

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs like numbers which are expected, empty input, string instead of letters, same input twice.
- Tested in my local terminal and the Code Institute Heroku terminal.



## Bugs

### Solved Bugs 

- 




### Remaining Bugs
- No bugs remaining.

### Validator Testing
- PEP 8
  - White spaces
  - To long strings 
  - After all corections no error were returned PEP8online.com
