# Import the chess library and random library
import chess
import random

def display_board(board):
    # Define a helper function to convert the piece to its Unicode symbol
    def piece_to_unicode(piece):
        if piece:
            return {
                'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
                'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
            }[piece.symbol()]
        else:
            return 'x '

    # Print the header of the chessboard
    print("\n  a b c d e f g h")
    print(" +-----------------+")

    # Loop through each row of the board
    for i in range(8):
        row = 8 - i
        row_str = f"{row}|"

        # Loop through each column of the board
        for j in range(8):
            piece = board.piece_at(chess.square(j, 7 - i))  # Calculate the square
            row_str += piece_to_unicode(piece) + ""

        # Display the row number after the row
        row_str += f"|{row}"
        print(row_str)
        print(" +-----------------+")

    # Print the footer of the chessboard
    print("  a b c d e f g h\n")

def display_moves(legal_moves):
    # Create an empty list to store formatted move strings
    formatted_moves = []

    # Iterate through all legal moves
    for move in legal_moves:
        # Get the source square name of the move
        source = chess.square_name(move.from_square)
        # Get the destination square name of the move
        destination = chess.square_name(move.to_square)
        # Append the formatted move string to the list
        formatted_moves.append(f"{source.upper()} -> {destination.upper()}")

    # Print the formatted move strings, four moves per row
    for i in range(0, len(formatted_moves), 4):
        print(" | ".join(formatted_moves[i:i+4]))
        
# Function to evaluate the current state of the board
def evaluate_board(board):
    # Dictionary to store the value of each chess piece
    piece_values = {'p': 1, 'r': 5, 'n': 3, 'b': 3, 'q': 9, 'k': 0}
    total_value = 0
    # Loop through all the pieces on the board
    for piece in board.piece_map().values():
        # Get the value of the current piece
        value = piece_values.get(piece.symbol().lower())
        # If the piece is a white piece, add its value to the total value
        if piece.color == chess.WHITE:
            total_value += value
        # If the piece is a black piece, subtract its value from the total value
        else:
            total_value -= value
    return total_value

def max_value(board, depth, alpha, beta):
    # Base case, return the evaluation of the board if we have reached the desired depth or the game is over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    # Set the initial maximum evaluation to negative infinity
    max_eval = float('-inf')
    best_move = None

    # Loop through all legal moves
    for move in board.legal_moves:
        # Make the move on the board
        board.push(move)
        # Recursively call the min_value function to get the evaluation of the next state
        eval, _ = min_value(board, depth - 1, alpha, beta)
        # Undo the move on the board
        board.pop()

        # Update the maximum evaluation and best move if a better one is found
        if eval > max_eval:
            max_eval = eval
            best_move = move

        # Update the alpha value
        alpha = max(alpha, eval)

        # Prune the search tree if beta is less than or equal to alpha
        if beta <= alpha:
            break

    # Return the maximum evaluation and the best move found
    return max_eval, best_move

def min_value(board, depth, alpha, beta):
    # Base case, return the evaluation of the board if we have reached the desired depth or the game is over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    # Set the initial minimum evaluation to positive infinity
    min_eval = float('inf')
    best_move = None

    # Loop through all legal moves
    for move in board.legal_moves:
        # Make the move on the board
        board.push(move)
        # Recursively call the max_value function to get the evaluation of the next state
        eval, _ = max_value(board, depth - 1, alpha, beta)
        # Undo the move on the board
        board.pop()

        # Update the minimum evaluation and best move if a better one is found
        if eval < min_eval:
            min_eval = eval
            best_move = move

        # Update the beta value
        beta = min(beta, eval)

        # Prune the search tree if beta is less than or equal to alpha
        if beta <= alpha:
            break

    # Return the minimum evaluation and the best move found
    return min_eval, best_move

def min_max_alpha_beta(board, depth, alpha, beta, maximizing_player):
    # Call either max_value or min_value depending on whether it's the maximizing player's turn or not
    if maximizing_player:
        return max_value(board, depth, alpha, beta)
    else:
        return min_value(board, depth, alpha, beta)
        
def playGame():
    
    print("========================================\n")
    print("       Welcome to the Chess Game!       \n")
    print("========================================\n")

    # Inform the player about their color and provide instructions
    print("You will be playing as White")
    print("The computer will play as Black")
    print("\nInstructions:")
    print("- Enter your move using the UCI (Universal Chess Interface) format.")
    print("  Example: To move the pawn from e2 to e4, enter 'e2e4'.")
    print("- Type 'quit' at any time to exit the game.")
    print("\nGood luck and have fun!")
    print("\nStarting the game...\n")
    
    # Initialize the chess board
    board = chess.Board()
    # Set the search depth for the MinMax Algorithm
    search_depth = 3
    # Loop until the game is over
    while not board.is_game_over():
        # Display the current state of the board
        display_board(board)

        # Check if it's the human player's turn
        if board.turn == chess.WHITE:
            print("\n***** Human's Turn *****")
            # Get a list of all legal moves for the human player
            legal_moves = list(board.legal_moves)
            print("All Possible Moves: ")
            display_moves(legal_moves)
            # Get the human player's move
            move = input("Enter Your Move (e.g., 'e2e4') or type 'quit' to exit the game: ")

            # Check if the human player wants to quit the game
            if move.lower() == 'quit':
                print("Exiting the game...")
                break

            # Convert the move from UCI format to a ChessMove object
            move = chess.Move.from_uci(move)
            # Check if the move is legal
            if move in board.legal_moves:
                # Make the move on the board
                board.push(move)
                print("Human Move: ", move)

            else:
                # If the move is not legal, prompt the player to try again
                print("Invalid Move. Try Again!")
        else:
            # If it's the computer's turn
            print("\n***** Computer's Turn *****")
            # Use the MinMax Algorithm to find the best move
            _, best_move = min_max_alpha_beta(board, search_depth, float('-inf'), float('inf'), False)
            # Make the best move on the board
            board.push(best_move)
            print("Computer Move: ", best_move)

    # Display the final state of the board
    display_board(board)
    # Print the result of the game
    result = board.result()
    print("Game Over. Result: ", result)
    if result == '1-0':
        print("Human Wins")
    elif result == '0-1':
        print("Computer Wins")
    else:
        print("Draw")

if __name__ == "__main__":
    # Start the game
    playGame()