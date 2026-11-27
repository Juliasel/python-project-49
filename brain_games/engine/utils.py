import prompt

def welcome_user():

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def get_user_answer():
    qeustion = prompt.string('Your answer: ')
    return qeustion

def show_wrong_user(user_answer, correct_answer):

    name = welcome_user()
    print(
        f'"{user_answer}" is wrong answer ;(.'
        f'Correct answer was "{correct_answer}".'
    )
    print(f"Let's try again, {name}")

def congrat(name):
    print(f'Congratulations, {name}!')

def run_game(rule:str, game_logic: callable):
    name = welcome_user()
    print(rule)

    for _ in range(3):
        question, correct_answer = game_logic()
        user_answer = get_user_answer(question)
        if user_answer == correct_answer:
            print('Correct!')
        else:
            show_wrong_user(user_answer, correct_answer)
            return
    congrat(name)
