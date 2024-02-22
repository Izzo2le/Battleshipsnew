from random import randint

# Legend
# 'X' for placing a ship and hitting a battleship
# '' for available space
# '-' for missed shot

HIDDEN_BOARD = [[''] * 8 for _ in range(8)]
GUESS_BOARD = [[''] * 8 for _ in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F G H')
    print('  -----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, " ".join(row)))
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

create_ships(HIDDEN_BOARD)
turns = 10
print('Hi, Welcome to my Battleship game')
while turns > 0:
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-' or GUESS_BOARD[row][column] == 'X':
        print('You have already guessed that.')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Yay, congratulations, you have hit a battleship!')
        GUESS_BOARD[row][column] = 'X'
    else:
        print('Oh no, sorry, you missed.')
        GUESS_BOARD[row][column] = '-'
    turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Yay, congratulations, you have sunk all the battleships!')
        break
    print(f'You have {turns} turns remaining.')
    if turns == 0:
        print('Sorry, your game is over.')
        break