# A basic simple project using oop in python 
# WAR GAME:
#      RULES:
#   -->This game has two players
#   -->Each player throws a card and the one with highest value wins
#   -->First person to ran out of cards will be loser.
#   -->What if when both cards came out of same value....Here is when war declares
#   --> Now each of them has to keep down there five cards and the game continues like previous manner
#   --> The one gets more value in other rounds gets all these 10 cards..
#  --> I have designed this in such a way that the person has less then 5 cards then the opponent wins!!
import random
from random import shuffle
#suit 
suits=("Hearts","Diamonds","Clubs","Spades")
#rank
ranks=("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","jack","Queen", "King", "Ace")
#value : This is a global variable more like dict that wil be useful to set values for different ranks.
values={"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10,"jack":11,
        "Queen":12, "King":13, "Ace":14}

#card class:
# implemtations done in card class: we have seen the suit and rank then assign value to a particular rank
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank+' of '+self.suit 
    
#deck class: this deck will have all cards in terms of object 
#and this will be done by the card one which previously created card ka class
class Deck:
    
    def __init__(self):
        self.allcards=[]
        for suit in suits:
            for rank in ranks:
                create_card=Card(suit,rank)
                self.allcards.append(create_card)
    # now we will shuffle this deck
    def shuffle(self):
        random.shuffle(self.allcards)
    #grabbing one cards somewhere in the list pop is used to do soo
    def deal_one(self):
        return self.allcards.pop()
class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
#game logic: part 1
#game setup
player_one=Player("one")
player_two=Player("two")
new_deck=Deck()
new_deck.shuffle()
# len(new_deck.allcards)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
game_on=True
round_num=0
round_num=0
while game_on:
    round_num+=1
    print(f'round{round_num}')
    
    if len(player_one.all_cards)==0:
        print('player 1 is out of cards')
        print('player 2 wins')
        game_on=False
        break
        
        
    if len(player_two.all_cards)==0: 
        print('player 2 is out of cards')
        print('player 1 wins')
        game_on=False
        break
        
    # now the game is still onnn!!!
    playerone_cards=[]
    playerone_cards.append(player_one.remove_one())
    
    playertwo_cards=[]
    playertwo_cards.append(player_two.remove_one())
        
        
    
    
    
    at_war=True
    
    while at_war:
        if playerone_cards[-1].value > playertwo_cards[-1].value:
            
            player_one.add_cards(playerone_cards)
            player_one.add_cards(playertwo_cards)
            at_war=False
            
        elif playerone_cards[-1].value < playertwo_cards[-1].value:
            player_two.add_cards(playerone_cards)
            player_two.add_cards(playertwo_cards)
            at_war=False
            
        else:
            if len(player_one.all_cards)<5:
                print('Player 1 has less than 5 cards ')
                print('player 2 wins')
                game_on=False
                break
                
            if len(player_two.all_cards)<5:
                print('Player 2 has less than 5 cards')
                print('Player 1 wins')
                game_on=False
                break
            else:
                print('War')
                for i in range(5):
                    playerone_cards.append(player_one.remove_one())
                    playertwo_cards.append(player_two.remove_one())     