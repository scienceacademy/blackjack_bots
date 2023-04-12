class Bot:
    def __init__(self):
        self.set = set()
    def get_decision(self, dealer_up_card, hand, prev_hand):
        true_count = 0
        points = 0
        ace = 0
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
                if points <= 10:
                    points += 11
            if ace == 2:
                if points > 9:
                    points += 2
                if points <= 9:
                    points += 12
            self.set.add(card)
        self.set.add(dealer_up_card)
        for i in self.set:
            if 2 <= i.rank <= 6:
                true_count += 1
            if (10 <= i.rank <= 13) or (i.rank == 1):
                true_count -= 1
        height = len(hand)
        if (len(hand) == 2) and (hand[0].rank == hand[1].rank):
            if hand[0].rank == 10:
                if (dealer_up_card.rank == 5) and (true_count >= 5):
                    return "split"
                if (dealer_up_card.rank == 6) and (true_count >= 5):
                    return "split"
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
            if (hand[0].rank == 7) and (2 <= dealer_up_card.rank <= 8):
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
        if ace == 0:
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
        if ace > 0:
            if points >= 20:
                return "stand"
            if points == 19:
                if ((1 <= dealer_up_card.rank <= 5) or (7 <= dealer_up_card.rank <= 13)):
                    return "stand"
                if (dealer_up_card.rank == 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "stand"
            if points == 18:
                if (3 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "stand"
                if ((7 <= dealer_up_card.rank <= 8) or (1 <= dealer_up_card.rank <= 2)):
                    return "stand"
                if (9 <= dealer_up_card.rank <= 13):
                    return "hit"
            if points == 17:
                if (2 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (dealer_up_card.rank == 1)):
                    return "hit"
            if points == 16:
                if (4 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (1 <= dealer_up_card.rank <= 3)):
                    return "hit"
            if points == 15:
                if (4 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (1 <= dealer_up_card.rank <= 3)):
                    return "hit"
            if points == 14:
                if (4 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (1 <= dealer_up_card.rank <= 3)):
                    return "hit"
            if points == 13:
                if (4 <= dealer_up_card.rank <= 6):
                    if (height == 2):
                        return "double down"
                    if (height > 2):
                        return "hit"
                if ((7 <= dealer_up_card.rank <= 13) or (1 <= dealer_up_card.rank <= 3)):
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
        else:
            return "stand"
