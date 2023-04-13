# Chess-Game-with-MinMax-Algorithm
This is a command-line based chess game implemented using the MinMax algorithm. The player plays as the White pieces and the computer plays as the Black pieces.

The game board is displayed using Unicode chess pieces and algebraic notation.

The MinMax algorithm is a decision-making algorithm used in game theory, decision theory, and artificial intelligence. It searches through all possible moves and outcomes to find the best move to make based on the current state of the game.

# Requirements
Python 3.x
python-chess

# How to Play
Clone the repository or download the source code.
Install the required libraries using the command pip install -r requirements.txt
Run the chess_game.py file using the command python chess_game.py
Follow the instructions displayed on the screen to play the game.

# Instructions

Enter your move using the UCI (Universal Chess Interface) format. For example, to move the pawn from e2 to e4, enter 'e2e4'.
Type 'quit' at any time to exit the game.

# Implementation Details
The game is implemented using the Python Chess library.
The board is displayed using Unicode chess pieces and algebraic notation.
The MinMax algorithm is used to determine the computer's moves.
The search depth for the MinMax algorithm is set to 3.
The evaluation function used to evaluate the state of the board is a simple material evaluation function that assigns a value to each piece and calculates the total value of all the pieces on the board.
