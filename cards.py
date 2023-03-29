import random
ranks = ["", "A", "2", "3", "4", "5", "6",
         "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♣", "♠", "♦"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{ranks[self.rank]}{suits[self.suit]}"
    def __repr__(self):
         return f"{ranks[self.rank]}{suits[self.suit]}"

class Hand:
    def __init__(self):
        self._cards = []

    def __str__(self):
        return str(self._cards)

    def add_card(self, card):
        self._cards.append(card)

    def remove_card(self, card):
        self._cards.remove(card)

    def get_cards(self):
        return self._cards.copy()

    def clear(self):
        self._cards.clear()

    def deal_card(self):
        return self._cards.pop()

    def get_bj_score(self):
        value = 0
        num_aces = 0
        for card in self._cards:
            if card.rank >= 10:
                value += 10
            elif card.rank > 1:
                value += card.rank
            elif card.rank == 1:
                num_aces += 1
                value += 11
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1
        return value

class Deck(Hand):
    def __init__(self):
        super().__init__()
        for s in range(4):
            for r in range(1, 14):
                self._cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self._cards)
