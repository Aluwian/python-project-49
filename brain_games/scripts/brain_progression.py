#!/usr/bin/env python3

from brain_games.game_engine import game_engine
from brain_games.games.brain_progression import make_question, game_task


def main():
    game_engine(game_task, make_question)


if __name__ == '__main__':
    main()
