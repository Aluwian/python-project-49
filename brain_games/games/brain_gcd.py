import random
from math import gcd


game_task = 'Find the greatest common divisor of given numbers.'


def make_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    string_gcd = f'{num1} {num2}'
    return (string_gcd, string_gcd)


def get_result(string):
    num1 = int(string.split(' ')[0])
    num2 = int(string.split(' ')[1])
    result = gcd(num1, num2)
    return str(result)
