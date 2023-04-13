#Setup
import os
import codecs
ranks = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["♥","♣","♠","♦"]
bj_hard_player_lookup = {5:0,6:0,7:0,8:1,9:2,10:3,11:4,12:5,13:6,14:7,15:8,16:9,17:10,18:10,19:10,20:10,21:10}
bj_soft_player_lookup = {13:0,14:1,15:2,16:3,17:4,18:5,19:6,20:7,21:7}
bj_hard_dealer_lookup = {2:0,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:8,12:8,13:8,1:9}
bj_split_player_lookup = {2:0,3:1,4:2,6:3,7:4,8:5,9:6,1:7}
bj_hard =       [['H','H','H','H','H','H','H','H','H','H'],
                 ['H','H','H','D','D','H','H','H','H','H'],
                 ['D','D','D','D','D','H','H','H','H','H'],
                 ['D','D','D','D','D','D','D','D','H','H'],
                 ['D','D','D','D','D','D','D','D','D','D'],
                 ['H','H','S','S','S','H','H','H','H','H'],
                 ['S','S','S','S','S','H','H','H','H','H'],
                 ['S','S','S','S','S','H','H','H','H','H'],
                 ['S','S','S','S','S','H','H','H','H','H'],
                 ['S','S','S','S','S','H','H','H','H','H'],
                 ['S','S','S','S','S','S','S','S','S','S']]
bj_split =      [['P','P','P','P','P','P','H','H','H','H'],
                 ['P','P','P','P','P','P','P','H','H','H'],
                 ['H','H','P','P','P','H','H','H','H','H'],
                 ['P','P','P','P','P','P','H','H','H','H'],
                 ['P','P','P','P','P','P','P','H','S','H'],
                 ['P','P','P','P','P','P','P','P','P','P'],
                 ['P','P','P','P','P','S','P','P','S','S'],
                 ['P','P','P','P','P','P','P','P','P','P']]
bj_soft =       [['H','H','D','D','D','H','H','H','H','H'],
                 ['H','H','D','D','D','H','H','H','H','H'],
                 ['H','H','D','D','D','H','H','H','H','H'],
                 ['H','H','D','D','D','H','H','H','H','H'],
                 ['D','D','D','D','D','H','H','H','H','H'],
                 ['S','E','E','E','E','S','S','H','H','S'],
                 ['S','S','S','S','E','S','S','S','S','S'],
                 ['S','S','S','S','S','S','S','S','S','S']]
#stand is 1
#double down is 2

illus={(11, 1): [-4, 1], (12, 5): [-2, 2], (13, 2): [9, 2], (16, 9): [10, 1], (16, 13): [8, 2], (10, 12): [11, 1], (15, 11): [3, 2], (10, 7): [1, 2], (11, 11): [10, 2], (17, 12): [6, 1], (15, 13): [11, 2], (11, 3): [3, 1], (11, 4): [1, 1], (15, 10): [9, 1], (16, 10): [0, 2], (9, 8): [9, 1]}
#Card Class
class Card:
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{suits[self.suit]}{ranks[self.rank]}"
    def __eq__(self,other):
        return self.suit==other.suit and self.rank==other.rank


#helpful functions
def hilo(card):
    if card.rank >= 2 and card.rank <= 6:
        return 1
    elif card.rank>= 10 or card.rank==1:
        return -1
    else:
        return 0
def wong(card):
    if card.rank==18 or card.rank==7:
        return 20
    elif card.rank>= 10 or card.rank==1:
        return -1
    elif card.rank>= 3 and card.rank<=6:
        return 1
    elif card.rank==9:
        return -0.5
    else:
        return 0
def omegaII(card):
    if card.rank==2 or card.rank==7 or card.rank==3:
        return 1
    elif card.rank>= 10:
        return -2
    elif card.rank>= 4 and card.rank<=6:
        return 1
    elif card.rank==9:
        return -1
    else:
        return 0
