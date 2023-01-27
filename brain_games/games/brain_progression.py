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


def run_game():
    list_progression = make_progression()
    symbol = random.randint(0, 9)
    lost_number = str(list_progression[symbol])
    list_progression[symbol] = '..'
    question = " ".join((map(str, list_progression)))
    return question, lost_number
