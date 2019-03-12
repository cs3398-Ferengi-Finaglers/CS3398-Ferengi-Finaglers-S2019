# [SaltShaker]

[Vision Statement] The Ferengi Finaglers(Leander Davis, Jacob Pangonas, Karen Proft, Ana Prymachenko, Jordan Severinson) will be working on the website SaltShaker, this website will allow people who play games to search for other people who want to play the same game as them. We are creating this for people who want to play games as a competitive team, or people who are just looking for others to play a game for fun. Many people who play games get frusturated with the game matching them up with people who they can not get along with or play with due to a multitude of reasons, the reason we are creating this website is to minimize this and allow people to enjoy playing games with others instead of getting frustrated by the idea.

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOSDcoZsLE0KZU7Zb39W681rYFs7J-GK7LYYxZNW1uPY0O365p)

[Description] Welcome to the SaltShaker! Our goal for this website is to eliminate the frustration of being matched with people, while playing games, that do not play the game the same way you play the game. Either for serious play or just wanting to play games for fun we hope to connect people with similar personalities, priorities and love for video games together in order to make advantageous teams and make the experience fun for everyone.

[Why is this special?] This project is unique because it shows how one team learns to work together on creating a project that we're all equally passionate about with realistic constraints. 

[Currently] We have completed the questionaire and all the team members have the ability to run django in a virtual enviroment. These will be stepping stones to start building the actual program.

[Sprint 1 Progress Report] 
Jacob Pangonas- During Sprint 1 I was able to get information on implementing the Steam API, the artifact is located in the artifacts branch and is called Steam API links, this links to multiple websites and should help implemnt the API in the future if we have the time. I was unable to fully complete the user profile page because it was a huge undertaking and I did not have enough time with everything else piling up. I should have allocated my time better but I do have a rough idea of what I want the page to look like. I have an html file showcasing that and I will need to put more time into this next time. My next step will be to look into Django more to learn how to get and get the user profile page working.

Jordan Severinson- During Sprint 1 I was able to write some questions for the questionnair and installed django virtual environment on my computer (in artifacts Jordan Django). I also wrote the HTML landing page we are using which was adapted to django templates by Karen (is serves as the homepage and is located in landingpage/templates). I also worked on the registration and login pages which don't work yet because the last two weeks have been filled with exams and homeworks (under Login and registration respectvely). My next step after my test on Thursday is to finish learning enough django to finish my registration page. Then I will look up how to connect that to the database, then I will finish implementing the Login page and merge it with the questionnaire

Karen Proft - 
Entry:
The questionnaire code for this sprint was written by Karen Proft. The artifact for the tasks associated with this is the code and files within the questionnaire folder on the main branch of the repository. This artifact pulls up a multiple choice quiz for the user to answer the questions to once the django server is running. This questionnaire can be accessed by going to localhost:8000/questionnaire when the server is running. Currently a user does not have to be logged in to access the questionnaire.
Status:
I have completed looking into the KNN equation for the project and deducted that we may use tensorflow to integrate in the equation or past KNN code I've written from my machine learning course (we will have to modify it to work in python). The CSS of the questionnaire is also completed, although it could still use some work to fit in better with the website's theme. The code for the questionnaire has been completed, as well as my portion of adding questions to be used on the questionnaire, setting up my local environment, and creating the instructions for the other members of my team to do so as well (this can be found in the artifact branch).
Next Step:
My next step will be to help task out the next sprint, to integrate the user login system with the questionnaire portion of the site so that when a user logs in they are redirected to the questionnaire, and to create different of types of question formats, not just multiple choice question types.

Leander Davis: During the first sprint, I spent the majority of my time learning Django.  I setup  a local test environment and created a Django server.  I helped setup standardized headers and footers for the website.  I generated sample data for testing algorithms when they are ready and to put a load on the database. I helped with bringing the code together and troubleshoot it.  Helped generate questions for the questionnaire.
Next Step:
My next step is to figure out how to convert JSON data into fields in a database to make it easier to apply the KNN algorithm.  I will learn more about Django to help make the site more dynamic.  Also I plan on learning more about KNN so I can apply Exponential Weighted Average to the hidden values of the users to help better match them.
