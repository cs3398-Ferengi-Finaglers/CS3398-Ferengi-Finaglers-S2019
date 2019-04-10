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

Leander Davis: For second sprint, I implemented friendslist database (the implementation is in /friendlist).  I learnt even more about django developement (had to learn this to properly build an app in django).  I also entered questions into the database for the questionnaire (we store our db in seperate repository branch because if you don't it will cause merge conflicts that are not possible to resolve.).
Next Step:
My next step is to help with the templates for the displaying friends and allowing to people to friend and unfriend people.  Also I would like to make sure that the site is well organized to allow easier extension, in a whichever way seems the most rational.

Ana Prymachenko Entry and Status: During the first Sprint, I created the database for both the questionnaire and the login pages. The tasks associated with this artifact are in the Database directory in the master branch of the repository. This artifact takes in values from the login website and checks it against the values stored under the login database. Similarly, this artifact stores answers from the questionnaire for the specific user. I have also participated in the creation of the questions that are used in the questionnaire page.                                                                                                                                    
Ana Prymachenko Next Step: My next step is to help the group in the tasks at hand for the next sprint. Furthermore, I will create a database for the registration form that will store the user’s personal information, including name, email, username and password.

[Sprint 2 Progress Report] 
Ana Prymachenko Entry and Status: During the second Sprint, I created an "Send Friend Requests and Add Friends page". The tasks associated with this artifact are in the connect directory in the master branch of the repository. This artifact checks from the database for friend requests associated with the user, outputs them on the page, and allows user to accept said friend requests. Similarly, this artifact allows the user to send friend requests to any users from the database.                                                                                                                                    
Ana Prymachenko Next Step: My next step is to create better form handling and a database that will better store the friendship relationship between users. Furthermore, beutifying this artifact and making it more in line with the SOLID principles will be a priority for the next sprint. 

Jacob Pangonas: During Sprint 2, I created the User Profile page. Currently the only editable field is the bio. I also did reasearch on Gitflow and have an artifact in the artifacts branch with information regarding Gitflow. My next steps will be to make everything editable as well as have a redirect button to the edit profile page. I also need to redirect the user to their profile page when they click on the profile tab.

Jordan Severinson: During sprint 2 I fixed the registration page, and connected it to the questionnaire. My next step is to auto login after registration so the questionnaire works properly h the register.

