from game_logic import generate_number, evaluate_guess
from database_manager import create_database
from user_interaction import get_user_guess, display_feedback, handle_success
import time


def play_game():
    """
    Main function to run the number guessing game.
    Steps:
    1. Initializes the database.
    2. Welcomes the player and gets their name.
    3. Generates a random number for the player to guess.
    4. Continuously prompts the player for guesses until they succeed or exit.
    5. Tracks the number of guesses and elapsed time to compute the score.
    """
    create_database()
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        print("You have exited the game. Goodbye!")
        return

    computer_number = generate_number()
    print("A 4-digit number has been generated. Try to guess it!")

    start_time = time.time()
    guesses = 0

    while True:
        user_guess = get_user_guess()
        if user_guess == 'quit':
            print("You have exited the game. Goodbye!")
            return
        guesses += 1
        feedback = evaluate_guess(computer_number, user_guess)
        display_feedback(feedback)

        if feedback == '++++':
            handle_success(name, guesses, start_time)
            return


if __name__ == "__main__":
    play_game()
