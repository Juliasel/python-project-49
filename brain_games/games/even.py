import random

MIN_EVEN = 1
MAX_EVEN = 100


def check_parity():

        number = random.randint(MIN_EVEN, MAX_EVEN)
        question = f'Question: {number}'
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        return question, correct_answer 