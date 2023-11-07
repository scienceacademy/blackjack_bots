import random

ranks = ["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

suits = ["♥", "♣", "♠", "♦"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{ranks[self.rank]} of {suits[self.suit]}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
    def deal_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        has_ace = False
        for card in self.cards:
            if card.rank == 1:
                has_ace = True
            value += min(card.rank, 10)
        if has_ace and value <= 11:
            value += 10
        return value

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for i in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def play(self):
        print("Player's hand: ", self.player_hand)
        print("Dealer's hand: ", self.dealer_hand.cards[0])
        while True:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player_hand.add_card(self.deck.deal_card())
                print("Player's hand: ", self.player_hand)
                if self.player_hand.get_value() > 21:
                    print("Bust! You lose.")
                    return
            elif choice.lower() == "stand":
                dealer_value = self.dealer_hand.get_value()
                while dealer_value < 17:
                    self.dealer_hand.add_card(self.deck.deal_card())
                    dealer_value = self.dealer_hand.get_value()
                print("Dealer's hand: ", self.dealer_hand)
                if dealer_value > 21:
                    print("Dealer bust! You win.")
                elif dealer_value > self.player_hand.get_value():
                    print("Dealer wins!")
                elif dealer_value < self.player_hand.get_value():
                    print("You win!")
                else:
                    print("It's a tie!")
                return
            else:
                print("Invalid choice. Please try again.")
