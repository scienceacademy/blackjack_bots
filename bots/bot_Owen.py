def get_bj_score(hand):
    value = 0
    num_aces = 0
    for card in hand:
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

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        if get_bj_score(hand) > 17:
            return "stand"
        else:
            return "hit"
