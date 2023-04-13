from cards import Card, Deck
from collections import Counter

ranks = ["","A", "2", "3", "4", "5", "6",
         "7", "8", "9", "10", "J", "Q", "K"]

bust_player = 0
most_card = 0
second_card = 0
num_card = 52
def blackjack_score(hand):
    #TODO: return the score of the hand
    score = 0
    aces = 0
    number_card = 0
    for card in hand:
        if card.rank >= 10:
            score = score + 10
        if card.rank >= 2 and card.rank <= 9:
            score = score + card.rank

        if card.rank == 1:
            score = score + 11
            aces = aces + 1

    for i in range(0,aces):
        if score > 21:
            score = score - 10
    return score

class Bot:
    def __init__(self):
        self.seen = set()
    def get_decision(self, dealer_up_card, hand, dealer_previous_hand):
        bust_player = 0
        numbers = []
        counter = {}
        num_card = 0
        self.seen.add(dealer_up_card)
        for card in dealer_previous_hand:
            self.seen.add(card)
        for card in hand:
            self.seen.add(card)

        for card in self.seen:
            if card.rank >= 10:
                numbers.append(10)
            else:
                numbers.append(card.rank)
        c = Counter(numbers)
        for i in range(1,11):
            if i == 10:
                c[i] = 16 - c[i]
            else:
                c[i] = 4-c[i]
        for i in range(1,11):
            num_card += c[i]
            if i + blackjack_score(hand) > 21:
                bust_player += c[i]
        for i in range(1,10):
            if c[i] > most_card:
                i = most_card
        for i in range(1,10):
            if i != most_card:
                if c[i] > second_card:
                    i = second_card
        if hand[0].rank == hand[1].rank :
            return "split"
        if 7 < blackjack_score(hand) < 12 and c[10]/num_card > .70:
            return "double down"
        if  3 < dealer_up_card.rank <= 6 and c[10]/num_card > .90:
            return "double down"
        if 14 < (dealer_up_card.rank + most_card) > 18:
            return "double down"


        if bust_player/num_card > .60:

            return "stand"

        else:
            return "hit"

