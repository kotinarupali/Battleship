# Two Player Battleship
# Used codeacademy to learn it
# Will include a 5 X 5 grid and 3 guesses to tank the ship
import os

from Tools.scripts.treesync import raw_input

print("Welcome to Battleship")
print("Find the ships and sink it")
playing_field_one = []
playing_field_two = []
playing_field_player_one = []
playing_field_player_two = []

# Creating the grid called playing field
for i in range(0, 5):
    playing_field_one.append(["0"] * 5)
    playing_field_two.append(["0"] * 5)
    playing_field_player_one.append(["0"] * 5)
    playing_field_player_two.append(["0"] * 5)


# The playing filed consists of all the 25 zeroes in one line
# Fixing it
def new_playing_field(playing_field_arg):
    for each_row in playing_field_arg:
        print(" ".join(each_row))


# Clearing the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Input names of two players
player_one = str(raw_input("Player 1's name: "))
player_two = str(raw_input("Player 2's name: "))

# Clearing the screen for placements
clear_screen()

# Player one will put in his two battle ships
print("Player one enter your battleship placements: ")
new_playing_field(playing_field_player_one)

for placement in range(0, 2):
    new_guess_player_one = placement + 1
    print("Placement:", new_guess_player_one)

    # Asking the user to input his choice row and column
    users_guess_row = int(raw_input("Guess Row: "))
    users_guess_col = int(raw_input("Guess Col: "))
    guess_row = users_guess_row - 1
    guess_col = users_guess_col - 1
    playing_field_player_one[guess_row][guess_col] = "B"
    new_playing_field(playing_field_player_one)

# Clearing the screen for player 1
clear_screen()

# Player two will put in his two battle ships
print("Player Two enter your battleship placements: ")
new_playing_field(playing_field_player_two)

for placement in range(0, 2):
    new_guess_player_two = placement + 1
    print("Placement:", new_guess_player_two)

    # Asking the user to input his choice row and column
    users_guess_row = int(raw_input("Guess Row: "))
    users_guess_col = int(raw_input("Guess Col: "))
    guess_row = users_guess_row - 1
    guess_col = users_guess_col - 1
    playing_field_player_two[guess_row][guess_col] = "B"
    new_playing_field(playing_field_player_two)

# Clearing the screen for player 1
clear_screen()

# Player one now guesses for player two
# Each player gets three guesses to find at least one battleship
print("Player one Make your guesses!")
for guess in range(0, 3):
    new_guess = guess + 1
    print("Guess no.: ", new_guess)

    # Asking the user to input his choice row and column
    users_guess_row = int(raw_input("Guess Row: "))
    users_guess_col = int(raw_input("Guess Col: "))
    guess_row = users_guess_row - 1
    guess_col = users_guess_col - 1

    if playing_field_player_two[guess_row][guess_col] == "B":
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")

        elif playing_field_one[guess_row][guess_col] == "X":
            print("You guessed that one already.")

        else:
            playing_field_player_two[guess_row][guess_col] = "X"
            playing_field_one[guess_row][guess_col] = "X"

        new_playing_field(playing_field_one)
        if guess == 2:
            print("Player 1 loses")
            print("Battleship Placements")
            new_playing_field(playing_field_player_two)

# Clearing the screen for player 2
clear_screen()

# Player one now guesses for player two
# Each player gets three guesses to find at least one battleship
print("Player two Make your guesses!")

for guess in range(0, 3):
    new_guess = guess + 1
    print("Guess no.: ", new_guess)

    # Asking the user to input his choice row and column
    users_guess_row = int(raw_input("Guess Row: "))
    users_guess_col = int(raw_input("Guess Col: "))
    guess_row = users_guess_row - 1
    guess_col = users_guess_col - 1

    if playing_field_player_one[guess_row][guess_col] == "B":
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")

        elif playing_field_two[guess_row][guess_col] == "X":
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")
            playing_field_player_one[guess_row][guess_col] = "X"
            playing_field_two[guess_row][guess_col] = "X"

        new_playing_field(playing_field_two)
        if guess == 2:
            print("Player 2 loses")
            print("Battleship placements")
            new_playing_field(playing_field_player_one)