import random
from card import suits,ranks,Card

class Deck:
    def __init__(self):
        self.all_cards = []
        # self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()