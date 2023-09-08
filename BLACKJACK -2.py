#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CARD 
#RANK, SUIT, VALUE 


#DECK CLASS 


#PLAYER 
import random 
from random import shuffle 
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three" : 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack" : 10, "Queen" : 10, "King": 10, "Ace": 11}


# In[2]:


#Define the card class 

class Card: 
    def __init__ (self,suit,rank): 
        self.suit = suit 
        self.rank = rank 
        self.value = values[rank]
        
        
    def __str__ (self) : 
        return f"{self.rank} of {self.suit}"


# In[3]:


class Deck: 
    def __init__(self): 
        self.card_deck = []
        
        
        #Initialize the deck 
        for suit in suits :
            for rank in ranks : 
                drawn_card = Card(suit,rank)
                self.card_deck.append(drawn_card)
                
    def shuffle_deck (self) : 
        shuffle(self.card_deck)
    
    def deal_one (self) : 
        return self.card_deck.pop()


# In[4]:


class Account : 
    def __init__ (self, name, account= 0) : 
        self.name = name
        self.account = account
        
    def table_bet (self, bet) : 
        if bet <= self.account : 
            self.bet = bet 
            self.account-= bet 
            #return True 
            
        #else : 
            #return False 
    def add_cash (self, cash): 
        self.account+= cash 
        
    def __str__(self) : 
        return f"Player: {self.name}\nBalance: £{self.account}"
            


# In[5]:


class Hand: 
    #Passing the cards user has in their hand returning the cards and sum  
    def __init__ (self,hand):
        self.hand = hand
        self.total = 0 

        for i in range (len(self.hand)) : 
            self.total += self.hand[i].value
        
        #If the sum of the hand is greater than 21 check if an Ace exists 
        if self.total > 21 :
            self.total = 0 
            for i in range(len(self.hand)) : 
                
                #If an Ace exists, change the value to a 1
                if self.hand[i].value == 11  :
                    self.hand[i].value = 1     
                else : 
                    continue         
            for i in range (len(self.hand)) : 
                self.total += self.hand[i].value 
            
    def __str__ (self): 
        hand_list = ""
        for i in range (len(self.hand)) : 
            hand_list += str(self.hand[i]) + "\n"
        return f"{hand_list}"   


# In[6]:


def winner (Player,H,P,bet) : 
    #Draw 
    if H == P :
        Player.add_cash(bet)
        print("Tie!!")
        print("\nYou broke even\n")
    
    #Player Wins 
    elif H < P or H > 21: 
        Player.add_cash(bet+bet/2)
        print(f"\nYou Win £{(bet/2)}\n")
        
    #House wins 
    else  : 
        print("House wins!")
        print(f"\nYou lost £{bet}\n")
                
    return Player 


# In[8]:


#Initialise Player  

player_name = input("Please input your name: ")

depositing = True  
while depositing : 
    #Try Deposit 
    try : 
        balance = int (input("Please input your deposit amount: "))
        depositing = False 
    except : 
        print("ERROR: Please input an integer")

#Initialize Player Account
Player = Account(player_name,balance)