def hiOptII(card):
    if card.rank==2 or card.rank==3 or card.rank==6 or card.rank==7:
        return 1
    elif card.rank==4 or card.rank==5:
        return 2
    elif card.rank>= 10:
        return -2
    else:
        return 0
def blackjack_score(hand):
        value = 0
        num_aces = 0
        b="HARD"
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
        if num_aces==0:
            b="HARD"
        else:
            b="SOFT"
        return [value,b]

#{(9, 7): [8, 2], (11, 1): [-2, 1], (12, 3): [2, 1], (12, 4): [2, 2], (12, 5): [-2, 2], (13, 2): [1, 2], (16, 9): [12, 1], (16, 10): [9, 2], (16, 11): [1, 2], (16, 13): [8, 2], (10, 11): [6, 1], (10, 12): [10, 1], (15, 11): [5, 2], (15, 12): [12, 2], (12, 2): [9, 2], (10, 7): [1, 1], (11, 11): [9, 1], (17, 12): [5, 1]}
#the bot itself
class Bot:
    card_count=0
    running_total=0.0
    true_total=0.0
    deckR=[]
    def __init__(self):
        self.deckR=[]
        for suit in range(4):
            for rank in range(1,14):
                self.deckR.append(Card(suit,rank))
        self.card_count=0
        self.running_total=0.0
        self.true_total=0.0
    def get_decision(self,dealer_up_card,hand,prev_hand):
        #print("Dealer-up: " + str(dealer_up_card))
        #print("Score: " + str(hand))
        #print("Previous Hand: " + str(prev_hand))
        for i in hand:
            if i in self.deckR:
                self.running_total+=hiOptII(i)
                self.deckR.remove(i)
                self.card_count+=1
        for i in prev_hand:
            if i in self.deckR:
                self.running_total+=hiOptII(i)
                self.deckR.remove(i)
                self.card_count+=1
        if dealer_up_card in self.deckR:
            self.running_total+=hiOptII(dealer_up_card)
            self.deckR.remove(dealer_up_card)
        self.card_count+=1
        self.true_total=(self.running_total)*((1-self.card_count)/52)
        des=""
        #print("Running Count: " + str(self.running_total))
        score=blackjack_score(hand)
        if len(hand)==2 and hand[0].rank==hand[1].rank and hand[0].rank < 10 and hand[0].rank!=5:
            des=bj_split[bj_split_player_lookup[hand[0].rank]][bj_hard_dealer_lookup[dealer_up_card.rank]]
        elif len(hand)==2 and hand[0].rank==hand[1].rank and hand[0].rank >= 10:
            if dealer_up_card.rank==5 and self.true_total>8:
                des = "P"
            elif dealer_up_card == 6 and self.true_total>7:
                des = "P"
            else:
                des=bj_hard[bj_hard_player_lookup[score[0]]][bj_hard_dealer_lookup[dealer_up_card.rank]]
        elif score[1]=="SOFT":
            des=bj_soft[bj_soft_player_lookup[score[0]]][bj_hard_dealer_lookup[dealer_up_card.rank]]
        else:
            des=bj_hard[bj_hard_player_lookup[score[0]]][bj_hard_dealer_lookup[dealer_up_card.rank]]
        if des=="H":
            if (score[0],dealer_up_card.rank) in illus:
                sub=illus[(score[0],dealer_up_card.rank)]
                if self.true_total>=sub[0]:
                    if sub[1]==1:
                        return "stand"
                    elif sub[1]==2:
                        if len(hand)==2:
                            return "double down"
                        else:
                            return "hit"
            return "hit"
        elif des=="S":
            return "stand"
        elif des=="D":
            if len(hand)==2:
                #print("Double down.")
                return "double down"
            else:
                #print("Stand.")
                return "hit"
        elif des=="E":
            if len(hand)==2:
                #print("Double down.")
                return "double down"
            else:
                #print("Stand.")
                return "stand"
        elif des=="P":
            #print("Split.")
            return "split"



