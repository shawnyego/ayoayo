#Iteration 2 (2 Queues approach)

#Initiazlise the board
player_1_holes =[4,4,4,4,4,4]
player_2_holes =[4,4,4,4,4,4]

#function to visualise the board

# def display_board():
#     print(f"Player 2:{player_2_holes[::-1]}")
#     print(f"Player 1:{player_1_holes}")
# #test1 
# display_board()

def redistribute_seeds(player,hole_index):
    global player_1_holes,player_2_holes
    
    #make sure hole isn't empty 
    if player ==1 :
        if player_1_holes[hole_index]==0:
            print("Choose a different hole ,this one is empty ")
    else: 
        if player_2_holes[hole_index]==0:
            print("Choose a different hole to play,this is empty ")
    #determine the starting point based on the player 
    if player == 1 :
        seeds=player_1_holes[hole_index]
        player_1_holes[hole_index]=0
        board=player_1_holes+player_2_holes[::-1]
    else:
        seeds=player_2_holes[hole_index]
        player_2_holes[hole_index]=0
        board=player_2_holes+player_1_holes[::-1]
        
    for _ in range(seeds):
        index = (index + 1) % 12  # Circular increment within the circular board
        board[index] += 1

        
    # Split the board back into two rows
    if player == 1:
        player_1_holes = board[:6]
        player_2_holes = board[6:][::-1]  # Reverse Player 2's pits back
    else:
        player_2_holes = board[:6]
        player_1_holes = board[6:][::-1]  # Reverse Player 1's pits back



player_1_bank = 0  # Player 1's bank (Store)
player_2_bank = 0  # Player 2's bank (Store)

# players to choose their bank
def declare_banks():
    global player_1_bank, player_2_bank, player_1_holes, player_2_holes
    
    #Player 1's choice of a bank hole
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
    
    # Store the initial bank hole selections
    player_1_holes[player_1_bank_index] = 'B'  # Mark Player 1's bank hole
    player_2_holes[player_2_bank_index] = 'B'  # Mark Player 2's bank hole

    print(f"Player 1 has chosen hole {player_1_bank_index} as their bank.")
    print(f"Player 2 has chosen hole {player_2_bank_index} as their bank.")
    
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


def display_board():
    print(f"Player 2: {player_2_holes}")
    print(f"Stores: P1 Bank={player_1_bank} P2 Bank={player_2_bank}")
    print(f"Player 1: {player_1_holes}")