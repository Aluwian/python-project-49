import random

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def run_game():
    number_even = random.randint(1, 100)
    result_even = 'yes' if is_even(number_even) else 'no'
    return number_even, result_even
