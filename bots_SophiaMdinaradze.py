class Bot:
    def blackjack_score(self, hand):
        score = 0
        ace = 0
        loopnum = 0
        for card in hand:
            if card.rank < 11 and card.rank != 1:
                score += card.rank
            if card.rank > 10:
                score += 10
            if card.rank == 1:
                ace += 1
                score += 11
            for i in range(ace):
                if score > 21:
                    score = score - 10
                    loopnum += 1
        return score, ace - loopnum
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score, soft = self.blackjack_score(hand)
        print(f"{hand} {score} {soft}" )
        if hand[0].rank == hand[1].rank and len(hand) == 2:
            if score >= 8 or score <= 14:
                return "hit"
            if score == 4 or score == 6 and dealer_up_card >= 3 and dealer_up_card <= 7:
                return "split"
            if score == 4 or score == 6 and dealer_up_card < 3 or dealer_up_card > 7:
                return "hit"
            if score == 16:
                return "split"
            if score == 20:
                return "stand"
            if score == 18:
                if dealer_up_card >= 2 and dealer_up_card <= 6:
                    return "split"
                if dealer_up_card == 8 or dealer_up_card == 9:
                    return "split"
                else:
                    return "stand"
            if score == 11:
                return "split"

        else:
            if score == 11 :
                    return "double down"
            if soft == 0:
                if score > 15 and score != 11:
                    return "stand"
                if score <= 15:
                    return "hit"
            #hard aces and soft aces
            if soft != 0:
                if score < 12:
                    return "hit"
                if score >= 13 and score <= 15:
                    return "hit"
                if score == 9 or score == 10 and dealer_up_card < score:
                    return "double down"
                if score >= 15:
                    return "stand"
                if score > 15 and score <= 18:
                    return "double down"
                if score == 15 or score >= 19:
                    return "stand"
