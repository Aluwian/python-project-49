import random

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_yes_no(value):
    return 'yes' if value else 'no'


def make_number_result(func):
    number = random.randint(1, 100)
    result = get_yes_no(func(number))
    return number, result


def make_even():
    return make_number_result(is_even)
