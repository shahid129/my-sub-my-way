# My-Sub My-Way
![Main Page](/assets/images/main_image.png)

[View Live Project Here](https://my-sub-my-way.herokuapp.com/)

## TABLE OF CONTENTS
- [User Experience/User Interface](#user-experience-or-user-interface)
- [Design](#design)
- [Features](#features)
- [Testing](#testing)
- [Technology](#technology)
- [Deployment](#deployment) 
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)

## User Experience or User Interface
### First Time User.
As a first time user I want:
- The user to have a warm welcome
- The user to have a clear idea of the ordering system.
- The ordering system to function properly and ordering system to be intuitive.
- The user can understand what the ordering system is about just from the name of the ordering system.
- The user to know the rules of the ordering system.
- The system gives the user hint of either to enter number or letters

### As Return or Frequent User.
As a return or frequent user I want:
- To be able to be able to be acknowledged by the system.
- The system to display the last order

### As a Owner of The Game.
As a owner of the game, I want:
- The user to know how to order from the main screen.
- The user to be given option, that if they would like to order more sub.

## Design

### Why I chose this project 
When it comes to building and designing a project, the first question that comes to my mind is, what am I going to build? when I googled for ideas it gave me millions of options and ideas that I could do. Games like tic tac toe, hangman, battleship, guess the number, and building a calculator are great options. I thought of making a hangman game. When I started building hangman, I found myself in a state of lost. The codes of these games are easily available all over the internet and I found myself looking for a solution all the time. This is when I said I need to build something by myself. I need to sweat my brain because that's the only way to learn something. That is when I came with the idea of building this project. The project calls an API to send and receive data and it manipulates those data to display required information to the user.

### Basic Design
Basic design of the game was built using the lucidchart website. The logic of the game was implemented in the 
chart. Once I was satisfied with the logic, I started to code. I tried not to use too many colors and make the terminal look messy.
The colors used are as follows:
- Green - for user inputs
- White - Most of the text
- Red - Whenever the code handled an error and throws an information to the user.

[Flow Chart Image](assets/images/flow-chart.png)


## Features
There are a lot of features in this website and they are as follows -
- The user can enter their last name and the name should be more than two characters and less than 25 characters.
- The terminal throws a message to the user when -
    - There is/are a special character in the name.
    - There is/ are numbers in the name.
    - Or there is an empty name input.
    Image of Error when name is not accepted. [Image](assets/images/name_error.png)
- The user receives a warm welcome by saying "Welcome to My-Sub My-Way Username"
- When user is asked to choose either footlong or six inch, the user has only option to type 'a' or 'b'.
- The terminal throws a message to the user when -
    - The user types a number
    - the user types any letter but a or b
    - The user inputs nothing and press enter
    Image of Error when typed wrong and  is not accepted. [Image](assets/images/footlong_error.png)

- The user is asked to choose what type of bread he/she would like to have.
- The terminal throws a message to the user when -
    - The user types letters instead of numbers.
    - The user types multiple numbers instead of one number.
    - The user types a number that is not in the list.
    - The user inputs nothing and presses enter.
    - The uer types special characters.
    Image of Error when typed wrong and  is not accepted. [Image](assets/images/bread_error.png)
- The same error pops up for most of the ordering system
- The user is limited to choose vegetables only six time.
- The user is limited to choose only three sauces rather than choosing all the sauces. [Image](assets/images/sauce_error.png)
- Once the order is complete, the ordering system calculates the price and offers the user if they 
   would like to have 15% off their bill.
- If the user select 'y', the system calculates the bill by taking off 15% off the price.
- The Receipt is Printed in the end which gives all the details of the order. [Receipt Image](assets/images/receipt.png)
- Once the order is complete the user is asked if he/she would to order again.

### One of the best features of this system is that, if the username exist in the system, it asks the user if he/she would like to view the last receipt. It always shows the last receipt. [Image of last Receipt](assets/images/last_receipt.png)

## Testing
Testing was done using the PEP8 Online. 
- Copy and paste code from run.py file to PEP8 Online checker. 
- Hit the check code button and it shows if you have any error or not.
In my case NO ERROR was found and it says ALL RIGHT
[PEP8 online Check image](assets/images/pep8_online.png)

## Technology
### Dev Language Used
- Python

### Application Used
- [GitPod](https://www.gitpod.io/) was used as an online IDE.
- [GitHub](https://github.com/) was used for version control and to save the app online.
- [Heroku](https://dashboard.heroku.com/apps/my-sub-my-way) was used to deploy the site.

### Frameworks Used
- os
- sys
    > os and sys was used to restart the ordering system.
- gspread
    > gspread was used to fetch user information and other details from google spreadsheet.
- google.oauth2.service_account
- Credentials
    > Details of Users were saved in google spreadsheet. 
- time
    > time was used to generate time for every order.
- random
    > random was used to generate a random receipt number.
- prettytable
    > prettytable was used to put all the details in table format.
- art
    > art was used to print the logo of the site.
- colorama
    > colorama was used to add color to text.

## Deployment
Gitpod was used to make this project. I used [Code Institute's Template](https://github.com/Code-Institute-Org/python-essentials-template) for this project

1. Click on [Code Institute's Template](https://github.com/Code-Institute-Org/python-essentials-template) and then click on use this template button.
2. Write the name of the project, select on PUBLIC and click Create Repository from template.
3. Click on the green Gitpod button and gitpod will start loading. Once Gitpod is loaded, you are ready to code.
4. Each time you write and save your code you do the following -
    - git add . 
    - git commit -m "your message"
    - git push

Each term explained below

*.git add*  adds all your last saved codes to your repository.

*git commit -m "your message"* A clear short message explaining the updates.

*git push* To push all the recent changes and make it live on the page.


### Deploying Locally

1. Navigate to the github [Repository](https://github.com/shahid129/my-sub-my-way).

2. Click on the drop down menu CODE.

3. Click on Download Zip and run locally on your machine or copy GIT URL from the HTTPS link.

4. Open your favorite IDE or editor and open the terminal.

5. Change the current working directory to the location where you want the cloned directory.

5. Use the 'git clone' command and paste the copied git URL.

6. Press enter to create clone on your device.

### Deploying the project using Heroku

Before you deploy to heroku, make sure to add the following code in gitpod to add all the requirements and then do a git push, the code is - 

    pip3 freeze --local > requirements.txt

1. Navigate to [heroku](https://www.heroku.com/) and click sign up to create a new account.

2. Click the New button and click Create New APP.

3. Add a name for app in the APP-Name field.

4. Select your region from the drop down menu and click on Create App button.

5. On the next page click on the Settings tab to adjust the settings.

6. Click on the 'config vars' button.

7.  Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

8. Click on the ADD Build button.

9. Add python buildpack and then node.js. The sequence of adding bulidpack has to correct or else it might not work properly.

10. Navigate to deploy screen, select github and connect to your github profile.

11. Now you can deploy the app automatically or manually. Automatic deploy will update the app automatically every time you push any changes to github.

12. Once the build is successful, you can open the app by clicking Open App button in the top right corner.

## Credits

>A lot of help was taken from all over the internet and the main ones are - 
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [FreeCodeCamp](https://www.freecodecamp.org/)

## ACKNOWLEDGEMENT
> I would like to thank my tutor, Kasia, and my mentor Ronan, for their invaluable help and guidance throughout the process. The slack group Jan-2022-lwetb, and all the fellow mates from slack

# THANK YOU
Thanks to my fellow slackers for reviewing my project and a very special thank you to my mentor Ronan, for his invaluable advice and resources throughout the development of this project. SPECIAL THANKS TO MY WIFE FOR BUYING ME ALL THE TIME IN THE WORLD TO DO THE COURSE AND THE PROJECTS.