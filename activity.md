## Instructions

Make sure Python is installed on your computer.

### 1. Install Pygame

You need to install the `pygame` library before running the game.

Open your terminal or command prompt and run:

```bash
pip install pygame
```

2. Fork the Snake Game Repository
   • Go to the repository link your Lecturer provided: https://github.com/Robbo-lab/snake-game.git
   • Click the “Fork” button in the top-right corner
   • This creates a copy of the repository under your **own GitHub account**

3. Clone Your Fork

Open your terminal or Git Bash and run the following:

```bash
git clone https://github.com/YOUR-USERNAME/basic-snake-game.git
cd basic-snake-game
```

Replace YOUR-USERNAME with your GitHub username.

4. Run the Snake Game

In the project folder, run the game to make sure it works:

```bash
python snake_game.py
```

If the game runs, you are ready to continue.

5. Create a New Branch

Create and switch to a new branch called change-snake-speed:

```bash
git checkout -b change-snake-speed
```

6. Make a Change

Open the file snake_game.py in a code editor.

Make one small change to the game. Some examples:
• Change FPS = 12 to a different speed
• Change the color of the snake or food
• Change how many points you earn per food

Save the file when finished.

7. Add and Commit Your Changes

Stage your changes and create a commit:

```bash
git add snake_game.py
git commit -m "Changed snake speed from 12 to 18 FPS"
```

8. Push the Branch to GitHub

Send your branch to your GitHub repository:

```bash
git push origin change-snake-speed
```

9. Optional: Create a Pull Request
   • Go to your GitHub repository in your browser
   • You will see a button that says “Compare & pull request”
   • Click it to suggest your changes to the main project

10. Optional: Pull Updates from the Lecturer’s Repository

If the Lecturer updates the original repository and you want those updates, you can run:

```bash
git remote add upstream https://github.com/Robbo-lab/snake-game.git
git pull upstream main
```

## Optional Challenges

If you finish early, try one or more of the following **but make a branch for each change**.

1. Change the snake’s color
2. Change the scoring system
3. Rename the file snake_game.py to something else

## Reflection - did you manage to do all of these?

• Installed pygame
• Forked the repository
• Cloned the repository to my computer
• Created a new branch
• Made a change to the code
• Committed my change
• Pushed my branch to GitHub
• (Optional) Opened a pull request
