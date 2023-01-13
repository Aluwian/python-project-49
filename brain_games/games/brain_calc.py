import random

game_task = 'What is the result of the expression?'


def game_run():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = ['+', '-', '*']
    op = random.choice(operator)
    result = f'{num1} {op} {num2}'
    print(f'Question: {result}')
    if op == '+':
        result = num1 + num2
    if op == '-':
        result = num1 - num2
    if op == '*':
        result = num1 * num2
    return str(result)
