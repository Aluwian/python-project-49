from brain_games.games.brain_even import make_number_result


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def make_prime():
    return make_number_result(is_prime)
