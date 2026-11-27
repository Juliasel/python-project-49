from engine.utils import run_game
from games.calculator import calc_example

GAME_RULE = 'What is the result of the expression?'

def main():
    run_game(GAME_RULE, calc_example)
   

if __name__ == '__main__':
    main()