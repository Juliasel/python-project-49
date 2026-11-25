from brain_games.cli import welcome_user
from brain_games.greet import greet
from brain_games.even import check_parity

def main():
    greet()
    welcome_user()
    check_parity()

if __name__ == '__main__':
    main()

