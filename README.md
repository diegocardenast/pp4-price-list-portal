# Plastilecor Price List Portal

Plastilecor is a small business without too much digitalization and a B2B line where it becomes handy to provide those distributors with an online price list that they can check anytime with an assigned user's access. Furthermore, if there are any needed modifications from the plastilecor admin, they can be applied online with an admin user and retrieved to all the other users with a valid access.

![Responsive Mockup](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/am-I-responsive-plastilecor-price-list-portal.png)

## User Experience

### User Stories
- As a **user** I want to **understand the game rules** so that I can **play the game correctly**
- As a **user** I want to **view the Game page** so that I can **click and start the game anytime**
- As a **user** I want to **navigate the web app** so that I can **see more information about the game**
- As a **user** I want to **view the Game page** so that I can **click and start the game anytime**
- As a **user** I want to **select the number of questions** so that I can **dedicate the time I have available**
- As a **user** I want to **see my score updating** so that I can **compete with my score**
- As a **user** I want to **see the time limit** so that I can **compete with myself**
- As a **user** I want to **hear the game audio/soundtrack** so that I can **feel the halloween spirit**
- As a **revisitng user** I want to **be able to see my previous score records** so that I can **try to beat it**
- As a **user** I want to **understand the game rules** so that I can **play the game correctly**
- As a **user** I want to **have the options menu available** so that I can **restart the game anytime**
- As a **user** I want to **select the level of difficulty** so that I can **challenge myself with shorter or larger words**
- As a **user** I want to **be able to guess a letter from the game word** so that I can **try several times before it is game over**
- As a **user** I want to **be able to watch the letters that were selected** so that I can **avoid repeating letters**
- As a **user** I want to **be able to watch the hangman image and the number of left tries** so that I can **be more cautious with the following letters selection**


### Tasks and Planning

Tasks and planning can be seen in the [Plastilecor Price List Portal - GitHub Project](https://github.com/users/diegocardenast/projects/3).

### Colour
The colour palette was generated from the company logo: [Plastilecor logo](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/am-I-responsive-plastilecor-price-list-portal.png).


## Wireframes

__Game Start__  

![Game Start](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/wireframeGameStart.png)

__Gameplay__  

![Gameplay1](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/wireframeGameplay1.png)

![Gameplay2](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/wireframeGameplay2.png)



## Features

### Implemented Features

__Sound ON/OFF__

  - The full responsive navigation bar includes links to the Game page, Instructions and Contact page, and is identical in each page to allow for easy navigation. 

![Sound ON/OFF](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/sound-on-off.png)

__Index__

  - The full responsive navigation bar includes links to the Game page, Instructions and Contact page, and is identical in each page to allow for easy navigation. 

![Index](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/index_image.png)

__Art Content__

- Some ghosts were created by the team as well as the team and game logo. 

![Game Logo](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/ghostHuntersLogo.png)

![Ghosts](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/naughty_ghost.png)

__In-game Information__

  - The time counter, the name of the schenario, pumpkins (lives) counter and how many ghosts you have hunt are part of the visual tools for the user/player. 

![inGameInfo](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/gameInfo.png)

__Game Story & Instructions__

  - The descriptions of the characters and how to play. 

![gameStory](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/characters.png)
![Instructions](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/instructions.png)

__Scoreboard__

  - It saves the scores of the players. 

![scoreboard](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/scoreboard.png)

### Features Left to Implement
- Make the game go faster and provide extra points per killed gost
- Add bonus points functionality

## Testing

### Validator Testing
- Python
  - No errors were returned when passing through the official [pep8ci validator](https://pep8ci.herokuapp.com/)  
- JavaScript
  - No errors were returned when passing through the official [JSHint validator](https://jshint.com/)
- HTML
  - One error related to invalid attributes for an img element was returned when passing the first time through the official [W3C validator](https://validator.w3.org/)
  - No errors were returned when passing the second time through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?)
- Lighthouse
  - The result given by the system for the lighthouse assessment is the following:
![Lighthouse results](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/lighthouse-test.png)

### Manual Testing
**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
Index | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Index | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Game | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Game | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Index page test | All phone sizes checked using Chrome Dev Tools | Elements look good | Works at expected
Game page test | All phone sizes checked using Chrome Dev Tools | Elements overlap and game runs faster at lower resolutions | Does not work as expected 



### Unfixed Bugs

- NA

## Deployment 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

- The game code is stored in a GitHub repository and was deployed in the Heroku app. The steps to deploy are as follows: 
  - Update the requirements file by running in the Gitpod terminal "pip3 freeze > requirements.txt"
  - Push the latest changes to the GitHub repository 
  - Inside the Heroku account, create a new app with a unique name
  - Inside the Heroku app settings tab, create a _Config Var_ called `PORT`. Set this to `8000`
  - Inside the Heroku app settings tab, add two buildpacks:
    - `heroku/python`
    - `heroku/nodejs`
  - Inside the Heroku app deploy tab, select GitHub as deployment method and connect the GitHub repository to the Heroku app
  - Inside the Heroku app deploy tab, click on deploy branch
  - Click on View App
  - Done!

The live link can be found [HERE](https://hangman-game-diego-dd66cfc0fedc.herokuapp.com/)

The live link can be found [HERE](https://diegocardenast.github.io/CodeBusters/)

--- 

## Credits

### Content 

- Good/Best practice on the readme were shared by Lauren-Nicole Popich in her [mentoring](https://github.com/CluelessBiker/mentoring/tree/main) GitHub repositry
- User Stories and tasks creation was implemented following this [publication](https://boosthigh.com/software-requirements-specification/)
- Use of Google to import [Google fonts](https://fonts.google.com/?classification=Display) 
- Inspiration of our [game color palette](https://tools.picsart.com/color/palette-generator/?colors=D8A56C-2D244C-955637-6C4346-697986-3D5980-394D71-6B89A4) and were based on the selected game background that comes from [themeforest.net](https://themeforest.net/)
- The animation and use of canvas in JavaScript was implemented following this [tutorial](https://youtu.be/GFO_txvwK_c?si=l2RwIYNxn0n712Ew)
- The use of GitHub to collaborate and apply good practices was implemented following this [Slack post](https://code-institute-room.slack.com/archives/C05UQAPDNCT/p1697457705802579) and this [GitHub post](https://github.com/auxfuse/hackathon-git-labs/blob/main/basic.md)
- The [team availability](https://docs.google.com/spreadsheets/d/1dMP_YxtveAuA8vppXYU1i1a0LoCAVq37If_BdVpL-fg/edit?usp=sharing) was organized using [Google sheets](https://www.google.com/sheets/about/)

### Media

- The creation of the team banner and game logo was implemented using [Canva](https://www.canva.com/)
- The wireframes were created using [Balsamiq Cloud](https://balsamiq.cloud/)
- The icons along the web app were taken from [Font Awesome](https://fontawesome.com/)
- The use of the icons was provided by [Flaticon](https://www.flaticon.com/free-icon/planet-earth_1598431?related_id=1598196&origin=search)
- The ghosts own art were created with [Procreate](https://procreate.com/) and [Photoshop](https://www.adobe.com/products/photoshop.html)
- The improvement/change of sprites (sequence of images for animation) were implemented using [GIMP](https://www.gimp.org/)
- The game background music was selected from opengameart.org and created by [Alexandr Zhelanov](https://opengameart.org/content/wtf-ghost)
- The game background image was selected from [themeforest.net](https://themeforest.net/)



Thank You!

Diego Cárdenas 
