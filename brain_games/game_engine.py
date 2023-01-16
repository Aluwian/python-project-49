import prompt


def greating():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    if name != " ":
        print(f'Hello, {name}!')


def game_engine(game_task, game_run):
    greating()
    welcome_user()
    print(game_task)
    i = 0
    while i < 3:
        result = game_run()
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
