import random
import time

# Define empty spaces on the board with a dictionary
the_board = {
    '1' : ' ',
    '2' : ' ',
    '3' : ' ',
    '4' : ' ',
    '5' : ' ',
    '6' : ' ',
    '7' : ' ',
    '8' : ' ',
    '9' : ' ',
}

# Choose who is X and who is O
character = ["X", "O"]
turns = ["player", "cpu"]

cpu_character = character[random.randint(0, 1)]
character.remove(cpu_character)
player_character = character[0]

# Decide turn order
turn = turns[random.randint(0, 1)]


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def win_condition_check(turn_count):

    # Check every turn to see if someone has won
    if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
        print("The " + turn + " has won.")
        return True
    elif turn_count == 10:
        print("It\'s a TIE!")
        return True

def place_character(user_turn):

    # CPU places character
    if user_turn == "cpu":
        cpu_choice = random.randint(1, 9)
        while the_board[str(cpu_choice)] != ' ':
            cpu_choice = random.randint(1, 9)
        the_board[str(cpu_choice)] = cpu_character
        time.sleep(2)

    # Player places character
    else:
        player_choice = input("Position: ")
        try:
            while the_board[player_choice] not in range(1, 9) and the_board[player_choice] != ' ': 
                player_choice = input("\nPlease choose an available position from 1-9 on the board: ")
            the_board[str(player_choice)] = player_character
        except KeyError:
            return place_character(user_turn)
        the_board[str(player_choice)] = player_character

def start_game():

    # Define a turn counter
    counter = 1
    global turn
    
    print("------------------------------------------------")
    print("\nWelcome to Noughts and Crosses. Please indicate which position you'd like on the\nboard by entering a number from 1-9, starting from the bottom left.")
    print("\nThe player\'s character is: " + player_character + "\nThe CPU\'s character is: " + cpu_character)
    
    while counter < 10:
        print("\nTurn: " + str(counter) + "  - It\'s the " + turn + "\'s turn")

        # Place a "X" or "O" on the board depending on the turn
        place_character(turn)
                
        print_board(the_board)
        print("------------------------------------------------")

        # Advance turn counter
        counter += 1

        # Win condition check
        if win_condition_check(counter) is True:
            return

        # Change turn
        if turn == "player":
            turn = "cpu"
        else:
            turn = "player"

def reset_board():
    for keys in the_board:
        the_board[keys] = ' '
        
    
