import random

def blackjack_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card.rank == 1:
            score += 11
            ace_count += 1
        elif card.rank >= 10:
            score += 10
        else:
            score += card.rank
    for i in range(ace_count):
        if score > 21:
            score-=10
    return score

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        hand_score = blackjack_score(hand)
        if dealer_up_card.rank == 1: #Ace
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "hit"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "hit"
                if hand[0].rank == 6:
                    return "hit"
                if hand[0].rank == 7:
                    return "hit"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "stand"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <= 10:
                return "hit"
            if hand_score == 11:
                return "double down"
            if hand_score <= 16 and hand_score >= 12:
                return "hit"
            if hand_score >= 17:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 2:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "hit"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "split"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=8:
                return "hit"
            if hand_score >= 9 and hand_score <= 11:
                return "double down"
            if hand_score == 12:
                return "hit"
            if hand_score >=13:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 3:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "split"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "split"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=8:
                return "hit"
            if hand_score >= 9 and hand_score <= 11:
                return "double down"
            if hand_score == 12:
                return "hit"
            if hand_score >=13:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 4:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "split"
                if hand[0].rank == 3:
                    return "split"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "split"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=8:
                return "hit"
            if hand_score >= 9 and hand_score <= 11:
                return "double down"
            if hand_score >= 12:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 5:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "split"
                if hand[0].rank == 3:
                    return "split"
                if hand[0].rank == 4:
                    return "double down"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "split"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=7:
                return "hit"
            if hand_score >= 8 and hand_score <= 11:
                return "double down"
            if hand_score >= 12:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 6:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "split"
                if hand[0].rank == 3:
                    return "split"
                if hand[0].rank == 4:
                    return "double down"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "split"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "double down"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=7:
                return "hit"
            if hand_score >= 8 and hand_score <= 11:
                return "double down"
            if hand_score >= 12:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 7:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "split"
                if hand[0].rank == 3:
                    return "split"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "hit"
                if hand[0].rank == 7:
                    return "split"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "stand"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=9:
                return "hit"
            if hand_score == 10:
                return "double down"
            if hand_score == 11:
                return "double down"
            if hand_score >= 12 and hand_score <= 16:
                return "hit"
            if hand_score >= 17:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 8:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "hit"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "hit"
                if hand[0].rank == 7:
                    return "hit"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=9:
                return "hit"
            if hand_score == 10:
                return "double down"
            if hand_score == 11:
                return "double down"
            if hand_score >= 12 and hand_score <= 16:
                return "hit"
            if hand_score >= 17:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank == 9:
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "hit"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "double down"
                if hand[0].rank == 6:
                    return "hit"
                if hand[0].rank == 7:
                    return "hit"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "split"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <=9:
                return "hit"
            if hand_score == 10:
                return "double down"
            if hand_score == 11:
                return "double down"
            if hand_score >= 12 and hand_score <= 16:
                return "hit"
            if hand_score >= 17:
                return "stand"

#--------------------------------------------------------------------------------------
        if dealer_up_card.rank >= 10: # Ten, Jack, Queen, King
            if len(hand) == 2 and hand[0].rank == hand[1].rank:
                if hand[0].rank == 1: #Ace
                    return "split"
                if hand[0].rank == 2:
                    return "hit"
                if hand[0].rank == 3:
                    return "hit"
                if hand[0].rank == 4:
                    return "hit"
                if hand[0].rank == 5:
                    return "hit"
                if hand[0].rank == 6:
                    return "hit"
                if hand[0].rank == 7:
                    return "stand"
                if hand[0].rank == 8:
                    return "split"
                if hand[0].rank == 9:
                    return "stand"
                if hand[0].rank >= 10:
                    return "stand"

            if len(hand) == 2 and hand[0].rank == 2 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 3 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 4 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 5 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 6 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 7 and hand[1].rank == 1:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 8 and hand[1].rank == 1:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 9 and hand[1].rank == 1:
                return "stand"

            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 2:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 3:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 4:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 5:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 6:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 7:
                return "hit"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 8:
                return "stand"
            if len(hand) == 2 and hand[0].rank == 1 and hand[1].rank == 9:
                return "stand"

            if hand_score <= 10:
                return "hit"
            if hand_score == 11:
                return "double down"
            if hand_score >= 12 and hand_score <= 16:
                return "hit"
            if hand_score >= 17:
                return "stand"
