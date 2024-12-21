import random


def generate_number():
    """Generate a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))


def evaluate_guess(computer_number, user_guess):
    """Evaluate the user's guess and provide feedback in a simple way."""
    feedback = []

    computer_number = str(computer_number)
    user_guess = str(user_guess)

    # Check for correct digits in the correct position
    for i in range(len(user_guess)):
        if user_guess[i] == computer_number[i]:
            feedback.append('+')

    # Check for correct digits in the wrong position
    for i in range(len(user_guess)):
        if user_guess[i] in computer_number and user_guess[i] != computer_number[i]:
            feedback.append('-')

    return ''.join(feedback)


def calculate_score(guesses, time_taken):
    """Calculate score based on number of guesses and time taken."""
    return 10000 / (guesses * time_taken)
