import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return "card is a " + self.rank + " of " + self.suit

class Deck:
    def __init__(self, rank, suit):
        self.card = Card(rank, suit)
        self.cards = []
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Ace", "King", "Queen", "Jack"]
        self.suit = ["Diamonds", "Clovers", "Hearts", "Spades"]

    def makeDeck(self, card):
        for i in self.ranks:
            for i in self.suit:
                card = Card(self.ranks, self.suit)
                self.cards.append(card)

