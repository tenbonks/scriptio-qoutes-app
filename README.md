# Scriptio | Quotes App

Hello there! this application is a hub of quotes, where you can enter your own easily, contributing to the quote bank, and also filter quotes easily, so if you see a quote by someone you like, just click his name and you will be shown all the quotes said by that person, the same for categories, there are many to choose from, wether you want to fill your mind with mindfulness, or maybe just want to see some classics from Tv shows and movies.

Its all just a click away!

**"Mama says, life is just like a box of chocolate, you never know what you gonna get"**

# Demo

**A live demo of the site can be found** <a href="https://scriptio-qoutes-app.herokuapp.com/" rel="nofollow" target="_blank">Here!</a>

![Desktop Demo](https://github.com/tenbonks/scriptio-qoutes-app/blob/master/static/images/screengrab-scriptio.png "Desktop Demo")

---

# UX

The design and experience of the site is desinged to be as streamlined as possible, everything is easily findable, and filtering is a breeze, just click a name, or category and the desired quotes will be displayed.

I used a simple color scheme of purple shades, and white, this keeps a clean environment and lets links pop, while still looking uniform and allowing the user to see what they can do, without anything distracting them.

1. As a FAN OF FILMS, I want to FIND QUOTES FROM FILMS, So I can RELIVE THE CLASSIC MOMENTS.
2. As a FAN OF OBI-WAN-KENOBi, I want to FIND QUOTES SAID BY HIM, So I can BASK IN THE WISDOM OF THE WISE JEDI.
3. As a USER WHO FEELS DOWN, I want to FIND MINDFULL/MOTIVATIONAL QUOTES, to HELP WITH MY DAY.
4. As a STUDENT WHOS STUDYING, I want to FIND MOTIVATIONAL QUOTES, to get me through MY STUDIES.
5. As a LOVER OF QUOTES, I want to LEAVE QUOTES, for others TO ENJOY.

**Mockup can be found in the files of this repository, under the folder "Mockup".**

I adapted my wireframe into the mockup, mainly being because I was happy with the wireframe, so I started to style it.

---

# Features

* A simple, and clear desing, which clearly shows what the user can do.

- A paginated response, as to not bog down the system with a high amount of data

- A simple to use filter, just click on a name, or category on a post, or go to categories

- A quote counter so the user can see how many quotes there are in any page

- A option to "Contact Me" - For if the user wants to collaborate, or maybe report a bug if found, a confirmation email will be sent to the supplied email address.
---
**Features to implement in the future**

There is a fair bit to be covered here, due to the nature of my site, for perfect implentation I would need to implement a log in system, I had this in mind but due to it being out of scope of the milestone project, it wasnt placed too high.

I had done research on how to implement this and would use "bcrypt" package to hash passwords, there are some features that would come from having a login system, such as the ability to...

Follow users, this would be implemented in a way where the username would be on each post, so it would be clickable to go to the users page, the users page would have all the quotes left by that user, and would be able to "follow user"

A followed users posts would be shown with priority over normal posts in the homepage, also maybe a individual "followed page" which just shows posts from followed users

As mentioned there would be users, so that would also create a need for a profile page, this would follow the websites design, I would also add the ability to delete a user, Im not sure if I would keep the deleted users posts, but if I would, I would edit the user field of the post to be a deleted user, this would elimiate an issue where if a new user chose the deleted users username, the posts would not be linked to the new user.

there is a lot that can be developed off having a log in system, but I'm confident that Ive displayed how the website works, without having the system, also note, had there been a log in, only the user who left the post, would be able to edit it.

I had planned on inplementing a login system, and had in my planning, but upon review of requirements for the project, it was out of scope, and it wasnt the aim of the project, Id of liked to add it but it would of taken too much time away from the actual requirements.

---

# Technologies used

HTML, CSS, Javascript, Python (packages, these can be found in requirements.txt), MongoDB, Flask, Materialize Framework, jQuery Framework, Github, Heroku emailJS , Figma (for design planning).

The site was created on Flask, this allowed for a very quick and versatile way of development, with the use of HTML to layout my site, and jinja2 templating language to populate the content from mongoDB

* HTML - Used in the structuring of the of all files within the template folder

- CSS - Is used for the styling of the site.

- Javascript -  Javacript is used for jQuery, and also for emailJS, this allows user to send a message to me, and also receive a confirmation email if the response was a success,

- Python - Is used for configuring the app, getting the data from MongoDB, also used with flask to create routes and functions for the app.

- Materialize - Used to position elements in the DOM, how I used cards to display each post, a modal for the contact form, materialize forms for any form within the site, buttons for any buttons in the site. I styled all of the elements to fit the site and make them more unique for my project.

- Jquery - I used jQuery to access some of the DOM elements, also for some materialize elements jquery is needed for it to function, I also used it to target the modal, so that if the response from sending a email is ok, then close the modal. 

- emailJS - I used this to send the supplied fields in the contact form to my email address, an auto reply will be sent to confirm the email was received 

- Figma - I used Figma for the design phase of the project, I started with outlines of the layout, and after that I ended up filling them in and refining the elements, it proved very useful especially with deciding on what color scheme I wanted to use, I decided on a 2 tone purple design, which keeps the site uniform and clean throughout.

- MongoDB(noSQL) - Used to store all quotes, a user of Scriptio can perform "crud operations" within the app.

- Github - Used for version control of the app.

- Heroku - Used for deployment of the app.



--- 
# Testing

I performed manual tests on Scriptio, during development and once all the functionality was in place



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


</p>
</details>

---

# Deployment

**I developed Scriptio using VScode on a local machine, I used GitHub for version control, and Heroku for the deployed site**

* Connecting to GitHub 
- I logged into Github, and created a repository, named scriptio-qoutes-app.
- I used the CLI to add the created repo to my remotes | `git remote add origin https://github.com/tenbonks/scriptio-qoutes-app.git`
- Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

* Creation of app in heroku, and connection
- Log in to Heroku (account is required), within the dashboard, click the "new" button featured in the top right of the page.
- Pick the closest region to you
- Using the CLI, add the heroku app as the remote master branch | `heroku git: remote a [app name]`

*Deployment to heroku
- Create app.py, this is the file that heroku will use to start the app
- Create a requirments.txt (list of packages and dependencies, required for the app to run) | <code>pip freeze > requirements.txt</code> (using pip, not pip3 due to virtual env)
- Create a Procfile (Information for heroku, on where to start the app) | <code>echo web: python app.py > Procfile</code>
- Once these were in place, add all files to git, and commit them.
- Push to Github and Heroku, I used vscode's git interface to streamline this, but a command for this is | <code>git push origin master && git push heroku master</code> 
- Instruct Heroku to start the app, (scale dynos) | <code>git push origin master && git push heroku master</code>
- Go back to the app in Heroku, click settings, and youll be able to reveal config vars, I set 2 initially, then added a 3rd later to hide an API KEY.
- The 2 initial config variables were | IP = 0.0.0.0 | PORT = 5000
- Within the applications page in Heroku, it can now be opened and the app will run.


**If you want to run *Scriptio* locally, you can clone this repository into an editor of your choice**

* Paste this into the editors terminal - <code>git clone https://github.com/tenbonks/scriptio-qoutes-app.git</code>

- To cut ties with this GitHub repository, type this into the terminal - <code>git remote rm origin</code>

There is no difference between the deployed version and the development version.

---

**If you want to run *Scriptio* locally, you can clone this repository into an editor of your choice**

* Paste this into the editors terminal - <code>git clone https://github.com/tenbonks/scriptio-qoutes-app.git</code>

- To cut ties with this GitHub repository, type this into the terminal - <code>git remote rm origin</code>

---

# Credits

**Content**

There is some content written by me within the site, all the things that dont change pretty much.
All of the quotes at this time were written by me, but all the quotes are named by who said them.

---

**Media**

Favicon was created using - https://favicon.io/

Textured Backgrounds - https://www.transparenttextures.com/

Typography - Nunito font - https://fonts.google.com/

---

**Acknowledgements**

flask-paginate, this lib is simply amazing - https://pythonhosted.org/Flask-paginate/

Tutors through code-institute, helped with pagination and a modal problem due to using emailJS

My mentor for valuable sessions during development 
