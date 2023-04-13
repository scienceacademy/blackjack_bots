from cards import Card, Deck
from collections import Counter
ranks = ["","A", "2", "3", "4", "5", "6",
         "7", "8", "9", "10", "J", "Q", "K"]
bust_player = 0
most_card = 0
second_card = 0
num_card = 52
class Bot:
    def __init__(self):
        self.seen = set()
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        points = 0
        ace = 0
        eleven = 0
        for card in hand:
            if 2 <= card.rank <= 10:
                points += card.rank
            if 11 <= card.rank <= 13:
                points += 10
            if card.rank == 1:
                ace += 1
        if ace == 1:
            if points > 10:
                points += 1
            elif points <= 10:
                points += 11
                eleven += 1
        if ace == 2:
            if points > 9:
                points += 2
            elif points <= 9:
                points += 12
                eleven += 1
        if ace == 3:
            if points > 8:
                points += 3
            elif points <= 8:
                points += 13
                eleven += 1
        if ace == 4:
            if points > 7:
                points += 4
            elif points <= 7:
                points += 14
                eleven += 1
        bust_player = 0
        numbers = []
        counter = {}
        num_card = 0
        self.seen.add(dealer_up_card)
        for card in dealer_prev_hand:
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
            if i + points > 21:
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
        if 7 < points < 12 and c[10]/num_card > .70:
            return "double down"
        if  3 < dealer_up_card.rank <= 6 and c[10]/num_card > .90:
            return "double down"
        if 14 < (dealer_up_card.rank + most_card) > 18:
            return "double down"
        if bust_player/num_card > .60:
            return "stand"
        height = len(hand)
        if (height == 2) and (hand[0].rank == hand[1].rank):
            if hand[0].rank == 1:
                return "split"
            if (hand[0].rank == 9):
                if (2 <= dealer_up_card.rank <= 6) or (8 <= dealer_up_card.rank <= 9):
                    return "split"
                if ((dealer_up_card.rank == 7) or (10 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "stand"
            if hand[0].rank == 8:
                return "split"
            if (hand[0].rank == 7):
                if (2 <= dealer_up_card.rank <= 8):
                    return "split"
                if ((dealer_up_card.rank == 9) or (dealer_up_card.rank == 1)):
                    return "hit"
                if (10 <= dealer_up_card.rank <= 13):
                    return "stand"
            if (hand[0].rank == 6):
                if (2 <= dealer_up_card.rank <= 7):
                    return "split"
                if ((8 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if (hand[0].rank == 5):
                if (2 <= dealer_up_card.rank <= 9):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((10 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if (hand[0].rank == 4):
                if (4 <= dealer_up_card.rank <= 6):
                    return "split"
                if ((7 <= dealer_up_card.rank <= 13) or (1 <= dealer_up_card.rank <= 3)):
                    return "hit"
            if (hand[0].rank == 3):
                if (2 <= dealer_up_card.rank <= 8):
                    return "split"
                if ((9 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if (hand[0].rank == 2):
                if (2 <= dealer_up_card.rank <= 7):
                    return "split"
                if ((8 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
        if eleven > -100:
            if points >= 17:
                return "stand"
            if points == 16:
                if (2 <= dealer_up_card.rank <= 6):
                    return "stand"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 15:
                if (2 <= dealer_up_card.rank <= 6):
                    return "stand"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 14:
                if (2 <= dealer_up_card.rank <= 6):
                    return "stand"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 13:
                if (2 <= dealer_up_card.rank <= 6):
                    return "stand"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 12:
                if (4 <= dealer_up_card.rank <= 6):
                    return "stand"
                if ((1 <= dealer_up_card.rank <= 3) or (7 <= dealer_up_card.rank <= 13)):
                    return "hit"
            if points == 11:
                if (height == 2):
                    return "double down"
                if (height > 2):
                    return "hit"
            if points == 10:
                if (2 <= dealer_up_card.rank <= 9):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((10 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 9:
                if (2 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 8:
                if ((1 <= dealer_up_card.rank <= 4) or (7 <= dealer_up_card.rank <= 13)):
                    return "hit"
                if (5 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
            if points <= 7:
                return "hit"
