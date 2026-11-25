from brain_games.cli import welcome_user
from brain_games.even import check_parity
from brain_games.greet import greet


def main():
    greet()
    name = welcome_user()
    check_parity(name)
   

if __name__ == '__main__':
    main()

