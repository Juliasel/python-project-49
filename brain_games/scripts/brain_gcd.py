from brain_games.engine.utils import run_game
from brain_games.games.gcd import find_gcd

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def main():

    run_game(
        rule=GAME_RULE,
        game_logic=find_gcd
    )


if __name__ == '__main__':
    main()