import random


game_task = 'What number is missing in the progression?'


def progression():
    items = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    i = 0
    while i < 10:
        start += step
        items.append(start)
        i += 1
    return items


def game_run():
    progression_full = progression()
    symbol = random.randint(0, 9)
    result = progression_full[symbol]
    progression_full[symbol] = '..'
    print('Question: ' + " ".join(map(str, progression_full)))
    return str(result)
