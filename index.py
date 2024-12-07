# 1 the game shuld allowd player to choose rock paper or scisors
# 2 the computer shuld randoming selec choice rock paper or scisors
# 3 the game shuld determin the winner and annuncing the winner based on the rules

import random

def player():
    from InquirerPy import prompt #use InquirerPy to improve the user experience with the interface
    choices = [
        {
            "type": "list",
            "message": "Choose",
            "choices": ["rock", "paper", "scisors"]
        },
    ]
    return prompt(choices)

choices_list = ["rock", "paper", "scisors"]

def computer(choices_list):
    computer_choice = random.choice(choices_list)
    return computer_choice


y = computer(choices_list)
x = player()

def verify_winner(x,y):
    if x == {0: 'paper'} and y == 'paper':
        result = 'draw'
        return result
    elif x == {0: 'scisors'} and y == 'scisors':
        result = 'draw'
        return result
    elif x == {0: 'rock'} and y == 'rock':
        result = 'draw'
        return result
    elif x == {0: 'rock'} and y == 'paper':
        result = 'looser'
        return result
    elif x == {0: 'paper'} and y == 'rock':
        result = 'winner'
        return result
    elif x == {0: 'scisors'} and y == 'rock':
        result = 'looser'
        return result
    elif x == {0: 'scisors'} and y == 'paper':
        result = 'winner'
        return result
    elif x == {0: 'paper'} and y == 'scisors':
        result = 'looser'
        return result
    elif x == {0: 'rock'} and y == 'scisors':
        result = 'winner'
        return result
print(verify_winner(x,y))