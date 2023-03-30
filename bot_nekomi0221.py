def blackjack_score(hand):
    # TODO: return the score of the hand
    score = 0
    ace_count = 0
    for cards in hand:
        if cards.rank > 1 and cards.rank < 10:
            score += cards.rank
        if cards.rank > 9:
            score += 10
        if cards.rank == 1:
            ace_count += 1
    score = score + ace_count * 11
    while score > 21:
        score = score - 10
    return score
  
class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_previous_hand):
        if hand.score >= 17:
          return "stand"
        if card.rank = 1:
          if hand.score + 11 >= 17 and hand.score + 11 <= 21:
            hand.score += 11
            return "stand"
          else:
            hand.score += 1
            return "hit"
          else:
            return "hit"
Footer
