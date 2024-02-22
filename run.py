from random import randint

# Initialize boards
HIDDEN_BOARD = [[''] * 8 for _ in range(8)]
GUESS_BOARD = [[''] * 8 for _ in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# Define your functions (print_board, create_ships, get_ship_location, count_hit_ships) here

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
 """
    Plays the game
    """
print("we're having so much fun!")

def rules():
      """
    Displays the rules
    """
print("The rules of the game are simple. The aim is to sink all five ships hidden on the board.")

def main_menu():
    """
    Displays the main menu
    """
    print('Welcome to Battleship!')
    print('1 -- Play Game')
    print('2 -- Rules')
    print('3 -- Exit')

    while True:
        choice = input('Please choose an option (1-3): ')
        if choice == '1':
            play_game()
            break  # Breaks the loop to allow re-displaying the menu after the game
        elif choice == '2':
            rules()
        elif choice == '3':
            print('Goodbye!')
            exit()
        else:
            print('Please choose an option between 1 - 3')

# Main program starts here
if __name__ == "__main__":
    while True:
        main_menu()


