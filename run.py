from random import randint

# Initialize boards
HIDDEN_BOARD = [[''] * 8 for _ in range(8)]
GUESS_BOARD = [[''] * 8 for _ in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F G H')
    print('  ----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, " ".join(row if row else ' ' for row in row)))
        row_number += 1

def create_ships(board):
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    while True:
        row = input('Please enter a ship row, using numbers 1-8: ')
        if row in '12345678':
            break
        else:
            print('Invalid input. Please enter a valid row.')
    
    while True:
        column = input('Please enter a ship column, using letters A-H: ').upper()
        if column in 'ABCDEFGH':
            break
        else:
            print('Invalid input. Please enter a valid column.')
    
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def play_game():
    global HIDDEN_BOARD, GUESS_BOARD
    HIDDEN_BOARD = [[''] * 8 for _ in range(8)]
    GUESS_BOARD = [[''] * 8 for _ in range(8)]
    create_ships(HIDDEN_BOARD)
    
    turns = 10
    while turns > 0:
        print_board(GUESS_BOARD)
        print(f"You have {turns} turns left.")
        row, col = get_ship_location()
        if GUESS_BOARD[row][col] != '':
            print("You've already tried that coordinate. Try again.")
            continue
        if HIDDEN_BOARD[row][col] == 'X':
            print("Congratulations! You've hit a battleship!")
            GUESS_BOARD[row][col] = 'X'
            turns -= 1
        else:
            print("Sorry, you missed!")
            if GUESS_BOARD[row][col] == '':
                GUESS_BOARD[row][col] = 'O'
            turns -= 1
        
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You've sunk all the battleships! You win!")
            break
        elif turns == 0:
            print("Game over! You've run out of turns.")
            print_board(HIDDEN_BOARD)
            break
    
    after_game()

def after_game():
    print("Would you like to play again or go back to the main menu?")
    print("1 -- Play Again")
    print("2 -- Main Menu")
    print("3 -- Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        play_game()
    elif choice == '2':
        main_menu()
    elif choice == '3':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")
        after_game()

def rules():
    print("The rules of the game are simple. The aim is to sink all five ships hidden on the board.")

def main_menu():
    print('Welcome to Battleship!')
    print('1 -- Play Game')
    print('2 -- Rules')
    print('3 -- Exit')

    while True:
        choice = input('Please choose an option (1-3): ')
        if choice == '1':
            play_game()
        elif choice == '2':
            rules()
        elif choice == '3':
            print('Goodbye!')
            exit()
        else:
            print('Please choose an option between 1 - 3')

if __name__ == "__main__":
    main_menu()