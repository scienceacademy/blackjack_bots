import io
import os
import sys
import importlib
import importlib.util
from cards import Deck, Card, Hand

class BlackjackGame:
    # This class handles playing the game between the bot and the dealer
    def __init__(self, bot):
        self.deck = Deck()
        self.bot_class = bot
        self.bot = bot()
        self.score = 0
        self.player = Hand()
        self.dealer = Hand()
        self.split_hands = []
        self.num_hands = 0
        self.dealer_last_hand = []

    def play_hand(self, hand):
        # This method plays one hand of Blackjack.
        hand.bet = 2
        self.num_hands += 1
        while True:
            # Ask the bot what it wants to do
            decision = self.bot.get_decision(self.dealer.get_cards()[0], hand.get_cards(), self.dealer_last_hand)
            if decision == "hit":
                hand.add_card(self.deck.deal_card())
                print(f"Hit: {hand.get_cards()[-1]}")
                if hand.get_bj_score() > 21:
                    break
            elif decision == "stand":
                break
            elif decision == "double down":
                if len(hand.get_cards()) == 2:
                    hand.add_card(self.deck.deal_card())
                    print(f"DD: {hand.get_cards()}")
                    if hand.get_bj_score() > 21:
                        break
                    self.score -= 2
                    hand.bet += 2
                    break
                else:
                    return
            elif decision == "split":
                if len(hand.get_cards()) == 2 and hand.get_cards()[0].rank == hand.get_cards()[1].rank:
                    self.score -= 2
                    new_hand = Hand()
                    new_hand.add_card(hand.deal_card())
                    new_hand.add_card(self.deck.deal_card())
                    hand.add_card(self.deck.deal_card())
                    self.split_hands.append(new_hand)
                else:
                    # print("can't split")
                    return

    def play_round(self):
        # Play one round, deal cards
        self.score -= 2
        self.player.clear()
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.split_hands = []
        self.dealer.clear()
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        print("-" * 20)
        print(f"Score: {self.score}")

        # Check for blackjacks
        player_bj = self.player.get_bj_score() == 21
        dealer_bj = self.dealer.get_bj_score() == 21
        if player_bj and dealer_bj:
            print("Push!")
            return
        elif player_bj:
            print("Blackjack!")
            self.score += 5
            return
        elif dealer_bj:
            print("Dealer blackjack!")
            self.dealer_last_hand = self.dealer.get_cards()
            return

        # Let the player play its hand
        self.play_hand(self.player)

        ## Play any split hands
        for hand in self.split_hands:
            self.play_hand(hand)

        # If player busted (including split hands), round is over
        busted = True
        if self.player.get_bj_score() <= 21:
            busted = False
        for hand in self.split_hands:
            if hand.get_bj_score() <= 21:
                busted = False
        if busted:
            print(f"Bust")
            self.dealer_last_hand = []
            return

        # Play the dealer's hand
        while self.dealer.get_bj_score() < 17:
            self.dealer.add_card(self.deck.deal_card())
        self.dealer_last_hand = self.dealer.get_cards()

        # Determine win/lose
        self.payout_hand(self.player)
        for hand in self.split_hands:
            self.payout_hand(hand)

    def payout_hand(self, hand):
        hand_score = hand.get_bj_score()
        if hand_score > 21:
            print("Busted")
            return
        dealer_score = self.dealer.get_bj_score()
        dealer_bust = dealer_score > 21
        print(f"Dealer: {self.dealer.get_cards()} - {'bust' if dealer_bust else dealer_score}")
        if dealer_bust or hand_score > dealer_score:
            print(f"Win!")
            self.score += hand.bet * 2
        elif hand_score < dealer_score:
            print(f"Lose")
            return
        elif hand_score == dealer_score:
            print(f"Push")
            self.score += hand.bet

    def play_game(self, games=100):
        for n in range(games):
            self.deck = Deck()
            self.deck.shuffle()
            self.bot = self.bot_class()
            self.dealer_last_hand = []
            while len(self.deck.get_cards()) > 20:
                self.play_round()
            print("==" * 20)
        return self.score, self.num_hands


if len(sys.argv) != 3:
    exit("Usage: python game_solo.py <bot_name.py> <N>")
filename = sys.argv[1]
N = int(sys.argv[2])

# load the bot
bot_path = os.path.join(".", filename)
bot_name = filename[5:-3]
bot_spec = importlib.util.spec_from_file_location(bot_name, bot_path)
bot_module = importlib.util.module_from_spec(bot_spec)
bot_spec.loader.exec_module(bot_module)
Bot = bot_module.Bot
print(f"loaded {Bot}")
Bot.name = Bot.__dict__['__module__']

# disable stdout
trap = io.StringIO()
sys.stdout = trap

# Start the game and play N times
game = BlackjackGame(Bot)
payout, num_hands = game.play_game(N)

sys.stdout = sys.__stdout__
# Results
print(f"{Bot.name} - Total: {payout} Avg: {payout / num_hands:.3f}")
