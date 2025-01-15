"""
Cloud-based Tic-tac-toe Game
Animation effects for game moves
"""
import tkinter as tk

def animate_placement(cell, icon, steps=10):
    """
    Animate the placement of a game piece
    
    Args:
        cell: The tkinter Label widget to animate
        icon: The icon to display (☁️ for S3, 🗄️ for DynamoDB)
        steps: Number of animation steps
    """
    def update_scale(step):
        if step <= steps:
            # Calculate scale factor
            scale = step / steps
            size = int(16 * scale)  # Base font size is 16
            cell.configure(
                text=icon,
                font=('Helvetica', size, 'bold'),
                fg='white'
            )
            cell.after(50, lambda: update_scale(step + 1))
    
    # Start animation
    update_scale(1)
