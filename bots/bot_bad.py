import random

class Bot:
    def get_decision(self, dealer_up_card, hand):
        if random.random() > 0.5:
            return "stand"
        else:
            return "hit"