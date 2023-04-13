class Bot:

    def blackjack_score(self, hand):
        score = 0
        acecount = 0
        for card in hand:
            if card.rank > 10:
                score += 10
            if card.rank > 1 and card.rank < 11:
                score += card.rank
            if card.rank == 1:
                score += 11
                acecount += 1
        while True:
            if score > 21 and acecount >= 1:
                score -= 10
                acecount -= 1
            else:
                break
        return score

    def get_decision(self, dealer_up_card, hand, dealer_previous_hand):
        selfscore = self.blackjack_score(self, hand)
        if hand[0].rank == hand[1].rank and len(hand) == 2: #1st two cards same
            if hand[0].rank == 1 and hand[1].rank == 1 or hand[0].rank == 8 and hand[1].rank == 8:
                return "split"
            if hand[0].rank == 9 and hand[1].rank == 9:
                if dealer_up_card.rank == 7:
                    return "stand"
                if dealer_up_card.rank >= 2 and dealer_up_card.rank <=6 and dealer_up_card.rank == 8 and dealer_up_card.rank == 9:
                    return "double down"
        if dealer_up_card.rank == 5: 
            if selfscore >= 14: 
                return "stand"
            if selfscore <= 13: 
                return "hit"
        if selfscore == 11:
            return "double down"
        if dealer_up_card.rank > 1 and dealer_up_card.rank <= 3: 
            if selfscore <= 12:
                return "hit"
            else:
                return "stand"
        if dealer_up_card.rank == 1 or dealer_up_card.rank == 7: 
            if selfscore <= 17:
                return "hit"
            else:
                return "stand"
        if dealer_up_card.rank >= 4 and dealer_up_card.rank <= 6: 
            if selfscore <= 11: 
                return "hit"
            else:
                return "stand"
        if dealer_up_card.rank >= 8:
            if selfscore > 17:
                return "stand"
            else:
                return "hit"
        if dealer_up_card.rank == 9 or dealer_up_card.rank == 10 or dealer_up_card.rank == 1: # 9, 10, 1
            if selfscore == 18:
                return "hit"
        if dealer_up_card.rank <= 9: 
            if selfscore == 10:
                return "double down"
        if dealer_up_card == 5 or dealer_up_card == 6:
            if selfscore >= 13 and selfscore <= 18:
                return "double down"
