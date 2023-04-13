class Bot:
    def blackjack_score(self, hand):
        score = 0
        score_count = 0
        for card in hand:
            if card.rank >= 2 and card.rank <= 10:
                score += card.rank
            if card.rank >= 11 and card.rank <= 13:
                score += 10
            if card.rank == 1 and score > 10:
                score += 1
            if card.rank == 1 and score <= 10:
                score += 11
                score_count += 11
        for card in hand:
            if score > 21 and card.rank == 1:
                if score_count >= 11:
                    score -= 10
        print(score)
        return score
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = self.blackjack_score(hand)
        if dealer_up_card.rank == 2 or dealer_up_card.rank == 3:
            if score == 12:
                return "hit"
        if len(hand) == 2 and (hand[0].rank == hand[1].rank):
            for card in hand:
                if card.rank == 8:
                    return "split"
                if card.rank == 1:
                    return "split"
                if score == 11:
                    return "double down"
            if score == 10:
                if dealer_up_card.rank <= 9:
                    return "double down"
        if score < 12:
            return "hit"
        if score == 12:
            if dealer_up_card.rank >= 4 and dealer_up_card.rank <= 6:
                return "stand"
            else:
                return "hit"
        if score == 13:
            if dealer_up_card.rank >= 2 and dealer_up_card.rank <= 6:
                return "stand"
            else:
                return "hit"
        if score == 14:
            if dealer_up_card.rank >= 2 and dealer_up_card.rank <= 6:
                return "stand"
            else:
                return "hit"
        if score == 15:
            if dealer_up_card.rank >= 2 and dealer_up_card.rank <= 6:
                return "stand"
            else:
                return "hit"
        if score == 16:
            if dealer_up_card.rank >= 2 and dealer_up_card.rank <= 6:
                return "hit"
            else:
                return "stand"
        if score >= 17:
            return "stand"
