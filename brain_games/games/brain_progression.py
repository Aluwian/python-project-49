import random


game_task = 'What number is missing in the progression?'


def make_progression():
    items = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    i = 0
    while i < 10:
        start += step
        items.append(start)
        i += 1
    return items


def make_question():
    list_progression = make_progression()
    symbol = random.randint(0, 9)
    lost_number = list_progression[symbol]
    list_progression[symbol] = '..'
    result = " ".join((map(str, list_progression)))
    return (result, lost_number)


def get_result(question):
    return str(question)
