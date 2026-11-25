import random
import prompt
from brain_games.cli import welcome_user

def check_parity():


    print('Answer "yes" if the number is even, otherwise answer "no".')


    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print("Let's try again", welcome_user())
            return
        
    print('Congratulations, welcome_user()!')
    