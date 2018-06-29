# Single Player Battleship
# Used codeacademy to learn it
# Will include a 5 X 5 grid and 3 guesses to tank the ship
from random import randint

from Tools.scripts.treesync import raw_input

print("Welcome to Battleship")
print("Find the ships and sink it")
playing_field = []

# Creating the grid called playing field
for i in range(0, 5):
    playing_field.append(["0"]*5)


# The playing filed consists of all the 25 zeroes in one line
# Fixing it
def new_playing_field(playing_field_arg):
    for each_row in playing_field_arg:
        print(" ".join(each_row))


# Printing the board for the user to see
new_playing_field(playing_field)


# To always have a new location for the hidden battleship using RANDOM to get new row and column
def random_row(playing_field_arg):
    return randint(0, len(playing_field_arg) - 1)


def random_col(playing_field_arg):
    return randint(0, len(playing_field_arg[0]) - 1)


ship_row = random_row(playing_field)
ship_col = random_col(playing_field)

# Looping for each guess
for guess in range(0, 3):
    new_guess = guess + 1
    print("Guess no.: ", new_guess)

    # Asking the user to input his choice row and column
    users_guess_row = int(raw_input("Guess Row: "))
    users_guess_col = int(raw_input("Guess Col: "))
    guess_row = users_guess_row - 1
    guess_col = users_guess_col - 1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif playing_field[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            playing_field[guess_row][guess_col] = "X"
        new_playing_field(playing_field)
        if guess == 2:
            print("Game Over")
            print("You lost")
            playing_field[ship_row][ship_col] = "B"
            new_playing_field(playing_field)