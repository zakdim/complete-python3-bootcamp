def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


def position_choice():

    choice = 'invalid'
    acceptable_choices = ['0','1','2']

    while choice not in acceptable_choices:

        choice = input("Pick a position (0,1,2): ")

        if choice not in acceptable_choices:
            print("Sorry, invalid choice!")

    return int(choice)

#position_choice()

def replacement_choice(game_list,position):

    user_choice = input("Type a string to place at position [{}]: ".format(position))

    game_list[position] = user_choice

    return game_list


def gameon_choice():

    choice = 'INVALID'
    acceptable_choices = ['Y','N']

    while choice not in acceptable_choices:

        choice = input("Keep playing? (Y or N): ").upper()

        if choice not in acceptable_choices:
            print("Sorry, I don't understand, please enter Y or N")

    if choice == "Y":
        return True
    else:
        return False


# Main game logic
game_on = True
game_list = [0,1,2]

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()


print('Game over, goodbye!')