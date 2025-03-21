# Tic Tac Toe | Version: 1.3.6
# Most Complete Version
# Move variables to global scope
# Added 3 options to replay the game

import random 
import time
import winsound

""" Global Variables """
game_mode_output = ""
difficulty_output = ""
player_marker_1 = ""
player_marker_2 = ""
computer_marker_1 = ""
computer_marker_2 = ""
choice_output = ""

def drawBoard(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i < 6:
            print('-' * 11)

def game_mode(game_mode_output):
    while True:
        mode = input("Choose game mode (0P/1P/2P): ").lower()
        if mode == "1p":
            print("1 Player mode selected.")
            game_mode_output = "1P"
            return game_mode_output
        elif mode == "2p":
            print("2 Player mode selected.")
            game_mode_output = "2P"
            return game_mode_output
        elif mode == "0p":
            print("Computer vs Computer mode selected.")
            game_mode_output = "0P"
            return game_mode_output
        else:
            print("Invalid. Please enter 0P, 1P, or 2P.")

def player_vs_player(board, choice_output, player_marker_1, player_marker_2):
    current_turn = ""

    if choice_output == "player 1 goes first":
        current_turn = "player 1"
    else:
        current_turn = "player 2"
    
    while True:
        drawBoard(board)
        if current_turn == "player 1":
            player_1_turn(board, player_marker_1)
            if check_condition(board, player_marker_1, player_marker_2):
                break
            current_turn = "player 2"
        else:
            player_2_turn(board, player_marker_2)
            if check_condition(board, player_marker_1, player_marker_2):
                break
            current_turn = "player 1"

def player_vs_computer(board, difficulty_output, choice_output, player_marker_1, computer_marker_1):
    current_turn = ""
    if choice_output == "player goes first":
        current_turn = "player"
    else:
        current_turn = "computer"

    while True:
        drawBoard(board)
        if current_turn == "player":
            player_1_turn(board, player_marker_1)
            if check_condition(board, player_marker_1, computer_marker_1):
                break
            current_turn = "computer"
        else:
            computer_1_turn(board, difficulty_output, computer_marker_1, player_marker_1)
            if check_condition(board, player_marker_1, computer_marker_1):
                break
            current_turn = "player"

def computer_vs_computer(board, game_mode_output, difficulty_output, computer_marker_1, computer_marker_2):
    current_turn = ""
    
    if game_mode_output == "0P":
        current_turn = "computer 1"
    else:
        current_turn = "computer 2"

    while True:
        drawBoard(board)
        if current_turn == "computer 1":
            winsound.Beep(300, 500)
            computer_1_turn(board, difficulty_output, computer_marker_1, computer_marker_2)
            if check_condition(board, computer_marker_1, computer_marker_2):
                break
            current_turn = "computer 2"
            time.sleep(1.5)
        else:
            winsound.Beep(400, 500)
            computer_2_turn(board, difficulty_output, computer_marker_2, computer_marker_1)
            if check_condition(board, computer_marker_1, computer_marker_2):
                break
            current_turn = "computer 1"
            time.sleep(1.5)

def difficulty_choice(game_mode_output, difficulty_output):
    if game_mode_output == "2P":
        return None
    else:
        while True:
            difficulty = input("\nChoose difficulty (easy/hard): ").lower()
            if difficulty == "easy":
                print("Easy mode selected.")
                difficulty_output = "easy"
                break
            elif difficulty == "hard":
                print("Hard mode selected.")
                difficulty_output = "hard"
                break
            else:
                print("Invalid. Please enter easy or hard.")

    return difficulty_output

def marker_selection(game_mode_output, player_marker_1, player_marker_2, computer_marker_1, computer_marker_2):
    if game_mode_output == "1P":
        while True:
            marker_selection = input("\nChoose your marker, X or O: ").lower()

            if marker_selection == "x":
                player_marker_1 = "X"
                computer_marker_1 = "O"
                break
            elif marker_selection == "o": 
                player_marker_1 = "O"
                computer_marker_1 = "X"
                break
            else:
                print("Invalid. Please enter 'X' or 'O'.")
        return player_marker_1, computer_marker_1

    elif game_mode_output == "2P":
        while True:
            marker_selection = input("Player 1. Choose your marker, X or O: ").lower()

            if marker_selection == "x":
                player_marker_1 = "X"
                player_marker_2 = "O"
                break
            elif marker_selection == "o": 
                player_marker_1 = "O"
                player_marker_2 = "X"
                break
            else:
                print("Invalid. Please enter 'X' or 'O'.")
        return player_marker_1, player_marker_2
    
    elif game_mode_output == "0P":
        random_number = random.randint(0, 1)
        if random_number == 0:
            computer_marker_1 = "X"
            computer_marker_2 = "O"
        else:
            computer_marker_1 = "O"
            computer_marker_2 = "X"
        return computer_marker_1, computer_marker_2

def turn_order_choice(game_mode_output, choice_output):
    while True:
        if game_mode_output == "1P":
            choice = input("\nGo first, second, or random?: ").lower()
            if choice == "first":
                choice_output = "player goes first"
                break
            elif choice == "second":
                print("Computer goes first.")
                choice_output = "computer goes first"
                break
            elif choice == "random":
                random_number = random.randint(0, 1)
                if random_number == 0:
                    print("Player goes first.")
                    choice_output = "player goes first"
                else:
                    print("Computer goes first.")
                    choice_output = "computer goes first"
                break
            else:
                print("Invalid. Please enter first, second, or random.")
        
        elif game_mode_output == "2P":
            choice = input("Player 1. Go first, second, or random?: ").lower()
            if choice == "first":
                choice_output = "player 1 goes first"
                break
            elif choice == "second":
                choice_output = "player 2 goes first"
                break
            elif choice == "random":
                random_number = random.randint(0, 1)
                if random_number == 0:
                    print("Player 1 goes first.")
                    choice_output = "player 1 goes first"
                else:
                    print("Player 2 goes first.")
                    choice_output = "player 2 goes first"
                break
            else:
                print("Invalid. Please enter first, second, or random.")

        elif game_mode_output == "0P":
            random_number = random.randint(0, 1)
            if random_number == 0:
                print("Computer 1 goes first.")
                choice_output = "computer 1 goes first"
            else:
                print("Computer 2 goes first.")
                choice_output = "computer 2 goes first"
            break
    
    return choice_output

def player_1_turn(board, player_marker_1):
    while True:
        try:
            position = int(input(f"\nPlayer {player_marker_1}, enter your move (1-9): "))
            if 1 <= position <= 9 and board[position - 1] == str(position):
                board[position - 1] = player_marker_1
                return board
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. No words allowed. Enter a number.")
    return board

def player_2_turn(board, player_marker_2):
    while True:
        try:
            position = int(input(f"\nPlayer {player_marker_2}, enter your move (1-9): "))
            if 1 <= position <= 9 and board[position - 1] == str(position):
                board[position - 1] = player_marker_2
                return board
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. No words allowed. Enter a number.")
    return board

def computer_1_turn(board, difficulty_output, computer_marker_1, player_marker_1):
    if difficulty_output == "easy":
        move = easy_computer(board, computer_marker_1)
    else:
        move = hard_computer(board, computer_marker_1, player_marker_1)
    if move is not None:
        board[move] = computer_marker_1
    return board

def computer_2_turn(board, difficulty_output, computer_marker_2, player_marker_1):
    if difficulty_output == "easy":
        move = easy_computer(board, computer_marker_2)
    else:
        move = hard_computer(board, computer_marker_2, player_marker_1)
    if move is not None:
        board[move] = computer_marker_2
    return board

def easy_computer(board, computer_marker_1):
    while True:
        random_number = random.randint(0, 8)
        if board[random_number] == str(random_number + 1):
            return random_number

def hard_computer(board, computer_marker_1, player_marker_1):
    # Check if computer can win in the next move
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board_copy = board[:]
            board_copy[i] = computer_marker_1
            if check_win(board_copy) == computer_marker_1:
                return i

    # Check if player can win. Block them.
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board_copy = board[:]
            board_copy[i] = player_marker_1
            if check_win(board_copy) == player_marker_1:
                return i

    # Take one of the corners if they are free
    for i in [0, 2, 6, 8]:
        if board[i] not in ['X', 'O']:
            return i

    # Take the center if it is free
    if board[4] not in ['X', 'O']:
        return 4

    # Take one of the sides
    for i in [1, 3, 5, 7]:
        if board[i] not in ['X', 'O']:
            return i

    return None

def check_condition(board, player_marker, computer_marker):
    winner = check_win(board)
    if winner:
        drawBoard(board)
        if winner == player_marker:
            print(f"\n{player_marker} wins!")
        else:
            print(f"\n{computer_marker} wins!")
        return True
    elif check_draw(board):
        drawBoard(board)
        print("\nIt's a draw!")
        return True
    return False

def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]]
        
    return None

