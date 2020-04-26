# ![alt text](https://github.com/tenbonks/scriptio-qoutes-app/blob/master/static/images/scriptio-logo.png) | Quotes App

Hello there! this here is Scriptio, which has a meaning of written words in Latin, is a hub of quotes, where you can post quotes easily, contributing to the quote bank, and also filter quotes, so if you see a quote by someone you like, just click the name and you will be shown all the quotes said by that person, the same for categories, there are many to choose from, whether you want to fill your mind with mindfulness, or maybe just want to see some classics from TV Shows and Movies.

Its all just a click away!

*"Mama says, life is just like a box of chocolate, you never know what you gonna' get"*

# Demo

**A live demo of the site can be found** <a href="https://scriptio-qoutes-app.herokuapp.com/" rel="nofollow" target="_blank">Here!</a>

![Desktop Demo](https://github.com/tenbonks/scriptio-qoutes-app/blob/master/static/images/scriptio-screengrab.png "Desktop Demo")

---

# UX

The design and experience of the site is desinged to be as streamlined as possible, everything is easily findable, and filtering is a breeze, just click a name, or category and the desired quotes will be displayed.

I used a simple color scheme of purple shades, and white, this keeps a clean environment and lets links pop, while still looking uniform and allowing the user to see what they can do, without anything distracting them.

1. As a FAN OF FILMS, I want to FIND QUOTES FROM FILMS, So I can RELIVE THE CLASSIC MOMENTS.
2. As a FAN OF OBI-WAN-KENOBi, I want to FIND QUOTES SAID BY HIM, So I can BASK IN THE WISDOM OF THE WISE JEDI.
3. As a USER WHO FEELS DOWN, I want to FIND MINDFULL/MOTIVATIONAL QUOTES, to HELP WITH MY DAY.
4. As a STUDENT WHOS STUDYING, I want to FIND MOTIVATIONAL QUOTES, to get me through MY STUDIES.
5. As a LOVER OF QUOTES, I want to LEAVE QUOTES, for others TO ENJOY.


**Mockup can be found under the folder "Mockup" in this repo, or [here](https://github.com/tenbonks/scriptio-qoutes-app/blob/master/mockup/Scriptio%20_%20Mockup.png).**


there is no wireframe to show, as I adapted my wireframe into the mockup, mainly being because I was happy with the wireframe, so I started to style it.

---

# Features

* A simple, clear and responsive design, which clearly shows what the user can do.

- A vibrant header, with app's logo, navigation buttons, this adapts to sidebar navigation for mobile.

- A paginated response, as to not bog down the system with a high amount of data

- A simple to use filter, just click on a name, or category on a post, or go to categories

- A quote counter so the user can see how many quotes there are in any page, category or said by the same person.

- Full CRUD (Create, Remove, Update, and Delete) operations of a database through the application

- A option to "Contact Me" - For if the user wants to collaborate, or maybe report a bug if found, a confirmation email will be sent to the supplied email address.
---

**Features to implement in the future**

There is a fair bit to be covered here, due to the nature of my site, for perfect implementation I would need a log in system, I had this in mind during development but due to it being out of scope/not a requirement for this milestone project, it wasn't a priority.

I had done research on how to implement this had it of been, I would of used "bcrypt" library to hash passwords to keep them secure, there are some features that would come from having a login system, such as the ability to...

This is the biggest issue that comes from not having a log in system, and that is user authentication, currently anyone can edit and delete comments, and this would be an issue in real world application, and that is understood, I would of liked to add it purely for the defensive design, but it isn't the focus of this project.

Follow users, this would be implemented in a way where the username would be on each post, so it would be clickable to go to the users page, the users page would have all the quotes left by that user, and would be able to "follow user"

A followed users posts would be shown with priority over normal posts in the homepage, also maybe a individual "followed page" which just shows posts from followed users

As mentioned there would be users, so that would also create a need for a profile page, this would follow the websites design, I would also add the ability to delete a user, Im not sure if I would keep the deleted users posts, but if I would, I would edit the user field of the post to read "Delted User" or similar, this would elimiate an issue where if a new user chose the deleted users username when creating account, the posts would not be linked to the new user.

there is a lot that can be developed off having a log in system, but I'm confident that Ive displayed the data-centric side of my project, in the way that it handles data left by a user, without having the system.

---

# Technologies used

HTML, CSS, Javascript, Python (packages, these can be found in requirements.txt), MongoDB, Flask, Materialize Framework, jQuery Framework, Github, Heroku emailJS , Figma (for design planning).

The site was created on Flask, this allowed for a very quick and versatile way of development, with the use of HTML to layout my site, and jinja2 templating language to populate the content from mongoDB

* HTML - Used in the structuring of the of all files within the template folder

- CSS - Is used for the styling of the site.

- Javascript -  Javacript is used for jQuery, and also for emailJS, this allows user to send a message to me, and also receive a confirmation email if the response was a success,

- Python - Is used for configuring the app, getting the data from MongoDB, also used with flask to create routes and functions for the app.

- Materialize - Used to position elements in the DOM, how I used cards to display each post, a modal for the contact form, materialize forms for any form within the site, buttons for any buttons in the site, toasts are also used within the site. I styled all of the elements to fit the site and make them more unique for my project.

- Jquery - I used jQuery to access some of the DOM elements, also for some materialize elements jquery is needed for it to function, I also used it to target the modal within emailJS.js. 

- emailJS - I used this to send the supplied fields in the contact form to my email address, an auto reply will be sent to confirm the email was received 

- Figma - I used Figma for the design phase of the project, I started with outlines of the layout, and after that I ended up filling them in and refining the elements, it proved very useful especially with deciding on what color scheme I wanted to use, I decided on a 2 tone purple design, which keeps the site uniform and clean throughout.

- MongoDB(noSQL) - Used to store all quotes, a user of Scriptio can perform "crud operations" within the app.

- Github - Used for version control of the app.

- Heroku - Used for deployment of the app.


--- 
# Testing

I performed manual tests on Scriptio, during development and once all the functionality was in place, please click the dropdown below for the processes I took.

I validated my HTML using W3C HTML Validation Service, This returned some errors, but these are caused by using template language within the html, so these are accounted for and aren't a problem. I also validated my css with W3C CSS Validation Service, and this validated at CSS Level 3 + SVG.

This site was tested on multiple popular browsers, such as Chrome, Safari, Internet Explorer, FireFox, I also used the "Device Toolbar" in dev tools to emulate a variety of mobile devices, such as  the Iphone 4/5/6 and Samsung Galaxy, aswell as the media breakpoints.

<details><summary>CLICK HERE for testing process'</summary>
<p>

1. The content of the site should resize fluidly to specific breakpoints
    1. Load the website on a large desktop monitor.
    2. Check all pages of the site to check the layout is as expected.
    3. Open developer tools and repeat step 2 at xs, small, medium breakpoints
    4. The layout is as expected and elements will display to fit the device its being displayed on.
    5. This verifies that the site is responsive to different screen size, and aspect ratios.

2. If a name is clicked within the quote container, it should filter quotes by selected name:
    1. Click "Obi-Wan Kenobi" within a quote
    2. I am sent to a new page, which filters quotes by name, Obi-Wan Kenobi is specified in the heading.
    3. All quotes by Obi-Wan Kenobi are being displayed.
    4. I repeated step 1-3 for "Oprah Winfrey" and the expected result was returned
    5. This verifies that the filter is working as expected

3. If a category name is clicked within a quote, or withing the categories page, all quotes within category should be returned
    1. Once the website is loaded, click "Mindfulness"
    2. Im redirected to a new page which filters quotes by category, Mindfulness is specified in the heading.
    3. All quotes within the page have the category name of "Mindfulness"
    4. I repeated this for "Famous" category, and all results were as expected.
    5. This verifies that the filter for category is working as expected.

4. If no quotes are returned within a category, alert the user that there are none.
    1. Load the website, and click the nav button for categories.
    2. Within the categories page, click "Funny" category
    3. Im redirected to the page which filters quotes by category.
    4. "Funny" is specified in the heading, and a message within the DOM is present telling the user "Oops, no quotes to be seen here".
    5. A button is featured underneath to promt the user to add a quote from the same page.
    6. This verifies that if no quotes are within a category, the user is alerted, and that the this function of the site works.

5. Contact form/modal:
    1. Click the "Contact Me" button in the footer of the page.
    2. Try to submit the empty form and verify that an error message "Please fill in this field." appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that the modal closes.
    5. If cancel, is clicked the *Modal* will close.
    6. If the modal is submitted with an "OK" status, then close the modal.
    7. This verifies that the modal is working as expected, and forms cant be submitted empty.



6. I expect to receive an email if I correctly fill out all fields of the contact modal
    1. Fill out the contact form, correctly, as tested in "Test 5", with a different email address to the one emailJS is set up to send to.
    2. Click "Send!" button.
    3. Sign into my gmail account, look at most recent email/s.
    4. The test email was received.
    5. I logged into the email address I provided in the contact modal.
    6. The auto reply has been received, confirming the email has been sent.
    7. This verifies that the contact modal, is working with emailJS as expected.


7. I expect not to be able to submit a post with a field empty.
    1. Load the page, and proceed to "Add Quote" within the page header.
    2. Try to submit form with all fields empty and verify a prompt appears to the user to "Fill in field"
    3. Try to submit a from with no "quote" and verify a prompt appears to the user to "Fill in field"
    4. Try to submit a from with no "said_by" and verify a prompt appears to the user to "Fill in field"
    5. Try to submit a from with no "category" selected and verify a prompt appears to the user to "Fill in field"
    6. This verifies that a post cannot be submitted with a empty field

8. I expect there to be a connection with mongoDB
    1. Load the page.
    2. The Home page is being populated with quotes, these are coming from mongoDB
    3. This means connection is valid upon page load, and is verifies that I am connected to the expected DB


9. I expect post to be limited to 10 per page
    1. Load the page, count the amount of quotes
    2. Counted 10 quotes, clicked the next page
    3. Counted another 10 quotes
    4. the information for the page is also correct in stating 0-10 posts being shown upon initial page load.
    5. This verifies that pagination is working as expected


10. I expect all the fields of a post to be carried to the form, if clicking edit on a quote
    1. Load the page, and click edit on one of the quotestenbo
    2. I am redirected to edit quote page
    3. All the fields have been carried over as expected
    4. this verifies that the fields are being supplied when editing a quote

11. I expect that when I edit a field within a quote, it is inserted
    1. Load the page, click edit on one of the quotes
    2. I am redirected to edit page.
    3. I added "(test)" to "Quote" field and hit submit
    4. I am redirected to the home page, and see that (edit) has been added to selected quote
    5. This verfies a quote can be edited

12. Can not submit a post within edit with a empty field
    1. Load the page, click edit on one of the quotes
    2. I am redirected to edit page.
    3. I blank out the quote section and try to submit
    4. A prompt for the user is displayed to "Fill in field"
    5. I blank out the category.
    6. A prompt for the user is displayed to "Fill in field", and then the category
    7. A prompt is displayed on the category to "Fill in field"
    8. This verifies that a quote needs to have all field filled before it is edited. 

13. I expect pagination not to have page links if less than 10 quotes return
    1. Load the page and click "categories" nav button in header
    2. Click on the "Video Games" Button
    3. Pagination info displaying 1-1, quotes in total 1
    4. Check under the content for pagination links, there are none
    5. This verifies my expectations
</p>
</details>

---

# Deployment

**I developed Scriptio using VScode on a local machine, I used GitHub for version control, and Heroku for the deployed site**

**Connecting to GitHub**
- I logged into Github, and created a repository, named scriptio-qoutes-app.
- I used the CLI to add the created repo to my remotes | `git remote add origin https://github.com/tenbonks/scriptio-qoutes-app.git`
- Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

**Creation of app in heroku, and connection**
- Log in to Heroku (account is required), within the dashboard, click the "new" button featured in the top right of the page.
- Pick the closest region to you
- Using the CLI, add the heroku app as the remote master branch | `heroku git: remote a [app name]`

**Deployment to heroku**
- Create app.py, this is the file that heroku will use to start the app
- Create a requirments.txt (list of packages and dependencies, required for the app to run) | <code>pip freeze > requirements.txt</code> (using pip, not pip3 due to virtual env)
- Create a Procfile (Information for heroku, on where to start the app) | <code>echo web: python app.py > Procfile</code>
- Once these were in place, add all files to git, and commit them.
- Push to Github and Heroku, I used vscode's git interface to streamline this, but a command for this is | <code>git push origin master && git push heroku master</code> 
- Instruct Heroku to start the app, (scale dynos) | <code>git push origin master && git push heroku master</code>
- Go back to the app in Heroku, click settings, and you'll be able to reveal config vars, I set 2 initially, then added a 3rd later to hide my MONGODB_URI.
- The 2 initial config variables were | IP = 0.0.0.0 | PORT = 5000
- Within the applications page in Heroku, it can now be opened and the app will run.


**If you want to run *Scriptio* locally, you can clone this repository into an editor of your choice**

* Paste this into the editors terminal - <code>git clone https://github.com/tenbonks/scriptio-qoutes-app.git</code>

- To install libraries for Python, create a virtual environment(for local machines), and use this code -  <code>pip install -r requirements.txt</code>

- To cut ties with this GitHub repository, type this into the terminal - <code>git remote rm origin</code>

There is no difference between the deployed version and the development version.

---


# Credits

**Content**

There is some content written by me within the site, all the things that don't change pretty much, so navigation elements and such.
All of the quotes at this time were written by me, but all the quotes are respectively named by who said them.

---

**Media**

Favicon was created using using [favicon.io](https://favicon.io/)

[Textured Backgrounds](https://www.transparenttextures.com/) - diagmonds (dark), created by [INS](https://www.flickr.com/photos/ins) 

Typography - Nunito font | [Google Fonts](https://fonts.google.com/)

Logo was created using [logomakr](https://logomakr.com/)

---

**Acknowledgements**

[flask-paginate](https://pythonhosted.org/Flask-paginate/), this lib is simply amazing, and helped a lot during implentation of pagination

This demonstration repository on Github of how to use Flask-Paginate was also very useful - https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

Tutors through code-institute, helped with pagination and a modal problem due to using emailJS

Users on slack for bits of knowlege, and also to mention "Paul F_alumni" for taking time to look over my project in peer-code-review channel. 

My mentor, Maranatha Ilesanmi for valuable sessions during key points of development 
