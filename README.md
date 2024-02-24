# BATTLESHIPS

Python Essentials Project Portfolio Three - Code Institute_

View deployed site (ADD IN HEROKU DEPLOYED SITE)

ADD PHOTO

## Table of contents

- [User Experience (UX)](#user-experience)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

## Game Instructions 

- The Battleships game, developed in Python, invites players to a strategic duel on an 8x8 grid where the objective is to locate and sink five randomly placed ships within ten turns. Players input row (1-8) and column (A-H) coordinates to fire at the hidden enemy fleet, with hits and misses marked as 'X' and 'O', respectively. The game provides immediate feedback on the outcomes of each guess, promoting strategic thinking and adaptation. Achieving victory requires sinking all enemy ships before exhausting the turn limit, challenging players to demonstrate deductive reasoning and precision. This project encapsulates essential programming concepts and offers a compelling exercise in logic and strategy. 

## Demographic 

- The Battleships game was designed with simplicity and ease of use in mind, catering to individuals who may not be particularly confident with technology but still harbor an interest in enjoying a classic game experience. This demographic encompasses a wide range of users, including those who may be new to digital gaming or prefer straightforward interfaces. By prioritizing accessibility and user-friendliness, the game aims to provide an inviting platform for anyone interested in trying their hand at Battleships without feeling overwhelmed by complex mechanics or technical barriers. Whether it's seasoned players looking for a quick and intuitive gaming session or newcomers eager to explore the world of digital entertainment, the Battleships game offers an inclusive and enjoyable experience for all. 

## Purpose 

- The purpose of creating this Python-based Battleships game was to demonstrate the practical application of Python programming within a project. By developing a classic game like Battleships using Python, the aim was to showcase the versatility and functionality of the language in real-world scenarios. This project serves as a tangible example of Python's capability to create interactive and engaging software, highlighting its suitability for both beginners and experienced programmers alike. Through the implementation of game logic, user interfaces, and various functionalities, the Battleships game underscores Python's adaptability and effectiveness in project development. Additionally, by sharing this game with others, the intention is to inspire and encourage individuals to explore Python as a valuable tool for bringing their ideas to life in the realm of software development. 

## Features 

### Existing Features

- Dynamic grid-based naval warfare simulation 

= Random placement of five ships at the start 

- User-friendly interface with error handling for invalid inputs 

- Limited ten turns for strategic planning and precise targeting 

- Clear feedback and congratulatory messages for successful hits 

- Intuitive display of player's and opponent's grids after each turn 

= Warm welcome message at the start sets the tone for immersive gameplay


<details>

ADD IN PHOTOS 

</details>

### Features, which I would like to implement in the future

- If I had more time on this I would of added an achievements and Leaderboards. This would Introduce achievements and online leaderboard which would hopefully incentivize players and foster competition 


## Data Model 

- I crafted this application utilizing Python 3. Every line of code was meticulously crafted within a virtual environment (venv) directly within Visual Studio Code. Once perfected, the code was seamlessly uploaded to GitHub and swiftly deployed onto Heroku, showcasing a seamless integration of cutting-edge technology for a smooth user experience. 

## Testing

### PEP8

- In the development of the project, I adhered to coding standards by utilizing Pep8 (https://pep8ci.herokuapp.com/) for maintaining code quality and consistency. While the tool did highlight some issues, these were predominantly related to whitespace and instances where lines exceeded the recommended length. It's important to note that the lines identified as too long were intentionally kept that way. Altering their length would have negatively impacted the functionality of the code, as certain commands and structures required specific formatting to operate correctly. 

## Deployment N

- Github 

- The website was developed using the Visual Studio Code editor and subsequently uploaded to a GitHub remote repository located at: https://github.com/Izzo2le/Battleshipsnew.git 

- During the development process, the following Git commands were employed to manage and update the code in the remote repository: 

1) git add .: This command added files to the staging area, preparing them for the next phase of the process. 

2) git commit -m "commit message...": This step involved committing the staged changes to the local repository, marking them as ready for the final push. 

3) git push: Finally, this command transferred all the committed code from the local repository to the GitHub remote repository 

- Heroku 

1) tart by visiting Heroku and selecting "New" to initiate a new app creation. 

2) Determine and set your app's name and region (There is an option of either United States or Europe), then proceed by clicking "Create app". 

3) In the "Settings" section, locate and move to Config Vars. Here, input the following configuration variables: PORT: 8000 

4) Proceed to the Buildpacks section and incorporate buildpacks for both Python and NodeJS, ensuring they are added in the specified sequence. 

5) Switch over to the "Deploy" tab. Opt for GitHub as the deployment method, then search for and link your repository. 

6) Scroll to the Manual Deploy section, choose the "main" branch, and initiate the deployment by clicking on "Deploy Branch". 

7) After waiting briefly, the application will be successfully deployed on Heroku. 

8) To view and interact with your app, simply click on "View". 

## Credits

- I used a few youtube videos from Youtube to help me set up my game board ( https://www.youtube.com/watch?v=tF1WRCrd_HQ  & https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i )


### Acknowledgments

- The Heroku Python template was provided by Code Institute. 

- A massibe thankyou to Richard Wells, id definitely of left the course without him! – my course tutor 

- I used Slack with my code institute account  

- A massive thank you to Paul Wroe - a code tutor in Brighton for the assistance in understanding python further.

**This is for educational use.**