# Initialize the board
player_1_holes = [4, 4, 4, 4, 4, 4]
player_2_holes = [4, 4, 4, 4, 4, 4]
player_1_bank = 0  # Player 1's bank (Store)
player_2_bank = 0  # Player 2's bank (Store)

# Declare bank holes
player_1_bank_index = None
player_2_bank_index = None

# Function to visualize the board
def display_board():
    print(f"Player 2: {player_2_holes[::-1]}")  # Reverse Player 2's holes for correct display
    print(f"Stores: P1 Bank={player_1_bank} P2 Bank={player_2_bank}")
    print(f"Player 1: {player_1_holes}")

# Function to redistribute seeds
def redistribute_seeds(player, hole_index):
    global player_1_holes, player_2_holes, player_1_bank, player_2_bank
    
    if player == 1:
        seeds = player_1_holes[hole_index]
        player_1_holes[hole_index] = 0
        board = player_1_holes + player_2_holes[::-1]
    else:
        seeds = player_2_holes[hole_index]
        player_2_holes[hole_index] = 0
        board = player_2_holes + player_1_holes[::-1]

    for _ in range(seeds):
        index = (index + 1) % 12
        if index == 5 and player == 1:  # If Player 1's bank hole
            player_1_bank += 1
        elif index == 11 and player == 2:  # If Player 2's bank hole
            player_2_bank += 1
        else:
            board[index] += 1
    
    if player == 1:
        player_1_holes = board[:6]
        player_2_holes = board[6:][::-1]
    else:
        player_2_holes = board[:6]
        player_1_holes = board[6:][::-1]

    
    # Display the updated board
    display_board()

# Function to declare bank choices
def declare_banks():
    global player_1_bank_index, player_2_bank_index
    
    # Player 1's choice of a bank hole
    print("Player 1, choose a hole (0-5) as your bank:")
    player_1_bank_index = int(input()) 
    while player_1_bank_index < 0 or player_1_bank_index > 5:
        print("Invalid choice! Choose a hole between 0 and 5.")
        player_1_bank_index = int(input())
    
    # Player 2 chooses a bank hole
    print("Player 2, choose a hole (0-5) as your bank:")
    player_2_bank_index = int(input())  
    while player_2_bank_index < 0 or player_2_bank_index > 5:
        print("Invalid choice! Choose a hole between 0 and 5.")
        player_2_bank_index = int(input())
    
    # Display initial bank choices
    print(f"Player 1 has chosen hole {player_1_bank_index} as their bank.")
    print(f"Player 2 has chosen hole {player_2_bank_index} as their bank.")

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