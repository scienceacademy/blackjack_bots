class Bot:
    def __init__(self):
        self.seen = set()

    def get_decision(self, dealer_up_card, hand, dealer_previous_hand):
        self.seen.add(dealer_up_card)
        for card in dealer_previous_hand:
            self.seen.add(card)
        for card in hand:
            self.seen.add(card)
        print(f"Dealer showing: {dealer_up_card}")
        print(f"Your hand: {hand}")
        print(f"Seen: {self.seen}")
        choice = input("Move: ")
        return choice
