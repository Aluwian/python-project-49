#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt
import random


def brain_even():
    number = random.randint(0, 10)
    i = 0
    while i < 4:
        answer = prompt.string(f'Question: {number}')
        print(f'Your answer: {answer}')
        if number / 0 == 0 and

        i += 1


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')



if __name__ == '__main__':
    main()
