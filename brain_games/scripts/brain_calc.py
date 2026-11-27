from brain_games.engine.utils import run_game
from brain_games.games.calculator import calc_example

GAME_RULE = 'What is the result of the expression?'


def main():
    run_game(
        rule=GAME_RULE,
        game_logic=calc_example
    )
   

if __name__ == '__main__':
    main()