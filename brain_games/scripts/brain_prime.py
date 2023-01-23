#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.brain_prime import get_result, make_question, game_task


def main():
    game_engine(game_task, make_question, get_result)


if __name__ == '__main__':
    main()
