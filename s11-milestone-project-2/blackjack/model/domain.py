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

rank_values = {Rank.TWO: 2, Rank.THREE: 3, Rank.FOUR: 4, Rank.FIVE: 5, Rank.SIX: 6, Rank.SEVEN: 7, Rank.EIGHT: 8,
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
        self.value = rank_values[rank]

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
