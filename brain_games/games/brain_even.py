import random
from brain_games.utils import get_yes_no


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def make_even():
    number_even = random.randint(1, 100)
    result_even = get_yes_no(is_even(number_even))
    return number_even, result_even
