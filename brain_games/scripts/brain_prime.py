#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.brain_prime import make_prime, game_task


def main():
    game_engine(game_task, make_prime)


if __name__ == '__main__':
    main()
