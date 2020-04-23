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

I sent a link out through personal messages
This site was tested on multiple popular browsers, such as Chrome, Safari, Internet Explorer, FireFox, I also used the "Device Toolbar" in dev tools to emulate a variety of mobile devices, Iphone 4/5/6 and Samsung Galaxy. The only compatibility issue that appeared was the footer and banner background not loading. This was due to me using "RGB" and setting opacity to it, this was rectified by using "RGBA". No other issues across browsers.

<details><summary>CLICK HERE for testing process'</summary>
<p>

1. gravBall on page load, should display a start screen, if clicked should start to draw the game and update the canvas
    1. Load the website.
    2. Check the canvas element to see if the expected function is running (drawStart).
    3. Click the canvas to see if the gamestate changes as expected (drawGame) is now running.
    4. This verifies the boot process of the game is working as expected.

2. Does gravBALL change to "Oops!" (drawLose) screen if collision is detected:
    1. Click the canvas to start game.
    2. Let the ball freely bounce until collides with a pillar.
    3. The canvas changes to "Oops" as expected.
    4. This verifies that the collision mechanic of the game is working as expected.

3. I expect there to be no sound, if mute button has been clicked since the page loaded:
    1. Click the mute button above canvas, and verify the text below the mute button changes to "Sound off".
    2. Click the canvas to start game. no starting sound was played when canvas was clicked.
    3. Let the ball freely bounce, no sound on ball bounce.
    4. Let the ball freely bounce and hit pillar, no sound when a collision is detected.
    5. Pass an obstacle and there is no sound to indicate the score incrementing.
    6. Let the ball collide with a pillar to get to the "Oops!" screen, when clicking to restart, no sound is played to indicate the start of the game.
    7. This verifies that the mute button is working as expected once clicked.

4. I expect there to be sound, if mute button has not clicked since page loading:
    1. Upon loading the text underneath the mute button should read "Sound on", this means sound is on by default as expected.
    2. Click the canvas to start game. Starting sound was played when canvas was clicked.
    3. Let the ball freely bounce, Sound was played on ball bounce.
    4. Let the ball freely bounce and hit pillar, played sound when a collision is detected.
    5. Pass an obstacle and a sound is played to indicate the score incrementing.
    6. Let the ball collide with a pillar to get to the "Oops!" screen, when clicking to restart, a sound is played to indicate the start of the game.
    7. This verifies that by default sound is on, and sound will play as expected when conditions are met.

5. Contact form/modal:
    1. Click the "Contact Me" button in the footer of the page.
    2. Try to submit the empty form and verify that an error message "Please fill in this field." appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
    5. If cancel/X in the top right corner, is clicked the *Modal* will close.

6. I expect the DOM to display a message saying the screen is too small, and the game canvas not to be displayed, if page is loaded under the small Bootstrap breakpoint:
    1. Load the page.
    2. Click on developer tools, and select "Toggle device toolbar" from the options.
    3. Check the expected message is displayed
    4. Check the game canvas is not being displayed.
    5. This is verifies it is functioning as expected.

7. I expect the high score to be kept if the page is reloaded, also for the high score to update if greater than the last.
    1. Load the page.
    2. Played the game, got a score of 1.
    3. Reloaded the page.
    4. The start screen displays "High Score: 1", also opened developer tools and checked under local storage to see if it was set.
    5. Local storage "high score" set to "1".
    6. Repeated step 2, but got a score of 7.
    7. Reloaded page
    8. The start screen displays "High Score: 7", also opened developer tools and checked under local storage and "high score" was set to "7".

8. I expect the canvas to not register key input if I've clicked outside of the canvas element
    1. Load the page.
    2. Click inside the canvas to start the game.
    3. Click outside of the canvas once the game has started.
    4. hold down *spacebar*, the ball freely bounces which means key input isn't being registered
    5. This verifies it is functioning as as expected.

9. I expect to receive an email if I correctly fill out all fields of the contact modal
    1. Fill out the contact form, correctly, as tested in "Test 5", with a different email address to the one emailJS is set up to send to.
    2. Click "Send!" button.
    3. Sign into my gmail account, look at most recent email/s.
    4. The test email was received.
    5. I logged into the email address I provided in the contact modal.
    6. The auto reply has been received, confirming the email has been sent.
    7. This verifies that the contact modal, is working with emailJS as expected.

</p>
</details>

---

# Deployment

**The deployment of this site was achieved with "Heroku", the process I took as follows...**

* I logged into Github, and created a repository, named scriptio-qoutes-app.
- I logged into Heroku, created a repository, gave it a matching name from Github, "scriptio-qoutes-app".
- I created a "Procfile", and "requirements.txt", this is required for the app to work within "Heroku"
- I pushed the initial commit to Github, and kept committing and pushing when any minor, or major change had been made that I was happy w.
- I pushed to Heroku, verified that deployment went okay via the log in Heroku, after that I scaled dynos via the terminal.

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
