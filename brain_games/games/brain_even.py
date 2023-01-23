import random


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number_even = random.randint(1, 100)
    return (number_even, number_even)


def verify_even(number):
    return number % 2 == 0


def get_result(number):
    return 'yes' if verify_even(number) is True else 'no'
