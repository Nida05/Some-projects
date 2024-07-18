import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                mycard = Card(suit, rank)
                self.allcards.append(mycard)
    
    def shuffling(self):
        random.shuffle(self.allcards)
        
    def deal_one(self):
        singlecard = self.allcards.pop()
        return singlecard

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.aces += 1
        self.value += card.value
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter your bet amount in numbers: '))
        except ValueError:
            print("Please enter a correct value")
        else:
            if chips.bet > chips.total:
                print("You ran out of coins, your total coins are: {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing
    
    while True:
        play = input("Enter hit or stand: ")
        if play.lower() == "hit":
            hit(deck, hand)
        elif play.lower() == "stand":
            playing = False
            print('Player stands, now Dealer plays')
        else:
            print('Sorry, can you enter again?')
            continue
        break

def show_some(player, dealer):
    print("Dealer's Hand:\n")
    print(dealer.cards[1])
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)
    
def show_all(player, dealer):
    print('After both the player and dealer take a stand')
    print("Dealer's Hand:\n")
    for card in dealer.cards:
        print(card)
    print("Dealer's Hand value:", dealer.value)
    print("Player's Hand:\n")
    for card in player.cards:
        print(card)
    print("Player's Hand value:", player.value)

def player_busts(player, chips, dealer):
    print("Oops! Player busts, Dealer wins")
    chips.lose_bet()

def player_wins(player, chips, dealer):
    print("Yay!! Player wins")
    chips.win_bet()

def dealer_busts(player, chips, dealer):
    print("Oops! Dealer busts, Player wins")
    chips.win_bet()  

def dealer_wins(player, chips, dealer):
    print("Dealer wins")
    chips.lose_bet() 

def push(player, chips, dealer):
    print("Dealer and Player tie! It's a push.") 

while True:
    print("Welcome to this game")
    player_chips = Chips()
    if player_chips.total<=0:
        print("Sorry u can not play!!")
        
        
    mydeck = Deck()
    mydeck.shuffling()
    
    player = Hand()
    player.add_card(mydeck.deal_one())
    player.add_card(mydeck.deal_one())
    
    dealer = Hand()
    dealer.add_card(mydeck.deal_one())
    dealer.add_card(mydeck.deal_one())
    
    
    take_bet(player_chips)
    
    show_some(player, dealer)
    
    while playing:
        hit_or_stand(mydeck, player)
        show_some(player, dealer)
        
        if player.value > 21:
            player_busts(player, player_chips, dealer)
            break
    
    if player.value <= 21:
        while dealer.value < 17:
            hit(mydeck, dealer)
        if dealer.value > 21:
            dealer_busts(player, player_chips, dealer)
        elif dealer.value > player.value:
            dealer_wins(player, player_chips, dealer)
        elif dealer.value < player.value:
            player_wins(player, player_chips, dealer)
        else:
            push(player, player_chips, dealer)
    
    print("Your total chips are:", player_chips.total)
    
    prompt = input("Do you want to play again? Y or N: ")
    if prompt.lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break
