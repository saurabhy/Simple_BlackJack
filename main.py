from Simple_BlackJack.Service.Helper import *
from Simple_BlackJack.Beans.Player import *
from Simple_BlackJack.CustomException.CardListEmptyException import *
print("WELCOME TO BLACK JACK - TRY YOUR LUCK (Some say Entropy of Computer generated random numbers isn't perfect)")
print("And ofcourse you will be playing against MR.PYTHON")

print('''
Rules for playing: 
1. All the face cards have value 10 and Ace can be treated as 1 or 11 \n
2. First 2 cards will be given to each player \n
3. Your 2 cards will be shown to you \n
4. Mr.Python's 1 card will be shown to you and one will be hidden \n
5. First chance will be yours - you can either hit (draw a card) or stay and continue till you \n
   want to stop or you reach 21 \n
6. Mr.python will then play he will always hit till he reaches value more than you or 21 \n
7. if at any stage any one of the player's total becomes more than 21 he loses \n
8. player reaching 21 wins immediately and other player looses the round \n
9. play continues till you have got chips left \n''')
points=0

while(True):
    try:
        chips=(int)(input("Enter the chips you want to play with (Integer please) : "))
        break
    except:
        print("I couldn't understand you response :(")

play_I=input("Enter your name : ")
play_C='Mr.Python'

player= Player(play_I,chips)
computer=Player(play_C,chips)

flag=False

flag=get_wish('continue playing ')

try:
    win=-1
    while(flag):
        bid=get_bid(player)
        cards= create_Deck()
        shuffle_card(cards)
        card1=get_card(cards)
        card2=get_card(cards)
        player.total=0
        computer.total=0
        print("Your first two cards are {} and {}".format(card1,card2))
        player.total=get_Points(card1,player)+get_Points(card2,player)
        card3=get_card(cards)
        card4=get_card(cards)
        print("{}'s first two cards are {} and ****".format(computer.name,card3))
        computer.total=get_Points(card3,computer)+get_Points(card4,computer)
        play(player,computer,card4,cards,bid)
        print("Your current money is {} and Mr.Python's money is {}".format(player.points, computer.points))
        if(player.points<=0):
            win=1
            break
        if(computer.points<=0):
            win=0
            break
        flag=get_wish('continue playing ')

    if(win==0):
        print("Congratulations you won the game :D")
    elif(win==1):
        print("Sorry you couldn't win this time")
    else:
        print("Game has stopped in between")

except CardListEmpty as e:
    print(e.__cause__)
    pass
finally:
    print("Game has ended hope you have enjoyed your time playing ")

