#!/usr/bin/env python3

from brain_games.game_engine import run_engine
from brain_games.games.brain_progression import run_game, game_task


def main():
    run_engine(game_task, run_game)


if __name__ == '__main__':
    main()
