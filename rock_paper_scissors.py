import random 
import os
os.system('cls')

def welcome_massage():
    print('Welcome to this game.')
    print('Thanks for choice us. ')
    print('Please start the game.')
    print('-'*35)

def input_user_correct():
    while True:
        user_input =input("Select between from paper , rock, scissors(p, r, s) : ")
        if user_input.lower() in ['r', 'p', 's']:
            return user_input
        print('Pleas enter from between (r, p, s)! ')
        print('-'*35)

def ai_random_choice():
    choices =['r', 'p', 's']
    ai_choice= random.choice(choices)
    return ai_choice


def user_time():
    while True:
        user_input= input('How many time you wants choices? ')
        if user_input.isdigit():
            return int(user_input)
        print('Pleas enter a correct number.')
        print('Please try again.')
        print('-'*35)


def start_game():
    use_score=0
    ai_score=0
    time= user_time()
    for i in range(time):
        user_choice=input_user_correct()
        ai_choice=ai_random_choice()
        if user_choice=='s'and ai_choice=='p':
            use_score+=1
            print('You given 1 mark!')
            print('-'*35)
        if user_choice=='p'and ai_choice=='r':
            use_score+=1
            print('You given 1 mark!')
            print('-'*35)
        if user_choice=='r'and ai_choice=='s':
            use_score+=1
            print('You given 1 mark!')
            print('-'*35)
        elif ai_choice==user_choice:
            print('Equal')
            print('-'*35)
        else:
            ai_score+=1
            print('ai given 1 mark!')
            print('-'*35)
    return ai_score, use_score


def how_one_owner():
    ai_score, user_score=start_game()
    if user_score >ai_score:
        print('You Won!')
        print(f'ai score is {ai_score} user score is {user_score}')
    elif user_score== ai_score:
        print('Equal')
        print(f'ai score is {ai_score} user score is {user_score}')
    else:
        print('You Lost.Sorry')
        print(f'ai score is {ai_score} user score is {user_score}')


welcome_massage()
how_one_owner()