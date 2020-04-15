import random


class Deck:
    def __init__(self):
        self.cards = []
        self.current_card = 0
        self.build()

    def build(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        for suit in suits:
            for num in range(1, 14):
                self.cards.append(Card(suit, num))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        drawn_card = self.cards[self.current_card]
        self.cards.remove(self.cards[self.current_card])
        return drawn_card

    def card_count(self):
        return len(self.cards)


class Card:

    value_map = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        1: 'Ace'
    }

    num_value = {
        11: 10,
        12: 10,
        13: 10,
        1: 1
    }

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        self.name = str(self.value_map.get(value, value)) + ' of ' + suit
        self.num_val = (self.num_value.get(value, value))

    def show(self):
        print(self.name)

    def return_value(self):
        return self.value
