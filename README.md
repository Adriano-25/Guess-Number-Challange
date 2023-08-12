# Guess Number Challenge

## Introduction

Welcome to Guess Number Challenge, an engaging Python game that challenges your guessing skills! Take on the CPU as you try to uncover the secret number within a limited number of attempts.

![main-image](assets/images/FireShot%20Capture%20027%20-%20Multi%20Device%20Website%20Mockup%20Generator%20-%20techsini.com.png)
## Overview

Guess Number Challenge is a command-line-based game where players strive to guess a randomly generated secret number. The game provides "Warm" and "Cold" hints to guide your guesses. Each successful attempt lands you a spot on the leaderboard, so aim high and show off your guessing prowess!

## How to Play

1. **Launch the Game:** Start the Guess Number Challenge by running the provided Python script.

2. **Enter Your Name:** Introduce yourself to the game by entering your name when prompted. Your journey begins!

3. **Make Your Guesses:** A random secret number between 1 and 100 awaits your discovery. Make your guesses and receive hints along the way.

4. **Use Hints Wisely:** The game offers "Warm" hints when you're getting closer and "Cold" hints when you're farther from the secret number.

5. **Reach for Victory:** You have a limited number of attempts to guess the secret number and secure your place on the leaderboard.

6. **Check the Leaderboard:** After each game, your score is recorded on the leaderboard. Curious about your rank? View the leaderboard and find out!

7. **Play Again:** Decide if you're up for another round or want to call it a day. The game is ready for your next challenge!

## Example Gameplay

```plaintext
Welcome to Guess Number Challenge!
Can you guess the secret number?

What's your name? Alice
Welcome, Alice!

Take a guess: 50
Warm!
Take a guess: 70
Cold!
Take a guess: 62
Warm!
Take a guess: 65
Warm!
Take a guess: 64
Congratulations, Alice! You guessed the secret number 64!

Do you want to view the leaderboard? (yes/no): yes
Leaderboard:
Alice: 3 attempts
Bob: 4 attempts
Eve: 5 attempts

Do you want to play again? (yes/no): no
Thank you for playing Guess Number Challenge. Goodbye!


```

### Future Features
 - Allow the player to set the grid size.
 - Enable players to position their ships on the grid.

### Testing
* I have manually tested this project through various scenarios:

- Entered incorrect inputs into the terminal to ensure appropriate warning messages are displayed.
- Ran the project through the terminal during development to verify function behavior.
- Tested the project on Heroku for deployment readiness.

### Bugs
#### Solved Bugs
- Corrected a bug where guessing values of row: 7, col: 7 caused a "value not in range" error. Fixed by adjusting the guessing logic by subtracting 1.
- Rectified the turn counter, which initially started at 0, by adding + 1 to accurately count turns.
- Addressed an issue where the CPU guessed incorrectly, marking the user's board with an X. Fixed by ensuring the code to display an X on the user board appears in the correct order: board cpu_guess_row cpu_guess_col.

### Remaining Bugs
- No bugs remaining

### Ready to play?
- Dive into the exciting world of Guess Number Challenge! Test your guessing skills, outsmart the CPU, and aim for the top spot on the leaderboard. Run the game, make your guesses, and embark on a thrilling journey of numbers and intuition.

## Deployment
I used Heroku to deploy my final project to the cloud. To do this I had to:

1. Push all latest code to GitHub.
2. Go to [Heroku](https://dashboard.heroku.com/apps)
3. Select new in the top right corner.
4. Create new app.
5. Enter the app name and select Europe as the region.
6. Connect to GitHub.
7. Search for repo-name.
8. Select connect to the relevant repo you want to deploy.
9. Select the settings tab.
10. Add buildpack
11. Select Python, then save changes.
12. Select Nodejs, then save changes.
13. Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
14. Navigate to the deploy tab
15. Scroll down to Manual Deploy and select deploy branch.
## End Product

## Credits

- GitHub Python Template [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
- Heroku deployment instructions from Code Institute