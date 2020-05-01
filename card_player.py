
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw(self, deck):
        card_draw = deck.draw()
        self.hand.append(card_draw)

    def show_hand(self):
        print("{} hand:".format(self.name))
        for card in self.hand:
            card.show()

    def assign_score(self, score):
        self.score = score
