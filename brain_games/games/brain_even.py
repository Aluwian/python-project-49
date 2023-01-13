import random


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_run():
    number = random.randint(1, 100)
    result = ""
    print(f'Question: {number}')
    if number % 2 == 0:
        result = 'yes'
    elif number % 2 != 0:
        result = 'no'
    return result
