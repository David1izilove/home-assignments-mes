
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

   - [Python 3.x]((https://www.python.org/downloads/))
   - SQLite (usually comes pre-installed with Python)

2. **Steps to Run**:

   - Open Terminal.
   - Navigate to the repository where you want to save the project.
   ```
   cd <folder name>
   ```
   - Clone or download the repository.
   ```
   git clone
   ```
   - Install the virtual environment.
   ```
   pip install virtualenv
   ```
   - Create a virtual environment in the project directory.
   ```
   cd 
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

### On Windows

1. **Requirements**:

   - [Python 3.x]((https://www.python.org/downloads/))
   - SQLite (usually comes pre-installed with Python)

2. **Steps to Run**:

   - Open Command Prompt.
   - Clone or download the repository.
   - Navigate to the project directory using `cd`.
   - Run the following command:
      ```
      python main.py
      ```

## Gameplay Instructions

- Enter your name to start the game.
- Guess the randomly generated 4-digit number.
- Receive feedback (`+` for correct position, `-` for correct digit but wrong position).
- Continue guessing until you match the correct number.
- Exit anytime by typing `quit`.

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


## Contact

If you have any problem with the game, please contact me.
