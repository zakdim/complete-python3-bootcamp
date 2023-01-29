from blackjack.model import domain as bj

test_deck = bj.Deck()
print(f'Deck size: {len(test_deck.deck)}')
test_deck.shuffle()
print(f'{test_deck}')
