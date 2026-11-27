import random

MIN_EVEN = 1
MAX_EVEN = 100

def calc_example(name):
        
        number1 = random.randint(MIN_EVEN, MAX_EVEN)
        number2 = random.randint(MIN_EVEN, MAX_EVEN)
        operations = random.choice(['+', '-', '*'])

        question = f'Question: {number1} {operations} {number2}'

        if operations == '+': 
            correct_answer = str(number1 + number2)
        elif operations == '-':
            correct_answer = str(number1 - number2)
        else:
            correct_answer = str(number1 * number2)
        return question, correct_answer
