from blackjack.model import domain as bj

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
