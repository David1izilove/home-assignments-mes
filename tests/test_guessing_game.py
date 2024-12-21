import pytest
from game_logic import generate_number, evaluate_guess, calculate_score


def test_generate_number():
    number = generate_number()
    assert len(number) == 4
    assert len(set(number)) == 4
    assert number.isdigit()


@pytest.mark.parametrize("computer_number, user_guess, expected", [
    ("1234", "1234", "++++"),
    ("1234", "4321", "----"),
    ("1234", "1243", "++--"),
    ("1234", "5678", ""),
    ("1234", "1256", "++")
])
def test_evaluate_guess(computer_number, user_guess, expected):
    assert evaluate_guess(computer_number, user_guess) == expected


def test_calculate_score():
    score = calculate_score(10, 20)
    assert score == 50
