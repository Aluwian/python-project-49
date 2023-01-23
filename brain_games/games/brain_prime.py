import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number_prime = random.randint(1, 100)
    return (number_prime, number_prime)


def verify_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_result(result):
    return 'yes' if verify_prime(result) is True else 'no'
