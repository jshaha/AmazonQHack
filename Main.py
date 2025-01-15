"""
Cloud-based Tic-tac-toe Game
Main game logic implementation
"""
import tkinter as tk
from ui import GameUI
from cloud_resources import CloudResources

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cloud Tic-tac-toe")
        self.window.protocol("WM_DELETE_WINDOW", self.cleanup_and_exit)
        self.cloud = CloudResources()
        self.ui = GameUI(self.window, self.make_move, self)
        self.current_player = "X"  # X represents S3, O represents DynamoDB
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def cleanup_and_exit(self):
        """Clean up resources and exit the game"""
        self.cloud.cleanup_resources()
        self.window.destroy()  # Close the game window

        
    def make_move(self, row, col):
        """Handle player moves and update game state"""
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.cloud.create_s3_bucket(f"XXXXXXXXXXXXXXXXXXXXXXX")
                self.ui.update_cell(row, col, "S3")
            else:
                self.cloud.create_database(f"player-move-{row}-{col}")
                self.ui.update_cell(row, col, "DB")
            
            if self.check_winner():
                self.ui.show_winner(self.current_player)
                return
            
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
                
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
            
        return False
    
    def cleanup_resources(self):
        try:
            # Example cleanup for S3
            response = self.s3.list_buckets()
            for bucket in response['Buckets']:
                if "tictactoe" in bucket['Name']:
                    self.s3.delete_bucket(Bucket=bucket['Name'])
                    print(f"Deleted bucket: {bucket['Name']}")

            # Example cleanup for DynamoDB
            response = self.dynamodb.list_tables()
            for table in response['TableNames']:
                if "tictactoe" in table:
                    self.dynamodb.delete_table(TableName=table)
                    print(f"Deleted table: {table}")
        except Exception as e:
            print(f"Error during resource cleanup: {e}")
    def reset_game(self):
        """Reset the game state for a new round"""
        self.current_player = "X"  # Reset to starting player
        self.board = [['' for _ in range(3)] for _ in range(3)]



    def run(self):
        """Start the game"""
        self.window.mainloop()
    

if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
