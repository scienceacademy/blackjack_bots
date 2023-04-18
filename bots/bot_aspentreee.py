def __init__(self):
        self.seen = set()
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        points = 0
        aces = 0
        eleven = 0
        for card in hand:
            if 2 <= card.rank <= 10:
                points += card.rank
            if 11 <= card.rank <= 13:
                points += 10
            if card.rank == 1:
                aces += 1
        if aces == 1:

if points > 10:
                points += 1
            elif points <= 10:
                points += 11
                eleven += 1
        if aces == 2:
            if points > 9:
                points += 2
            elif points <= 9:
                points += 12
                eleven += 1
        if aces == 3:
            if points > 8:
                points += 3
            elif points <= 8:
                points += 13
                eleven += 1
        if aces == 4:
            if points > 7:
                points += 4
            elif points <= 7:
                points += 14
                eleven += 1
        bust_player = 0
        numbers = []
        counter = {}
        num_card = 0
        self.seen.add(dealer_up_card)
        for card in dealer_prev_hand:
            self.seen.add(card)
