"""
Cloud-based Tic-tac-toe Game
User Interface implementation with animations
"""
import tkinter as tk
from animations import animate_placement

class GameUI:
    def __init__(self, window, move_callback, game):
        self.window = window
        self.move_callback = move_callback
        self.game = game
        self.cells = []
        self.setup_ui()

        
    def setup_ui(self):
        """Initialize the game board UI"""
        # Configure style
        self.window.configure(bg='#2c3e50')
        self.window.geometry("600x700")
        
        # Title
        title = tk.Label(
            self.window,
            text="Cloud Tic-tac-toe",
            font=('Helvetica', 24, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title.pack(pady=20)
        
        # Game board frame
        board_frame = tk.Frame(
            self.window,
            bg='#34495e',
            padx=10,
            pady=10
        )
        board_frame.pack()
        
        # Create cells
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Label(
                    board_frame,
                    width=10,
                    height=5,
                    bg='#3498db',
                    font=('Helvetica', 16, 'bold'),
                    relief='raised'
                )
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell.bind('<Button-1>', lambda e, r=row, c=col: self.cell_clicked(r, c))
                cell_row.append(cell)
            self.cells.append(cell_row)
    
    def cell_clicked(self, row, col):
        """Handle cell click events"""
        self.move_callback(row, col)
    
    def update_cell(self, row, col, player):
        """Update cell with player's move and animation"""
        cell = self.cells[row][col]
        icon = "☁️" if player == "S3" else "🗄️"
        animate_placement(cell, icon)
    
    def show_winner(self, winner):
        """Display winner notification"""
        message = "It's a Draw!" if winner == "draw" else f"{winner} Wins!"
        win_window = tk.Toplevel(self.window)
        win_window.title("Game Over")
        win_window.geometry("400x200")
        win_window.configure(bg='#f0f0f0')

        label = tk.Label(
            win_window,
            text=message,
            font=('Helvetica', 24, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        label.pack(pady=40)

        button = tk.Button(
            win_window,
            text="New Game",
            command=lambda: [win_window.destroy(), self.reset_game()],
            font=('Helvetica', 14),
            bg='#007bff',  # Blue button
            fg='white',
            bd=0,
            padx=10,
            pady=5
        )
        button.pack(pady=10)

        # Ensure resources are cleaned up on game end
        self.game.cloud.cleanup_resources()


    def reset_game(self):
        """Reset the game board for a new game"""
        # Cleanup AWS resources
        self.game.cloud.cleanup_resources()

        # Clear the UI cells
        for row in self.cells:
            for cell in row:
                cell.configure(text='', bg='#3498db')

        # Reset the game state via the game instance
        self.game.reset_game()

