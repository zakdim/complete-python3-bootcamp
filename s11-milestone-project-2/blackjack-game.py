from blackjack.model import domain as bj

playing = True


def take_bet(chips: bj.Chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))


def hit(deck: bj.Deck, hand: bj.Hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: bj.Deck, hand: bj.Hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter h or s ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again")


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
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(player: bj.Hand, dealer: bj.Hand, chips: bj.Chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push():
    print('Dealer and player tie! PUSH')


test_deck = bj.Deck()
print(f'Deck size: {len(test_deck.deck)}')
test_deck.shuffle()
# print(f'{test_deck}')

# PLAYER
test_player = bj.Hand()
print(f'{test_player}')

# Deal 1 card from the deck Card(suit, rank)
test_player.add_card(test_deck.deal())
print(f'{test_player}')
print(f'Deck size: {len(test_deck.deck)}')

test_player.add_card(test_deck.deal())
print(f'{test_player}')
print(f'Deck size: {len(test_deck.deck)}')

dealer = bj.Hand()
dealer.add_card(test_deck.deal())
dealer.add_card(test_deck.deal())

show_some(test_player, dealer)
show_all(test_player, dealer)
