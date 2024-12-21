import time
from game_logic import calculate_score
from database_manager import save_score, get_best_score


def get_user_guess():
    """Prompt the user to enter a valid 4-digit guess or exit the game.."""
    while True:
        user_guess = input("Enter your 4-digit guess (or type 'quit' to exit): ")
        if user_guess.lower() == 'quit':
            return 'quit'
        elif len(user_guess) == 4 and user_guess.isdigit():
            return user_guess
        else:
            print("Invalid input. Please enter exactly 4 digits or type 'quit' to exit.")


def display_feedback(feedback):
    """Display feedback for the user's guess."""
    print(f"Feedback: {feedback}")


def handle_success(name, guesses, start_time):
    """Handle actions after the user successfully guesses the number."""
    end_time = time.time()
    time_taken = end_time - start_time
    score = calculate_score(guesses, time_taken)
    save_score(name, guesses, time_taken, score)
    print(f"Congratulations, {name}! You guessed the number in {guesses} guesses and {time_taken:.2f} seconds.")
    best = get_best_score()
    if best:
        print(f"Best score: {best[0]} - Guesses: {best[1]}, Time: {best[2]:.2f}s, Score: {best[3]:.2f}")
