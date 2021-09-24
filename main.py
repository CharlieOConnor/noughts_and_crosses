import noughts_and_crosses

replay = True

def play_again():
    global replay
    player_ask = input("\nWould you like to play again? (yes/no): ")
        
    if "yes" in player_ask:
        noughts_and_crosses.reset_board()
        noughts_and_crosses.start_game()
    elif "no" in player_ask:
        print("Thanks for playing!")
        replay = False
    else:
        print("Response not understood. Please enter either 'yes' or 'no'.")
        return play_again()

while replay == True:
    noughts_and_crosses.start_game()
    play_again()

            
            
