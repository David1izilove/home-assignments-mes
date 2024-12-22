from game_logic import generate_number, evaluate_guess
from database_manager import create_database, get_best_score, get_all_scores
from user_interaction import get_user_guess, display_feedback, handle_success
import time


def display_all_scores():
    """
    Fetch and display scores from the database, with an option to view the latest 10 games or all results.
    """
    print("\n--- View Scores ---")
    print("1. View the latest 10 games")
    print("2. View all games")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        scores = get_all_scores(limit=10)
        print("\n--- Latest 10 Games ---")
    elif choice == "2":
        scores = get_all_scores()
        print("\n--- All Games ---")
    else:
        print("Invalid choice. Returning to the main menu.")
        return

    if scores:
        print(f"{'Rank':<5} {'Player':<15} {'Guesses':<10} {'Time (s)':<10} {'Score':<10}")
        print("-" * 50)
        for rank, (name, guesses, time_taken, score) in enumerate(scores, start=1):
            print(f"{rank:<5} {name:<15} {guesses:<10} {time_taken:<10.2f} {score:<10.2f}")
    else:
        print("No scores available yet. Play the game to set a new record!")


def display_best_score():
    """
    Fetch and display the best score from the database.
    """
    best = get_best_score()
    if best:
        print(f"Best score:\n"
              f"Player: {best[0]}\n"
              f"Guesses: {best[1]}\n"
              f"Time Taken: {best[2]:.2f} seconds\n"
              f"Score: {best[3]:.2f}")
    else:
        print("No scores available yet. Play the game to set a new record!")


def play_game():
    """
    Main function to run the number guessing game.
    """
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        print("You have exited the game. Goodbye!")
        return

    computer_number = generate_number()
    print(computer_number)
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


def main_menu():
    """
    Display the main menu and handle user choices.
    """
    create_database()
    while True:
        print("\n--- Number Guessing Game ---")
        print("1. Play the game")
        print("2. View best score")
        print("3. View scores (latest 10 or all)")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            display_best_score()
        elif choice == "3":
            display_all_scores()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()
