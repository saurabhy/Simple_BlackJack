import random
from Beans.Card import *
from Beans.Player import *
from CustomException.CardListEmptyException import CardListEmpty

#Function to shuffle the deck of cards
def shuffle_card(mylist):
    random.shuffle(mylist)

#Function to add Face Cards

def add_Face(suit):
    cardlist = [Card(num, suit) for num in range(2, 11)]
    cardlist.append(Card('King',suit))
    cardlist.append(Card('Queen',suit))
    cardlist.append(Card('Jack',suit))
    cardlist.append(Card('Ace',suit))
    #print(cardlist)
    return cardlist

#Function to create the deck of cards
def create_Deck():
    return add_Face('Heart')+add_Face('Spade')+add_Face('Clubs')+add_Face('Diamond')


#To increase the randomness we will have a sampling without replacement function
def get_card(cardlist):
    if(len(cardlist)==0):
        raise CardListEmpty()
    else:
        return cardlist.pop()

#To get the points from a card
def get_Points(card,player):
    if(card.type in ['King','Queen','Jack']):
        return 10
    elif(card.type=='Ace'):
        if(player.name=='Mr.Python'):
            if(player.total+11<=21):
                return 11
            else:
                return 1
        while(True):
            try:
                inp=(int)(input("Enter the value you want to consider for Ace from 1 or 11 : "))
                if(inp==1 or inp==11):
                    return inp
            except:
                print("I couldn't understand you response :(")
    else:
        return 0

#To get the bids of the player
def get_bid(player):
    try:
        inp=(int)(input("Enter your bid .It should be less than or equal to the money you have currently : "))
        if(inp<=player.points):
            return inp
        else:
            print("Your bid is greater than money you have make another bid")
            return get_bid(player)
    except:
        print("I couldn't understand your response :(")
        return get_bid(player)

#Get Wish
def get_wish(text):
    while (True):
        inp = input("Do you want to {} (YES/NO) : ".format(text))
        if (inp.upper() == 'YES'):
            return True
        elif (inp.upper() == 'NO'):
            return False
        else:
            print("I coudn't understand your response :(")

def check_bust(player):
    if(player.total>21):
        return True
    return False

#This function simulates the play
def play(player,computer,card_hidden,cards,bid):
    hit=get_wish('hit')
    while(hit):
        card_cur=get_card(cards)
        print('Your card is {}'.format(card_cur))
        player.total+=get_Points(card_cur,player)
        if(check_bust(player)):
            print('Sorry you have lost this round :(')
            player.points-=bid
            computer.points+=bid
            return
        elif(player.total==21):
            print('Congratulations you have won this round')
            player.points+=bid
            computer.points-=bid
            return
        print('Your current total value for this round is {}'.format(player.total))
        hit=get_wish('hit')

    print("Starting Mr.Python's turn ")
    print("Mr.Python's second card was {}".format(card_hidden))
    print("Mr.Python's current total is {}".format(computer.total))
    hit=True
    while(hit):
        print('Mr.Python wants to hit')
        card_cur=get_card(cards)
        print("Mr.Python's card is {}".format(card_cur))
        computer.total+=get_Points(card_cur,computer)
        if(check_bust(computer)):
            print('Mr.Python is lost for this round')
            player.points+=bid
            computer.points-=bid
            return
        elif(computer.total==21 or computer.total>player.total):
            print('Mr.Python has won this round ')
            player.points-=bid
            computer.points+=bid
            return
        print("Mr.Python's current total value for this round is {}".format(computer.total))
