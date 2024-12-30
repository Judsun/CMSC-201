import os
root, directories, files = next(os.walk('.'))
FROG = '\U0001318F' # the hieroglyphic one

def select_game_file():

    frog_directory = 'C:\\Users\\jayja\\Documents\\Testing\\Homeworks\\project2'
    frogs_list = [f for f in os.listdir(frog_directory) if f[-5:] == '.frog']

    for i in range(len(frogs_list)):
       print(f'[{i+1}] - [{frogs_list[i]}]\n')

    file_choice = list(input("Please enter an option or file name: "))

    for i in range(len(frogs_list)):
       filenum = i + 1
       if str(filenum) in file_choice:
           return open(frogs_list[i], 'r')
    
def frogger_game(game_file):
    pass

# Ask user which file they want to use

# Display the current board (based on the file they use)

# Print the frog at the right location without overwriting the element in the list
    # make a copy of the list and have that list be the position for the frog

# Frog starting position
    # frog starts at len(row)//2 

# check if frog collided with car (position value is the same), print losing message
    # or print winning message at the end and exit

# User input - use WASD and J
    # take upper and lower case
    # if J, the user enters the position based on rows and columns
        # can jump at most one row away but any column
    
# given number of jumps
    # subtract each jump by one
    # if its 0, no more jumping

# Car rotation
    # Rotates the cars from left to right (loops around too)
        #moves in the increments of the speed

if __name__ == '__main__':
   selected_game_file = select_game_file()
   frogger_game(selected_game_file)