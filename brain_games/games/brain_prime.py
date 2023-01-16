import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_run():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    for i in range(2, number):
        if number % i == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    return result