def check_draw(board):
    for number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if number in board:
            return False
    return True

def main():
    global game_mode_output, difficulty_output, player_marker_1, player_marker_2, computer_marker_1, computer_marker_2, choice_output # Overwrite global variables
    
    board = ['1', '2', '3','4', '5', '6','7', '8', '9']
          
    print("\n" * 50)
    print("Welcome to Tic-Tac-Toe!")

    if not game_mode_output: # If global variable, "game_mode_output", is empty then ask for settings.

        game_mode_output = game_mode(game_mode_output)

        difficulty_output = difficulty_choice(game_mode_output, difficulty_output)
        
        if game_mode_output == "1P":
            player_marker_1, computer_marker_1 = marker_selection(game_mode_output, player_marker_1, player_marker_2, computer_marker_1, computer_marker_2)
        elif game_mode_output == "2P":
            player_marker_1, player_marker_2 = marker_selection(game_mode_output, player_marker_1, player_marker_2, computer_marker_1, computer_marker_2)
        elif game_mode_output == "0P":
            computer_marker_1, computer_marker_2 = marker_selection(game_mode_output, player_marker_1, player_marker_2, computer_marker_1, computer_marker_2)

        choice_output = turn_order_choice(game_mode_output, choice_output)

    """ Game Loop """
    if game_mode_output == "1P":
        player_vs_computer(board, difficulty_output, choice_output, player_marker_1, computer_marker_1)
    elif game_mode_output == "2P":
        player_vs_player(board, game_mode_output, player_marker_1, player_marker_2)
    elif game_mode_output == "0P":
        computer_vs_computer(board, game_mode_output, difficulty_output, computer_marker_1, computer_marker_2)
    else:
        print("Invalid game mode.")

    while True:
        print("\nChoose:")
        print("1. Play again with SAME settings")
        print("2. Play again with NEW settings")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            main()
        elif choice == "2":
            game_mode_output = ""
            difficulty_output = ""
            player_marker_1 = ""
            player_marker_2 = ""
            computer_marker_1 = ""
            computer_marker_2 = ""
            choice_output = ""
            main() 
        elif choice == "3":
            print("Exiting...")
            exit()
        else:
            print("\nInvalid. Please enter 1, 2, or 3.")

main()