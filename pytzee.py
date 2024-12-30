"""                                                                                     
File: pytzee.py                                                                     
Author: Judson Asomani                                                                  
Date: 10/31/2024                                                                          
Section: 11                                                                             
E-mail: judsona1@umbc.edu                                                               
Description:  For every round, 
    displays the round number, then the current score.
    Then rolls the dice 
    ask the user for input on how the dice roll should be counted, Dependant on the way of counting, displays a custom message.
    Displays the scorecard of how many points for each number has been recieved so far
    Then displays the special instance options and how many points were awarded to each option                                                                          
                                                                                        
"""

import random

TOTAL_DICE = 5
DICE_FACES = 6
round = 0
my_score = 0
updated_score = 0

# Your constants should go here.  


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list



# Your additional functions should go here.
def count_dice():
    dice_values = roll_dice()
    amount_of_ones = 0
    amount_of_twos = 0
    amount_of_threes = 0
    amount_of_fours = 0
    amount_of_fives = 0
    amount_of_sixes = 0
    for number in dice_values:
        if number == 1:
            amount_of_ones += 1
        elif number == 2:
            amount_of_twos += 1
        elif number == 3:
            amount_of_threes += 1
        elif number == 4:
            amount_of_fours += 1
        elif number == 5:
            amount_of_fives += 1
        elif number == 6:
            amount_of_sixes += 1
       
    return amount_of_ones, amount_of_twos, amount_of_threes, amount_of_fours, amount_of_fives, amount_of_sixes

def display_score():
    updated_score = 0
    if round >= 2:
        updated_score = check_score()
    return updated_score

def check_score():
    global my_score
    counting_type = input('How would you like to count this dice roll? ')
    if counting_type.lower() == 'three of a kind':
        print('Three of a Kind!')
        my_score = my_score + 30
    elif counting_type.lower() == 'four of a kind':
        print('Four of a Kind!')
    elif counting_type.lower() == 'full house':
        print('Full House! 25 points gained.')
    elif counting_type.lower() == 'small straight':
        print('There was a small straight and you gained 30 points')
    elif counting_type.lower() == 'large straight':
        print('There was a large straight and you gained 40 points')
    elif counting_type.lower() == 'pytzee':
        print('PYTZEE')
    elif counting_type.lower() == 'chance':
        print('Added the dice faces for chance')
    elif counting_type.lower() == 'count 1':
        print("Accepted the 1")
    elif counting_type.lower() == 'count 2':
        print("Accepted the 2")
    elif counting_type.lower() == 'count 3':
        print("Accepted the 3")  
    elif counting_type.lower() == 'count 4':
        print("Accepted the 4")
    elif counting_type.lower() == 'count 5':
        print("Accepted the 5")
    elif counting_type.lower() == 'count 6':
        print("Accepted the 6")
    elif counting_type.lower() == 'skip':
        pass


def play_game(num_rounds):
    """
    For every round, 
    displays the round number, then the current score.
    Then rolls the dice, displays the dice face that were rolled
    ask the user for input on how the dice roll should be counted, Dependant on the way of counting, displays a custom message.
    Displays the scorecard of how many points for each number has been recieved so far
    Then displays the special instance options and how many points were awarded to each option
    """
    for i in range(num_rounds):
        round = i+1
        print('***** Beginning Round ', round, ' *****')
        print('      Your score is: ', display_score())
        print('Your dice rolled are: ', count_dice())
        check_score()
        


if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)