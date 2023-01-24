import prompt


CYCLE_COUNT = 3


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(game_task, make_question):
    greet()
    name = welcome_user()
    print(game_task)
    i = 0
    while i < CYCLE_COUNT:
        (question, result) = make_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'"
                  f"\nLet's try again, {name}!")
            quit()
        i += 1
    print(f'Congratulations, {name}!')
