import random

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.totalCards = 0

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, index):
        del self.cards[index]

    def get_card(self, index):
        if 0 <= index < len(self.cards):
            return self.cards[index]
        else:
            return -1         
        
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def get_length(self):
        return len(self.cards)
