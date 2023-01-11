#!/usr/bin/env python3


import random
import prompt
from brain_games import cli


def brain_calc():
    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = ['+', '-', '*']
        op = random.choice(operator)
        result = f'{num1} {op} {num2}'
        print(f'Question: {result}')
        answer = prompt.string('Your answer: ')
        if op == '+':
            result = num1 + num2
            if int(answer) == result:
                print('Correct!')
            else:
                print(f''''{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {cli.name}!''')
                quit()
        if op == '-':
            result = num1 - num2
            if int(answer) == result:
                print('Correct!')
            else:
                print(f''''{answer}' is wrong answer ;(. Correct answer was '{result}'
Let's try again, {cli.name}!''')
                quit()
        if op == '*':
            result = num1 * num2
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
    print('What is the result of the expression?')
    brain_calc()


if __name__ == '__main__':
    main()
