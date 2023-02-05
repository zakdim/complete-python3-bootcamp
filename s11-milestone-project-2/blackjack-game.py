from blackjack.model import domain as bj

playing = True


def take_bet(chips: bj.Chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break


def hit(deck: bj.Deck, hand: bj.Hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: bj.Deck, hand: bj.Hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter h/s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again")
            continue
        break


def show_cards(cards):
    if isinstance(cards, bj.Card):
        print(f'\t{cards}')
    elif isinstance(cards, list):
        # print('', *cards, sep='\n')
        for card in cards:
            print(f'\t{card}')


def show_some(player: bj.Hand, dealer: bj.Hand):
    # Show only one of the dealer's cards
    print("Dealer's Hand: ")
    print('First card is hidden!')
    show_cards(dealer.cards[1])

    # Show all (2 cards) of the player's hand
    print(f"Player's Hand: ")
    show_cards(player.cards)


def show_all(player: bj.Hand, dealer: bj.Hand):
    # Show all the dealer's cards
    print(f"Dealer's Hand: ")
    show_cards(dealer.cards)
    # Calculate and display value (J+K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # Show all the players cards
    print(f"Player's Hand: ")
    show_cards(player.cards)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()


def player_wins(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('DEALER BUSTS!')
    chips.win_bet()


def dealer_wins(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push(player: bj.Hand, dealer: bj.Hand):
    print("Dealer and player tie! It's a PUSH")


def play_game():
    global playing
    hand_num = 0
    player_chips = bj.Chips()
    while True:
        hand_num += 1
        # Print an opening statement
        print("WELCOME TO BLACKJACK hand: {}".format(hand_num))

        # Create & shuffle the deck, dela two cards to each player
        deck = bj.Deck()
        deck.shuffle()

        player_hand = bj.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = bj.Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        if hand_num > 1:
            player_chips.bet = 0    # On subsequent hand rounds only rest bet
        print(f"Player's chips: {player_chips}")

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:  # or < player_hand.value
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print("\nPlayer's total chips are at: {}".format(player_chips.total))

        # Ask to play again
        if player_chips.total > 0:
            new_game = input("Would you like to play another hand? y/n: ")
            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print('Thank you for playing!')
                break
        else:
            reset_game = input("You are out of chips, would you like to reset and play another hand? y/n: ")
            if reset_game[0].lower() == 'y':
                player_chips = bj.Chips()
                playing = True
                continue
            else:
                print('Thank you for playing!')
                break


if __name__ == "__main__":
    play_game()
else:
    print('blackjack-game.py has been imported')
