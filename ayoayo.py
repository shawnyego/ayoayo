# Initialize the board
player_1_holes = [4, 4, 4, 4, 4, 4]
player_2_holes = [4, 4, 4, 4, 4, 4]
player_1_bank = 0  # Player 1's bank (Store)
player_2_bank = 0  # Player 2's bank (Store)


def declare_banks():
    global player_1_bank, player_2_bank
    
    # Player 1's choice of a bank hole
    print("Player 1, choose a hole (0-5) as your bank:")
    player_1_bank_index = int(input()) 
    while player_1_bank_index < 0 or player_1_bank_index > 5:
        print("Invalid choice! Choose a hole between 0 and 5.")
        player_1_bank_index = int(input())
    
    # Update player_1_bank to the chosen hole index value
    player_1_bank = player_1_bank_index
    print(f"Player 1 has chosen hole {player_1_bank} as their bank.")
    
    # Player 2 chooses a bank hole (Assuming player 2 selects their bank manually or by another system)
    print("Player 2, choose a hole (0-5) as your bank:")
    player_2_bank_index = int(input())
    while player_2_bank_index < 0 or player_2_bank_index > 5 :
        print("Invalid choice! Choose a hole between 0 and 5.")
        player_2_bank_index = int(input())
    
    # Update player_2_bank to the chosen hole index value
    player_2_bank = player_2_bank_index
    print(f"Player 2 has chosen hole {player_2_bank} as their bank.")
    
# Function to visualize the board
def display_board():
    print(f"Player 2: {player_2_holes[::-1]}")  # Reverse Player 2's holes for correct display
    print(f"Stores: P1 Bank={player_1_bank} P2 Bank={player_2_bank}")
    print(f"Player 1: {player_1_holes}")

def redistribute_seeds(player, hole_index):
    global player_1_holes, player_2_holes, player_1_bank, player_2_bank
    # Ensure the player number is valid (either 1 or 2)
    if player not in [1, 2]:
        print("Invalid player number!")
        return

    # Determine the player's holes and bank
    if player == 1:
        holes = player_1_holes
        opponent_holes = player_2_holes
        bank = player_1_bank
        opponent_bank = player_2_bank
        player_name="Player 1 "
    else:
        holes = player_2_holes
        opponent_holes = player_1_holes
        bank = player_2_bank
        opponent_bank = player_1_bank
        player_name="Player 2"

    print(f"\n{player_name}'s turn")
    display_board()

    # Validate that the hole is between 1 and 5 and not empty
    while True:
        hole_index = int(input(f"Choose a hole between 1-5 (current: {holes}): "))

        if hole_index < 1 or hole_index > 5:  # Check if hole index is in valid range
          print("Invalid choice! Choose a hole between 1-5.")
        elif holes[hole_index] == 0:  # Check if the chosen hole is empty
          print("The chosen hole is empty! Please choose a different hole with seeds.")
        elif hole_index == bank:  # Ensure the player doesn't pick their bank hole (0 for P1, 6 for P2)
          print(f"You cannot choose your bank (hole {bank}). Choose a hole between 1-5 that is not empty.")
        else:
          break  

    seeds = holes[hole_index]
    holes[hole_index] = 0  # Empty the chosen hole
# Combine Player 1's and Player 2's holes for redistribution
    board = holes + opponent_holes[::-1]  # Reverse Player 2's holes for proper indexing

    index = hole_index
    while seeds > 0:
        index = (index + 1) % 12  # Wrap around the board
        
        # Skip the bank (hole 0 for Player 1 and hole 6 for Player 2)
        if index == 0:  # Player 1's bank
            continue
        elif index == 6:  # Player 2's bank
            continue
        
        # Distribute the seeds
        if index < 6:  # Player 1's holes (index 1-5)
            player_1_holes[index] += 1
        else:  # Player 2's holes (index 6-11)
            player_2_holes[index - 6] += 1
        
        seeds -= 1

    # Update the board after redistribution
    player_1_holes = board[:6]
    player_2_holes = board[6:][::-1]   # Reverse Player 2's holes back to their correct order

# Display the updated board
display_board()


# Function to check if the game has ended
def check_end_game():
    global player_1_holes, player_2_holes, player_1_bank, player_2_bank

    # Check if one side is empty
    if all(seeds == 0 for seeds in player_1_holes) or all(seeds == 0 for seeds in player_2_holes):
        # Transfer remaining seeds to the opponent's bank
        player_1_bank += sum(player_1_holes)
        player_2_bank += sum(player_2_holes)

        # Clear the board
        player_1_holes = [0] * 6
        player_2_holes = [0] * 6

        # Display the final board and scores
        display_board()

        # Determine the winner
        if player_1_bank > player_2_bank:
            print(f"Player 1 wins! Final Score: P1={player_1_bank} P2={player_2_bank}")
        elif player_2_bank > player_1_bank:
            print(f"Player 2 wins! Final Score: P1={player_1_bank} P2={player_2_bank}")
        else:
            print(f"It's a draw! Final Score: P1={player_1_bank} P2={player_2_bank}")

        return True  # Game over
    return False

# Function to play the game
def play_game():
    # Declare banks at the start
    declare_banks()

    while True:
        # Player 1's turn
        print("\nPlayer 1's turn")
        display_board()
        hole_index = int(input("Choose a hole (0-5): "))
        redistribute_seeds(1, hole_index)
        if check_end_game():
            break

        # Player 2's turn
        print("\nPlayer 2's turn")
        display_board()
        hole_index = int(input("Choose a hole (0-5): "))
        redistribute_seeds(2, hole_index)
        if check_end_game():
            break

# Start the game
play_game()


