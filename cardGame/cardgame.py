""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")

rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def clearDeck():

    for i in cardLoc:                                                                                                   # Iterate through each value of cardLoc
        cardLoc[i] = 0                                                                                                  # Set it to 0

def assignCard(owner):
    keepGoing = True
    while(keepGoing == True):
        location = randint(0, NUMCARDS)                                                                                 # Set a new random deck location each iterations
        if(cardLoc[location] == 0):                                                                                     # If the card at location 'location' is not assigned
            cardLoc[location] = owner                                                                                   # Set the card at that location to the value of the owner param
            keepGoing = False                                                                                           # Tell the loop to stop iterating
        else:
            keepGoing = True                                                                                            # If card is assigned, loop again until a card is chosen which isn't

def showDeck():
    print("Location of all cards\n"                                                                                     # Format card tabs
          "# 	 card 	 	 location")

    count = 0                                                                                                           # Set count to 0

    for i in range(0, len(suitName)):                                                                                   # Loop through the suit names
        for j in range(0, len(rankName)):                                                                               # For each suit loop through a rank
            print("{}   {} of {}   {}".format((count), rankName[j], suitName[i], playerName[cardLoc[(count)]]))         # Display the iteration, rank of rank iteration j, suit of suit iteration i, and the playername which corresponds with the value at cardLoc
            count += 1                                                                                                  # Iterate count

def showHand(owner):
    print("Displaying {} hand".format(playerName[owner]))                                                               # Format label

    for k in range(0, len(cardLoc)):                                                                                    # Loop through cardLoc
        if(cardLoc[k] == owner):                                                                                        # If value at cardLoc corresponds with owner param
            print(" {} of {} ".format(rankName[(k % 13)], suitName[k // 13]))                                           # Format rank and suit of k

def main():
    clearDeck()

    for i in range(5):
        assignCard(PLAYER)
        assignCard(COMP)

    showDeck()
    showHand(PLAYER)
    showHand(COMP)

main()