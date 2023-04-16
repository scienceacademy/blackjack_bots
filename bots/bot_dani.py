class Bot:

    def __init__(self):
        self.seen = set()


    def blackjack_score(hand):  # calculates score of hand
        score = 0
        aces = 0
        for card in hand:
            if card.rank >= 2 and card.rank <= 9:
                score = score + card.rank
            if card.rank >= 10:
                score = score + 10
            if card.rank == 1:
                aces = aces + 1
        for i in range(aces):
            if score + 11 <= 21:
                score = score + 11
            elif score + 1 > 21:
                score = score - 9
            else:
                score = score + 1
        return score

    def certain_card_left(self, num):  # calculates how much of one card is left in the deck. For 10 it is 10 - K
        number = 0
        left = 0
        if num == 10:
            for card in self.seen:
                if card.rank >= int(num):
                    number = number + 1
            left = 16 - number
            return left
        else:
            for card in self.seen:
                if card.rank == int(num):
                    number = number + 1
            left = 4 - number
            return left

    def num_in_hand(hand, num):  # calculates how much of one card is in your hand
        number = 0
        for card in hand:
            if card.rank == int(num):
                number = number + 1
        return number

    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = Bot.blackjack_score(hand)
        self.seen.add(dealer_up_card)
        for card in dealer_prev_hand:
            self.seen.add(card)
        for card in hand:
            self.seen.add(card)
        num_tens = Bot.certain_card_left(self, 10)
        num_nine = Bot.certain_card_left(self, 9)
        num_eight = Bot.certain_card_left(self, 8)
        num_seven = Bot.certain_card_left(self, 7)
        num_six = Bot.certain_card_left(self, 6)
        num_aces = Bot.certain_card_left(self, 1)
        aces = Bot.num_in_hand(hand, 1)
        num_cards_seen = len(self.seen)
        num_cards_left = 52 - num_cards_seen
        chance_getting_highcard = (num_tens + num_aces)/ num_cards_left
        chance_getting_midcard = (num_seven + num_eight + num_nine) / num_cards_left
        chance_getting_lowcard = 1 - chance_getting_highcard - chance_getting_midcard
        if len(hand) == 2:
            if Bot.num_in_hand(hand, 8) == 2 or Bot.num_in_hand(hand, 1) == 2:
                return "split"
            if Bot.num_in_hand(hand, 10) == 2:
                return "stand"
            if Bot.num_in_hand(hand, 9) == 2:
                return "split"
            if Bot.num_in_hand(hand, 7) == 2:
                return "split"
            if Bot.num_in_hand(hand, 6) == 2:
                return "split"
            if Bot.num_in_hand(hand, 5) == 2:
                return "split"
            if Bot.num_in_hand(hand, 4) == 2:
                return "split"
            if Bot.num_in_hand(hand, 3) == 2:
                return "split"
            if Bot.num_in_hand(hand, 2) == 2:
                return "split"
        if aces == 0: # hard hands
            if score >= 4 and score <= 7:
                if Bot.num_in_hand(hand, 2) == 2 or Bot.num_in_hand(hand, 3) == 2:
                    if dealer_up_card.rank < 8:
                        return "split"
                else:
                    return "hit"
            if score == 8:
                if dealer_up_card.rank == 5 or dealer_up_card.rank == 6:
                    if Bot.num_in_hand(hand, 4) == 2:
                        return "split"
                    elif len(hand) == 2:
                        return "double down"
                else:
                    return "hit"
            if score == 9:
                if dealer_up_card.rank < 7 and dealer_up_card.rank >= 2 and len(hand) == 2:
                    return "double down"
                else:
                    return "hit"
            if score == 10:
                if dealer_up_card.rank < 10 and dealer_up_card.rank >= 2 and len(hand) == 2:
                    return "double down"
                else:
                    return "hit"
            if score == 11:
                if len(hand) == 2:
                    return "double down"
                else:
                    return "hit"
            if score == 12:
                if Bot.num_in_hand(hand, 6) == 2:
                    if dealer_up_card.rank < 7 and dealer_up_card.rank > 1:
                        return "split"
                    else:
                        return "hit"
                elif dealer_up_card.rank > 3 and dealer_up_card.rank < 7:
                    return "stand"
                else:
                    if chance_getting_highcard < chance_getting_lowcard + chance_getting_midcard:
                        return "hit"
                    else:
                        return "stand"
            if score == 13:
                chance_busting = (num_tens + num_nine)/ num_cards_left
                chance_not_busting = 1 - chance_busting
                #print("chance_busting")
                #print(chance_busting)
                if chance_busting < chance_not_busting:
                    return "hit"
                else:
                    return "stand"
            if score == 14:
                if Bot.num_in_hand(hand, 7) == 2:
                    if dealer_up_card.rank < 8 and dealer_up_card.rank > 1:
                        return "split"
                    else:
                        return "hit"
                else:
                    chance_busting = (num_tens + num_nine + num_eight)/ num_cards_left
                    chance_not_busting = 1 - chance_busting
                    #print("chance_busting")
                    #print(chance_busting)
                    if chance_busting < chance_not_busting:
                        return "hit"
                    else:
                        return "stand"
            if score == 15:
                chance_busting = (num_tens + num_nine + num_eight + num_seven)/ num_cards_left
                chance_not_busting = 1 - chance_busting
                #print("chance_busting")
                #print(chance_busting)
                if chance_busting < chance_not_busting:
                    return "hit"
                else:
                    return "stand"
            if score == 16:
                if Bot.num_in_hand(hand, 7) == 2:
                    return "split"
                else:
                    chance_busting = (num_tens + num_nine + num_eight + num_seven + num_six)/ num_cards_left
                    chance_not_busting = 1 - chance_busting
                    #print("chance_busting")
                    #print(chance_busting)
                    if chance_busting < chance_not_busting:
                        return "hit"
                    else:
                        return "stand"
            if score == 18:
                if Bot.num_in_hand(hand, 9) == 2:
                    if dealer_up_card.rank == 7 or dealer_up_card.rank >= 10 or dealer_up_card.rank == 1:
                        return "stand"
                    else:
                        return "split"
            if score >= 17:
                return "stand"

        if aces == 1: # soft hands
            if score <=16:
                if dealer_up_card.rank >=4 and dealer_up_card.rank <= 6 and len(hand) == 2:
                    return "double down"
                else:
                    return "hit"
            if score == 17:
                if dealer_up_card.rank >= 2 and dealer_up_card.rank <= 6 and len(hand) == 2:
                    return "double down"
                else:
                    return "hit"
            if score == 18:
                if dealer_up_card.rank >= 3 and dealer_up_card.rank <= 6 and len(hand) == 2:
                    return "double down"
                elif dealer_up_card.rank >= 9 or dealer_up_card.rank == 1:
                    return "hit"
                else:
                    return "stand"
            if score == 19:
                if chance_getting_highcard + chance_getting_midcard >= chance_getting_lowcard and dealer_up_card.rank == 6 and len(hand) == 2:
                    return "double down"
                else:
                    return "stand"
            if score > 19:
                return "stand"
        if aces == 2 and score == 12:
            return "split"
        else:
            if score >= 17:
                return "stand"
            else:
                return "hit"
