import random

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        if random.random() > 0.5:
            return "stand"
        else:
            return "hit"
