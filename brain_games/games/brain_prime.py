import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def make_prime():
    number_prime = random.randint(1, 100)
    result_prime = 'yes' if is_prime(number_prime) is True else 'no'
    return number_prime, result_prime
