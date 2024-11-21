#Iteration 2 (2 Queues approach)

#Initiazlise the board
player_1_holes =[4,4,4,4,4,4]
player_2_holes =[4,4,4,4,4,4]

#function to visualise the board

def display_board():
    print(f"Player 2:{player_2_holes[::-1]}")
    print(f"Player 1:{player_1_holes}")
#test1 
display_board()

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

#test2
display_board()