
# Number Guessing Game

## Overview

The Number Guessing Game is an interactive command-line game where players try to guess a randomly generated 4-digit number. The app provides feedback on each guess, tracks the player's score, and stores the best scores in a SQLite database for later comparison.

## Features

- **Random Number Generation**: Generates a unique 4-digit number with no repeated digits.
- **Feedback Mechanism**: Provides hints on how close the player's guess is to the correct number:
  - `+` indicates a correct digit in the correct position.
  - `-` indicates a correct digit in the wrong position.
- **Score Calculation**: Computes a score based on the number of guesses and the time taken.
- **Persistence**: Saves scores to a SQLite database and retrieves the best score for display.
- **User-Friendly Interaction**: Allows players to exit at any point and handles invalid inputs gracefully.

## File Structure

```
.
├── main.py              # Entry point for the game.
├── tests               # Directory containing test cases.
│   └── test_guessing_game.py  # Test cases for the core functionality.
├── game_logic.py        # Handles number generation and evaluation.
├── user_interaction.py  # Manages user input and output.
├── database_manager.py  # Manages the SQLite database for storing scores.
├── test_guessing_game.py # Contains test cases for the core functionality.
├── README.md            # Documentation for the project.
```

## How to Run

### On macOS

1. **Requirements**:

   - [Python 3.x](https://www.python.org/downloads/)
   - SQLite (usually comes pre-installed with Python)

2. **Steps to Run**:

   - Open Terminal.
   - Navigate to the repository where you want to save the project.
   ```
   cd <folder name>
   ```
   - Clone or download the repository.
   ```
   git clone https://github.com/David1izilove/home-assignments-mes
   ```
   - Install the virtual environment.
   ```
   pip install virtualenv
   ```
   - Create a virtual environment in the project directory.
   ```
   cd home-assignments-mes
   virtualenv venv
   ```
   - Activate the virtual environment.
   ```
   source venv/bin/activate
   ```
   - Install project dependencies.
   ```
   pip install -r requirements.txt
   ```
   - Run the following command:
   ```
   python3 main.py
   ```

### On Windows 11

1. **Requirements**:

   - [Python 3.x](https://www.python.org/downloads/)
   - SQLite (usually comes pre-installed with Python)

2. **Steps to Run**:

   - [Download and install git](https://git-scm.com/downloads)
   - Open terminal as admin.
   - Clone or download the repository.
   ```
   git clone https://github.com/David1izilove/home-assignments-mes
   ```
   - Install the virtual environment.
   ```
   pip install virtualenv
   ```
   - Create a virtual environment in the project directory.
   ```
   cd .\home-assignments-mes\
   python -m venv venv
   ```
   - Activate the virtual environment.
   ```
   .\venv\Scripts\activate
   ```
   - Install project dependencies.
   ```
   pip install -r .\requirements.txt
   ```
   - Run the following command:
   ```
   python main.py
   ```

## Gameplay Instructions

1. Launch the game by running the appropriate command for your operating system (see "How to Run" above).
2. From the main menu, choose one of the following options:
   - **Play the Game**: Start a new game session where you guess the randomly generated 4-digit number.
   - **View Best Score**: Display the highest score in the database, including the player's name, guesses, time, and score.
   - **View Scores (Latest 10 or All)**: Choose to view either the latest 10 games or all recorded scores in a tabular format.
   - **Quit**: Exit the game.
3. If you choose to play the game:
   - Enter your name to start.
   - Guess the randomly generated 4-digit number.
   - Receive feedback:
     - `+` indicates a correct digit in the correct position.
     - `-` indicates a correct digit in the wrong position.
   - Keep guessing until you match the number or type `quit` to exit.
4. After successfully guessing the number, your score will be calculated based on the number of guesses and time taken.
5. Your score will be saved in the database, and you can compare it with others using the "View Scores" option.

## Database

The app uses a SQLite database (`game_scores.db`) to store player scores. It maintains the following columns:

- `id`: Primary key.
- `name`: Player's name.
- `guesses`: Number of guesses made.
- `time_taken`: Time taken to guess the number.
- `score`: Calculated score.

## Score Calculation

The score is calculated as:

```
score = 10000 / (guesses * time_taken)
```
This formula rewards faster solutions with fewer guesses.

## Best Score Display

After a successful game, the app displays:

- The player's score and game statistics.
- The best score recorded in the database, encouraging players to beat the top score.

## Testing

The project includes a suite of tests to ensure the core functionalities work as expected. The tests cover:

- Random number generation (`generate_number`).
- Guess evaluation (`evaluate_guess`).
- Score calculation (`calculate_score`).

### How to Run Tests

1. Ensure you have `pytest` installed. If not, install it using:
   ```
   pip install pytest
   ```

2. Run the tests using the following command:
   ```
   pytest tests/test_guessing_game.py
   ```

3. Review the output to confirm all tests pass.


## Troubleshooting

### **Problem 1**:

If you encounter issues activating the virtual environment on Windows 11, you might need to set the execution policy. Run the following command in PowerShell:
```
Set-ExecutionPolicy RemoteSigned
```


## Contact

If you have any problem with the game, please contact me.