game_on = True 
while game_on :
    
    #If the player has less than £5, they are unable to bet 
    if Player.account < 5 : 
        print("You don't have the minimum amount to play the game")
        game_on = False
        
    #IF they have £5 or more, start the game 
    else : 
        
        #Initialize totals
        total_player = 0 
        total_house = 0 
        
        #initialize Deck of cards
        deck = Deck()
               
        #Shuffle Card deck 
        deck.shuffle_deck()
        print("\n")
        print(Player,flush ="True")

        #Both Players start with empty hand of cards 
        Player_cards = []
        House_cards = []

        #Ask Player for how much he would like to bet 
        betting = True 
        while betting:  
            #Ask user for input bet 
            bet = (input("\nInput the amount you would like to bet: "))
            
            #Check if bet is a number 
            if bet.isdigit() == True  : 
                bet = int(bet)
                
                #If the player can afford to bet that amount table the bet 
                if bet <= Player.account  :
                    Player.table_bet(bet)
                    print("\nBET ACCEPTED!")
                    
                    print(Player)
                    
                    #Deal 2 cards to both players 
                    for cards in range (2) : 
                        Player_cards.append(deck.deal_one())
                        House_cards.append(deck.deal_one())

                    #Print the players cards 
                    print (f"\n{Player.name} has the following cards: \n")
                    player_hand = Hand(Player_cards)
                    print (player_hand)

                    #Print the total of shown cards
                    print (f"Total: {player_hand.total}")


                    #Print the house cards - Hide 1  
                    print (f"\nHouse has the following cards: \n")
                    print ("--HIDDEN--")
                    print (f"{House_cards[1]}")

                    #Print the total of shown cards
                    print(f"\nTotal: {House_cards[1].value}")
                    betting = False 
                    
                #If player cant afford to bet 
                else : 
                    print("\n")
                    print("ERROR: You dont have enough money to make this bet\n")
                    print("  ACCOUNT")
                    print(Player)
                    continue 
                    
            #If the players input is not a number 
            elif bet.isdigit() != True  : 
                print("Please input an integer")
                continue 
                                      
        #Starts Playing        
        playing = True 
        while playing : 

            #Ask Player if they want to hit or Stay 
            Hit_Stay = input("\nPress Y to Hit and N to Stay: ")
            
            #If they choose to hit display their cards 
            if Hit_Stay.upper() == "Y" :
                Player_cards.append(deck.deal_one())
                player_hand = Hand(Player_cards)
                print (f"\n{Player.name} has the following cards: \n")
                print(player_hand)
                print(f"Total: {player_hand.total}")

                #If player is still in the game, continue  
                if player_hand.total <= 21 :
                    continue 

                #If players new hit > 21   
                else  :
                    print(f"\nYou lost £{bet}\n")
                    print("  ACCOUNT")
                    #Player.account = Player.account
                    print(Player)
                    playing = False 

            #Display computer cards      
            if Hit_Stay.upper() == "N" :
                print ("\n--House Cards Reval--")
                house_hand = Hand(House_cards)
                print(house_hand)
                
                #Print the total of cards
                print(f"Total: {house_hand.total}\n")
                
                #Check if House has won on reveal 
                if house_hand.total <= 21 : 
                    
                    #If house isnt bust on reveal, compare player and house
                    #If house is greater than player or house is >= 17 compare 
                    if house_hand.total >= 17 : 
                        Player = winner(Player,house_hand.total,player_hand.total,bet)   
                        print("  ACCOUNT")
                        print(Player)
                        playing = False
   
                    #Keep adding 
                    else :
                        adding = True 
                        while adding : 
                            #Print new cards and display total  
                            print("\n!!!House adds new card!!!\n")
                            House_cards.append(deck.deal_one())
                            house_hand = Hand(House_cards)
                            print(house_hand)
                            print(f"Total: {house_hand.total}\n")

                            #If new house hands >= 17 compare 
                            if house_hand.total >= 17 :
                                Player = winner(Player,house_hand.total,player_hand.total,bet)
                                print("  ACCOUNT")
                                print(Player)   
                                playing = False 
                                adding = False 

                            else: 
                                adding = True 
                                
                #House is bust and call compare function      
                else : 
                    Player = winner(Player,house_hand.total,player_hand.total,bet)
                    
        #Playing is done                    
        #Ask to play again 
        print("\nWould you like to play again?")
        play_again = input("Press Y for Yes and N for No: ")
        asking = True 
        while asking : 
            if play_again.upper() == "Y" : 
                #They want to play again 
                #Pass account details into the next game 
                Player = Account(Player.name,Player.account)
                House = Account("House")
                
                #If player account is <5 they cannot continue to a new game
                if Player.account < 5 : 
                    game_on = False 
                else : 
                    game_on = True 
                asking = False

            elif play_again.upper() == "N" : 
                #They do not want to play again
                print("\nThank you for playing BlackJack!\n")
                asking = False
                game_on = False 
            else : 
                
                print("Invalid input will ask again\n")
print("Restart the game to play")


# In[ ]:




