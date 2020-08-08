import math
import random

class Card:
    #def __init__(self, number, suit):
    #    self.suit = suit
    #    self.number = number

    def __init__(self, card_num):
        self.suit=num2suit(math.ceil(card_num/14))
        if (card_num%14==0):
            self.number=num2value(14)
        else:
            self.number=num2value(card_num%14)
    
        self.card_name= self.number+" of "+self.suit
    def print_card(self):
        print("This card is", self.card_name , "\n")

class Player:

    def __init__(self, name):
        self.hand=[]
        self.score=0
        self.name=name
    
    def deal_hand(self, new_hand):
        self.hand=new_hand

    def print_hand(self):
        print("Hand of", self.name,":")
        count=1
        for x in self.hand:
            my_card=Card(x)
            print("\tCard", count,": ", my_card.card_name)
            count=count+1

class Vault:

    def __init__(self):
        self.hand=[]
    
    def deal_hand(self, new_hand):
        self.hand=new_hand

    def print_vault(self):
        print("Vault:")
        count=1
        for x in self.hand:
            my_card=Card(x)
            print("\tCard", count,": ", my_card.card_name)
            count=count+1
    


class Deck:

    def __init__(self):
        game_deck=[]
        for x in range(2,57):
            if(x%14!=1):
                game_deck.append(x)
        self.game_deck=game_deck

    def deal_player(self,player):
        hand=[]
        for x in range(0, 16):
            new_card=random.choice(self.game_deck)
            self.game_deck.remove(new_card)
            hand.append(new_card)
        player.deal_hand(hand)
        player.print_hand()
    
    def deal_vault(self,vault):
        hand=[]
        for x in range(0, 4):
            new_card=random.choice(self.game_deck)
            self.game_deck.remove(new_card)
            hand.append(new_card)
        vault.deal_hand(hand)
        vault.print_vault()

    
    def print_deck(self):
        print("Cards in Deck:")
        count=1
        for x in self.game_deck:
            my_card=Card(x)
            print("\tCard", count,": ", my_card.card_name)
            count=count+1

    def deal(self, player1, player2, player3, vault):
        self.deal_player(player1)
        self.deal_player(player2)
        self.deal_player(player3)
        self.deal_vault(vault)


def suit2num(suit):
    if (suit=="Diamonds"):
        return 1
    elif (suit=="Clubs"):
        return 2
    elif (suit=="Hearts"):
        return 3
    elif (suit=="Spades"):
        return 4
    return 0

def num2suit(num):
    if (num==1):
        return "Diamonds"
    elif (num==2):
        return "Clubs"
    elif (num==3):
        return "Hearts"
    elif (num==4):
        return "Spades"
    return 0

def value2num(value):
    if (value=="Jack"):
        return 11
    elif (value=="Queen"):
        return 12
    elif (value=="King"):
        return 13
    elif (value=="Ace"):
        return 14
    else:
        return int(value)
    return 0

def num2value(num):
    if (num<11 and num>1):
        return str(num)
    elif (num==11):
        return "Jack"
    elif (num==12):
        return "Queen"
    elif (num==13):
        return "King"
    elif (num==14):
        return "Ace"
    return 0


def main():
    #hand=[]
    random.seed(0)
    my_deck=Deck()
    my_deck.print_deck()
    first_player=Player("Kagan")
    second_player=Player("Batuhan")
    third_player=Player("Seniha")
    game_vault=Vault()
    my_deck.deal(first_player,second_player,third_player,game_vault)

    #same = False
    #for vault_card in game_vault.hand:
    #    if(vault_card in first_player.hand or vault_card in second_player.hand or vault_card in third_player.hand):
    #        same=True
    #print(same)

if __name__ == "__main__":
    # execute only if run as a script
    main()


