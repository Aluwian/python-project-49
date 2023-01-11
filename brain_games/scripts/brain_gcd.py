#!/usr/bin/env python3


import random
import prompt
from math import gcd
from brain_games import cli


def brain_gcd():
    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question:{num1}, {num2}')
        result = gcd(num1, num2)
        answer = prompt.string('Your answer: ')
        if int(answer) == result:
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {cli.name}!''')
            quit()
        i += 1
    print(f'Congratulations, {cli.name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    brain_gcd()


if __name__ == '__main__':
    main()
