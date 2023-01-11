#!/usr/bin/env python3

from brain_games import cli
import prompt
import random


def brain_even():
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print(f''''{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {cli.name}!''')
                quit()
        if number % 2 != 0:
            if answer == 'no':
                print('Correct!')
            else:
                print(f''''{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {cli.name}!''')
                quit()
        i += 1
    print(f'Congratulations, {cli.name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even()


if __name__ == '__main__':
    main()
