import random

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = 0
        ace_count = 0
        for card in hand:
            if card.rank > 1 and card.rank < 10:
                score += card.rank
            if card.rank > 9:
                score += 10
            if card.rank == 1:
                ace_count += 1
        score = score + ace_count * 11
        for i in range(ace_count):
            if score > 21:
                score = score - 10
                ace_count -= 1
        return score, ace_count
    def get_decision(self, dealer_up_card, hand):
        score, ace_count = self.blackjack_score(hand)
        if ace_count == 0:
            if score > 12 and score < 17 and dealer_up_card.rank < 7:
                return "stand"
            if score == 12 and dealer_up_card.rank > 3 and dealer_up_card.rank < 7:
                return "stand"
            if score > 16:
                return "stand"
            if score == 11:
                return "double down"
            if score == 10 and dealer_up_card.rank < 10:
                return "double down"
            if score == 9 and dealer_up_card.rank > 2 and dealer_up_card.rank < 7:
                return "double down"
            else:
                return "hit"
        if ace_count == 1:
            if score == 20:
                return "stand"
            if score == 19 and dealer_up_card.rank < 6 and dealer_up_card.rank > 6:
                return "stand"
            if score == 19 and dealer_up_card.rank == 6 and len(hand) == 2:
                return "double down"
            if score == 19 and dealer_up_card.rank == 6 and len(hand) > 2:
                return "stand"
            if score == 18 and dealer_up_card.rank < 7 and len(hand) == 2 :
                return "double down"
            if score == 18 and dealer_up_card.rank < 7 and len(hand) > 2:
                return "stand"
            if score == 18 and dealer_up_card.rank == 7 or dealer_up_card.rank == 8:
                return "stand"
            if score == 17 and 2 < dealer_up_card.rank < 7:
                return "double down"
            if score == 16 and 3 < dealer_up_card.rank < 7:
                return "double down"
            if score == 15 and 3 < dealer_up_card.rank < 7:
                return "double down"
            if score == 14 and 4 < dealer_up_card.rank < 7:
                return "double down"
            if score == 13 and 4 < dealer_up_card.rank < 7:
                return "double down"
            else:
                return "hit"
        if len(hand) == 2 and hand[0].rank == hand[1].rank:
            if hand[0].rank == 1:
                return "split"
            if hand[0].rank == 9 and dealer_up_card != 7 or dealer_up_card > 9:
                return "split"
            if hand[0].rank == 8:
                return "split"
            if hand[0].rank == 7 and dealer_up_card <=7:
                return "split"
            if hand[0].rank == 6 and dealer_up_card <= 6:
                return "split"
            if hand[0].rank == 4 and dealer_up_card == 5 or dealer_up_card == 6:
                return "split"
            if hand[0].rank == 3 and dealer_up_card <= 7:
                return "split"
            if hand[0].rank == 2 and dealer_up_card <= 7:
                return "split"
