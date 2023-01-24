import random
import operator

game_task = 'What is the result of the expression?'


def return_operation(num1, num2, symbol):
    if symbol == '+':
        return operator.add(num1, num2)
    if symbol == '-':
        return operator.sub(num1, num2)
    if symbol == '*':
        return operator.mul(num1, num2)


def make_calc():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    symbol = ['+', '-', '*']
    op = random.choice(symbol)
    algorithm = f'{num1} {op} {num2}'
    result = return_operation(num1, num2, op)
    return algorithm, str(result)
