import random
import operator

game_task = 'What is the result of the expression?'


def make_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    symbol = ['+', '-', '*']
    op = random.choice(symbol)
    algorithm = f'{num1} {op} {num2}'
    return (algorithm, algorithm)


def return_operation(num1, num2, symbol):
    if symbol == '+':
        return operator.add(num1, num2)
    if symbol == '-':
        return operator.sub(num1, num2)
    if symbol == '*':
        return operator.mul(num1, num2)


def get_result(string):
    num1 = int(string.split(' ')[0])
    num2 = int(string.split(' ')[2])
    symbol = string.split(' ')[1]
    result = return_operation(num1, num2, symbol)
    return str(result)
