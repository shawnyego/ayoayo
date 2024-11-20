#First iteration attempt
class AyoayoGame:
    def __init__(self):
        # Each player has 6 pits; initialize each with 4 seeds
        self.board = [4] * 12
        self.stores = [0, 0]  # Player 1's and Player 2's stores
        self.current_player = 1

    def display_board(self):
        print("\nBoard:")
        print(f"Player 2: {' '.join(map(str, self.board[6:][::-1]))}")
        print(f"Stores: P1={self.stores[0]} P2={self.stores[1]}")
        print(f"Player 1: {' '.join(map(str, self.board[:6]))}\n")

    def play_turn(self):
        print(f"Player {self.current_player}'s turn")
        pit_choice = self.get_valid_pit_choice()
        self.sow_seeds(pit_choice)

    def get_valid_pit_choice(self):
        while True:
            try:
                pit = int(input(f"Player {self.current_player}, choose a pit (1-6): ")) - 1
                if self.is_valid_pit(pit):
                    return pit
                else:
                    print("Invalid choice. Choose a non-empty pit from your side.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

    def is_valid_pit(self, pit):
        # Check if the pit belongs to the current player and is not empty
        start, end = (0, 6) if self.current_player == 1 else (6, 12)
        return start <= pit < end and self.board[pit] > 0

    def sow_seeds(self, pit):
        seeds = self.board[pit]
        self.board[pit] = 0
        index = pit

        while seeds > 0:
            index = (index + 1) % 12
            if index != pit:  # Skip the pit the seeds came from
                self.board[index] += 1
                seeds -= 1

        # Check for capture rules if last seed lands on an opponent's pit
        if self.is_opponent_pit(index):
            if self.board[index] in (2, 3):
                self.capture_seeds(index)

        # Switch turns
        self.current_player = 3 - self.current_player

    def is_opponent_pit(self, index):
        if self.current_player == 1:
            return 6 <= index < 12
        else:
            return 0 <= index < 6

    def capture_seeds(self, index):
        captured = self.board[index]
        self.board[index] = 0
        self.stores[self.current_player - 1] += captured
        print(f"Player {self.current_player} captured {captured} seeds!")

    def is_game_over(self):
        # Game ends when one side of the board is empty
        return all(s == 0 for s in self.board[:6]) or all(s == 0 for s in self.board[6:])

    def announce_winner(self):
        print("\nGame over!")
        print(f"Final Stores: P1={self.stores[0]} P2={self.stores[1]}")
        if self.stores[0] > self.stores[1]:
            print("Player 1 wins!")
        elif self.stores[1] > self.stores[0]:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    def play_game(self):
        while not self.is_game_over():
            self.display_board()
            self.play_turn()
        self.announce_winner()

# Run the game
if __name__ == "__main__":
    game = AyoayoGame()
    game.play_game()
