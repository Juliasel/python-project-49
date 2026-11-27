from engine.utils import run_game
from games.even import check_parity

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

def main():

    run_game(
        rule=GAME_RULE,
        game_logic=check_parity
    )

if __name__ == '__main__':
    main()