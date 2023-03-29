class Bot:

    def get_decision(self, dealer_up_card, hand):

        print(f"Dealer showing: {dealer_up_card}")
        print(f"Your hand: {hand}")
        choice = input("Move: ")
        return choice