import os
import random

clear = lambda: os.system('clear')


# def clear_output():
#     print('\n'*100)

def init_board():
    return [' '] * 10


def display_board(board):
    """
    Display 3x3 board where index of each cell corresponds with a number on a keypad as follows:\n
    |7|8|9|\n
    |4|5|6|\n
    |1|2|3|
    :param board: list of 10 elements where the element at position 0 is not used
    :return:
    """
    clear()
    print('-' * 13)
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('-' * 13)
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('-' * 13)
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('-' * 13)


# Test
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# display_board(test_board)
# clear()

def player_input():
    """
    Take in a player input and assign a marker as 'X' or 'O'
    :return: tuple (player1 marker, player2 marker)
    """

    marker = ''
    acceptable_markers = ['X', 'O']

    # Keep asking player-1 to choose X or O as a marker
    while marker not in acceptable_markers:
        marker = input('PLAYER-1, do you want to use X or O? ').upper()

        if marker not in acceptable_markers:
            print("INVALID INPUT: please enter a valid option X or O")

    # Assign player-2 the opposite marker
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Test
# player1_marker, player2_marker = player_input()
# print(f'player1: "{player1_marker}", player2: "{player2_marker}"')

def place_marker(board, marker, position):
    """
    Take in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the
    board.
    :param board:
    :param marker:
    :param position:
    :return:
    """
    board[position] = marker


# Test
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board, mark):
    """
    Take in a board and a mark (X or O) and then checks to see if that mark has won.
    Check all the rows, all the columns and diagonals in 3x3 board where index of each cell corresponds with a number
    on a keypad as follows:\n
    |7|8|9|\n
    |4|5|6|\n
    |1|2|3|
    :param board:
    :param mark:
    :return:
    """
    win_comb = [mark.upper()] * 3
    print(f'win_comb={win_comb}')
    return win_comb == board[7:10] or win_comb == board[4:7] or win_comb == board[1:4] \
        or win_comb == board[1:8:3] or win_comb == board[2:9:3] or win_comb == board[3:10:3] \
        or win_comb == board[1:10:4] or win_comb == board[3:8:2]


# Test
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# print(win_check(test_board, 'o'))

def choose_first():
    """
    Randomly decide which of two players goes first.
    :return: a string of which player went first
    """
    return str(random.randint(1, 2))


def space_check(board, position):
    """
    Check whether a space at the specified index on the board is freely available.
    :param board:
    :param position:
    :return: True if space is available, False otherwise
    """
    return board[position].upper() not in ['X', 'O']


# Test
# test_board = ['#','X',' ','X','O','X','O','X','O','X']
# display_board(test_board)
# print(space_check(test_board, 2))

def full_board_check(board):
    """
    Check if the board is full.
    :param board:
    :return: True if full, False otherwise
    """
    # Version-1: using space_check function
    # for i in range (1,10):
    #     if space_check(board,i):
    #         return False
    #
    # return True

    # Version-2: convert board list to the set of unique values, filter the set for char other than 'X' or 'O', convert
    # the result back to list and check its len. If length is equal 0 board is full.
    # return len(list(filter(lambda x:x.upper() not in ['X','O'], set(board[1:])))) == 0

    # Version-3: find first occurrence of position with available space on the board, if found the board is not full,
    # otherwise it's full
    return next((position for position in range(1, 10) if space_check(board, position)), None) is None


# Test
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# print(f'is_board_full={full_board_check(test_board)}')

def player_choice(board, player_num, player_marker):
    """
    Ask for a player's next position (as a number 1-9). Check if it's a free position.
    :param board:
    :return: position index
    """
    assert not full_board_check(board), "board should not be full"

    choice = 'INVALID'
    acceptable_range = range(1, 10)
    within_range = False
    space_available = False

    # Conditions to check: digit and within_range and board and space is available
    while not choice.isdigit() or not within_range or not space_available:

        choice = input(f"PLAYER-{player_num} ({player_marker}), please choose the next position (1-9): ")

        # Digit check
        if not choice.isdigit():
            print('INVALID INPUT: please enter a number (1-9)')
            continue
        else:
            # Range check for digit
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("INVALID INPUT: you are out of acceptable range (1-9), please try again")
                within_range = False
                continue

            # Space availability check
            if within_range:
                space_available = space_check(board, int(choice))
                if not space_available:
                    print(f'The space at position [{int(choice)}] is not available, please try again')

    return int(choice)


def replay():
    """
    Ask the player if they want to play again.
    :return: True if they do want to play again, otherwise False
    """
    choice = 'invalid'
    acceptable_choices = ['Y', 'N']

    while choice not in acceptable_choices:

        choice = input("Do you want to play again? (Y/N) ").upper()

        if choice not in acceptable_choices:
            print("INVALID INPUT: please enter one of the following [YyNn]")

    return choice == "Y"


def play_turn(board, player_marker, player_num, game_on):
    # Show the board
    display_board(board)
    # Chose a position
    position = player_choice(board, player_num, player_marker)
    # Place the marker on the board
    place_marker(board, player_marker, position)

    # Check if they won
    if win_check(board, player_marker):
        display_board(board)
        print(f'PLAYER-{player_num} HAS WON!!!')
        game_on = False
    else:
        if full_board_check(board):
            display_board(board)
            print('TIE GAME!')
            game_on = False
        else:
            player_num = '2' if player_num == '1' else '1'

    return player_num, game_on


# Main program
def main():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Play the game
        board = [' '] * 10
        display_board(board)
        player1_marker, player2_marker = player_input()
        print(f'PLAYER-1 marker: {player1_marker}, PLAYER-2 marker: {player2_marker}')

        player_num = choose_first()
        print(f'PLAYER-{player_num} will go first')

        play_game = (input('Ready to play (y or n)? [y] ') or 'y').upper()

        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        ## Game play
        while game_on:
            if player_num == '1':
                player_num, game_on = play_turn(board, player1_marker, player_num, game_on)
            else:
                player_num, game_on = play_turn(board, player2_marker, player_num, game_on)

        if not replay():
            print("Game's over, goodbye!")
            break


main()
