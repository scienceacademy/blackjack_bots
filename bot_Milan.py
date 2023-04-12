import random

class Bot:
    def blackjack_score(self, hand):
        score = 0
        ace_count = 0
        for card in hand:
            if card.rank > 10:                                          # if royal
                score += 10
            if card.rank > 1 and card.rank < 11:                        # if 2 through 10
                score += card.rank
            if card.rank == 1:                                          # if ace
                score += 11
                ace_count += 1
        while True:
            if score > 21 and ace_count >= 1:
                score -= 10
                ace_count -= 1
            else:
                break
        return score

    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = self.blackjack_score(hand)
        if hand[0].rank == hand[1].rank and len(hand) == 2:              # if first 2 cards are the same
            if dealer_up_card.rank >= 7:
                if score >= dealer_up_card.rank + 10:
                    return "stand"
                else:
                    if score + 10 >= dealer_up_card.rank + 10:
                        return "hit"
                    else:
                        return "split"
            elif dealer_up_card.rank == 1:
                if score <=8 or score == 18:
                    return "split"
                else:
                    if score >= 18:                                     # if card is greater than 18, stand
                        return "stand"
                    else:
                        return "hit"
            else:
                if score >= 18:
                    return "stand"
                else:
                    return "split"
        else:
            if dealer_up_card.rank >=4 and dealer_up_card.rank <= 6:    # dealer high chance of busting
                if score <= 11:                                         # double down if score is less than 12
                    return "double down"
                else:                                                   # have more than 11
                    return "stand"
            elif dealer_up_card.rank >= 7 or dealer_up_card.rank == 1:   # dealer high chance of winning
                if score >= 17:                                         # if card is greater than 17, stand
                    return "stand"
                else:
                    return "hit"

            else:                                                       # dealer showing 2 or 3
                if score >= 13:
                    return "stand"
                else:
                    return "hit"
