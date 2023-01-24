import random
from math import gcd


game_task = 'Find the greatest common divisor of given numbers.'


def make_gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question_gcd = f'{num1} {num2}'
    result_gcd = gcd(num1, num2)
    return question_gcd, str(result_gcd)
