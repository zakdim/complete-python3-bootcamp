from enum import Enum
import random


# Enum - class syntax
class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4


# Enum - functional syntax
Rank = Enum('Rank',
            ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE'])

card_values = {Rank.TWO: 2, Rank.THREE: 3, Rank.FOUR: 4, Rank.FIVE: 5, Rank.SIX: 6, Rank.SEVEN: 7, Rank.EIGHT: 8,
               Rank.NINE: 9, Rank.TEN: 10, Rank.JACK: 10, Rank.QUEEN: 10, Rank.KING: 10, Rank.ACE: 11}


# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
#           'Jack': 10,
#           'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return "Card(suit={}, rank={}, value={})".format(self.suit, self.rank, self.value)


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in Suit:
            for rank in Rank:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += f'{card}\n'

        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card: Card):
        """
        Card passed in from Deck.deal()
        :param card:
        :return:
        """
        self.cards.append(card)
        self.value += card.value

        # Track aces
        if card.rank == Rank.ACE:
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21, and I still have an ace than change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        deck_comp = f'Hand(value={self.value}, cards='
        if len(self.cards) == 0:
            deck_comp += '[])'
        else:
            deck_comp += '[\n'
            for i, card in enumerate(self.cards):
                deck_comp += f'\t{card}{"," if i + 1 < len(self.cards) else ""}\n'
            deck_comp += ']'

        return deck_comp


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        return f'Chips(total={self.total}, bet={self.bet})'
