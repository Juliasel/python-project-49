import random

MIN_EVEN = 1
MAX_EVEN = 100

def find_gcd():

    number1 = random.randint(MIN_EVEN, MAX_EVEN)
    number2 = random.randint(MIN_EVEN, MAX_EVEN)

    question = f'Question: {number1} {number2}'

    while number2 != 0:
        number1, number2 = number2, number1 % number2
    correct_answer = str(number1)
    return question, correct_answer
