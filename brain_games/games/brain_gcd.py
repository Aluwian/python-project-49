import random
from math import gcd


game_task = 'Find the greatest common divisor of given numbers.'


def game_run():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Question: {num1}, {num2}')
    result = gcd(num1, num2)
    return str(result)
