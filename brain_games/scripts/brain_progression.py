#!/usr/bin/env python3

from brain_games.game_engine import game_engine
from brain_games.games.brain_progression import make_question, \
    game_task, get_result


def main():
    game_engine(game_task, make_question, get_result)


if __name__ == '__main__':
    main()
