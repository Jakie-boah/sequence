_SUITS = ('spades', 'hearts', 'diamonds', 'clubs')
_RANKS = tuple(range(2, 11)) + tuple('JQKA')

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')


class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length)

    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.reverse = reverse
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= self.length:
                raise StopIteration

            if self.reverse:
                index = self.length - 1 - self.index
            else:
                index = self.index

            suit = _SUITS[index // len(_RANKS)]
            rank = _RANKS[index % len(_RANKS)]

            self.index += 1
            return Card(rank, suit)


deck = CardDeck()
for card in deck:
    print(card)


class Squares:
    def __init__(self, length):
        self.squares = [i ** 2 for i in range(length)]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, index):
        return self.squares[index]

    def __reversed__(self):
        return 'Hello python!'
