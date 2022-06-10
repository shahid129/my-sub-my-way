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

## Credits

>A lot of help was taken from all over the internet and the main ones are - 
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [CSS Tricks](https://css-tricks.com/)
- [Youtube](https://www.youtube.com/)
- [FreeCodeCamp](https://www.freecodecamp.org/)

## ACKNOWLEDGEMENT
> I would like to thank my tutor, Kasia, and my mentor Ronan, for their invaluable help and guidance throughout the process. The slack group Jan-2022-lwetb, and all the fellow mates from slack

# THANK YOU
Thanks to my fellow slackers for reviewing my project and a very special thank you to my mentor Ronan, for his invaluable advice and resources throughout the development of this project. SPECIAL THANKS TO MY WIFE FOR BUYING ME ALL THE TIME IN THE WORLD TO DO THE COURSE AND THE PROJECTS.