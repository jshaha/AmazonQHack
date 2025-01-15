# AmazonQHack

# Cloud Tic-tac-toe Game

A unique take on the classic Tic-tac-toe game where players use cloud resources (S3 buckets and DynamoDB tables) instead of X's and O's.

## Features

- Clean and modern user interface
- Player X uses S3 buckets (☁️)
- Player O uses DynamoDB tables (🗄️)
- Smooth animations for piece placement
- Cloud resource simulation

## Requirementsa

- Python 3.7+
- tkinter
- boto3

## Installation

1. Clone the repository
2. Install requirements:
   ```
   pip install boto3
   ```

## Running the Game

```python
python main.py
```

## Code Structure

- `main.py`: Main game logic and controller
- `ui.py`: User interface implementation
- `cloud_resources.py`: AWS resource management
- `animations.py`: Visual effects and animations

## Note

This is a simulation - no actual AWS resources are created during gameplay. In a production environment, you would need to implement proper AWS resource management and cleanup.
