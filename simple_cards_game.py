#Olivier Niyonshuti Mizero
#March 1, 2021
#simple card game

class Error(Exception): 
    '''creating an error class in case i want to print an error message'''
    def __init__(self,message):
        self.message = message
        
class Card:
    def __init__(self,csuit,cval):
        self._csuits = {'H': 'Hearts','D': 'Diamonds','S': 'Spades','C': 'Clubs'}
        self._csuit = self._csuits[csuit]
        self._cval = cval
        self._cvals = {1: 'Ace',11:'Jack',12:'Queen',13:'King'}
        self._specialVals = {'A': 1, 'J':11, 'Q':12, 'K':13}
        
       
        if type(cval) == int: #if user inputs cval as integer
              self._cval = cval
        elif cval in self._specialVals.keys():
            self._cval = self._specialVals[cval]
        else: #if user inputs cval as string
            self._cval = int(cval)
            
    # other functions
    def __str__(self): #print
        #return self._cval + 'of' + str(self._csuit)
        if self._cval in self._cvals.keys():
            return ('{} of {}'.format (self._cvals[self._cval], self._csuit))
        else:
            return ('{} of {}'.format (self._cval, self._csuit))
    def getCval(self):
        return self._cval
    def getCsuit(self):
        return self._csuit
    def setCval(self,val):
        raise Error('The value cannot be changed.')
    def setCsuit (self,suit):
        raise Error('The suit cannot be changed.')
        
    
    #overloading operators
    def __lt__(self,other):
        return self._cval < other._cval
    def __le__(self,other):
        return self._cval <= other._cval
    def __gt__(self,other):
        return self._cval > other._cval
    def __ge__(self,other):
        return self._cval >= other._cval
    def __eq__(self,other):
        return self._cval == other._cval
    def __ne__(self,other):
        return not(self._cval == other._cval)


import random
class Deck:
    def __init__(self):
        self.thedeck = []
        self.thedeck = self.populate()
    def draw(self):
        m = self.thedeck.pop()
        return m
    def populate(self):
        deck = []
        infile = open('deck.csv','r')
        infile.readline() # clear first line
        temp = infile.readlines()
        for line in temp:
            card = line.split(',')
            x = Card(card[1],card[0])
            #add to deck
            deck.append(x)
        #save number of cards or something
        return deck
    def add(self,c):
        #your code here
            self.thedeck.append(c)
    def dshuffle(self):
        return random.shuffle(self.thedeck)
    def peek(self):
         #your code here
        return self.thedeck[-1]
    def clearDeck(self):
        #your code here
        self.thedeck = []
    def isEmpty(self):
        #your code here
        return len(self.thedeck) == 0
    def size(self):
        #your code here
        return len(self.thedeck)
    def getDeck(self):
        #your code here
        return self.thedeck
    def replace(self,a):
        #your code here
        self.thedeck = a
    def __len__(self):
        #your code here
        return self.size()
    def __iter__( self ): 
        return _DeckIterator(self.thedeck )
    def __str__(self):
        # your code here
        return 'Deck has ' + str(len (self.thedeck)) + ' cards' 
    
class _DeckIterator : 
    def __init__( self, theList ): 
        self._bagItems = theList # an alias to the list 
        self._curItem = 0 # loop index variable 
    def __iter__( self ): 
        return self # return a reference to the object itself
    def __next__( self ):
        if self._curItem < len( self._bagItems ) : 
            item = self._bagItems[ self._curItem ] # reference to the indicated item 
            self._curItem += 1 
            return item
        else: raise StopIteration

def won(p1,p1_disc,p2,p2_disc): 
    #your code here
    #player is going to win when 
    #his main deck and the discard pile empty
    #return True or False
    if (p1.isEmpty() and p1_disc.isEmpty())or((p2.isEmpty() and p2_disc.isEmpty())):
        return True
    return  False

def print_winner(p1wins,p2wins):
    #your code here
    print ('Player 1 won ' + str(p1wins) + ' times')
    print ('Player 2 won ' + str(p2wins) + ' times')
    winner = None
    if p1wins == p2wins:
        print ("It's a tie!")
    elif p1wins > p2wins:
        winner = 'Player 1'
    else:
        winner = 'Player 2'
    print("The winner is ", winner)
    
#print_winner(243, 233)

def turn(p1,p1_disc,p2,p2_disc,p1wins,p2wins):
    #your code here
    all_cards = []
    if p1.isEmpty():
        p1.replace(p1_disc.thedeck)
        p1_disc.clearDeck()
        p1.dshuffle()#shuffle again
    if p2.isEmpty():
        p2.replace(p2_disc.thedeck)
        p2_disc.clearDeck()
        p2.dshuffle()#shuffle again
    
    p1_card = p1.draw()
    p2_card = p2.draw()
    if p1_card > p2_card:
        if (len(all_cards) > 0):
            deck_now = p1_disc.getDeck()
            deck_now = deck_now.extend(all_cards)
            p1_disc.replace(deck_now)#replaces disc pile 1 by cards in all_cards
        else:
            p1wins += 1
            p1_disc.add(p1_card)
            p1_disc.add(p2_card)
    elif p1_card < p2_card:
        if (len (all_cards)>0):
            deck_now = p2_disc.getDeck()
            deck_now = deck_now.extend(all_cards)
            p1_disc.replace(deck_now)#replaces disc pile 2 by cards in all_cards 
        else:
            p2wins += 1
            p2_disc.add(p2_card)
            p2_disc.add(p2_card)
    elif p1_card == p2_card:
        all_cards.append(p2_card)
        all_cards.append(p1_card)
        
    return p1,p1_disc,p2,p2_disc,p1wins,p2wins

def init():
    #initialize: each player gets 2 decks. Discard deck initially empty for each player
    p1 = Deck()
    p1.dshuffle()
    p1_disc = Deck()
    p1_disc.clearDeck()
    p2 = Deck()
    p2.dshuffle()
    p2_disc = Deck()
    p2_disc.clearDeck()
    return p1,p1_disc,p2,p2_disc
def resetDecks(p1,p1_disc,p2,p2_disc):
    if p1.isEmpty() and (not p1_disc.isEmpty()):
        p1.replace(p1_disc.getDeck())
        p1_disc.clearDeck()
        p1.dshuffle()
    if p2.isEmpty() and (not p2_disc.isEmpty()):
        p2.replace(p2_disc.getDeck())
        p2_disc.clearDeck()
        p2.dshuffle()
    return p1,p1_disc,p2,p2_disc

def war(): 
    p1,p1_disc,p2,p2_disc = init()
    p1wins = 0
    p2wins = 0
    stop = False
    while not stop:
        p1,p1_disc,p2,p2_disc,p1wins,p2wins = turn(p1,p1_disc,p2,p2_disc,p1wins,p2wins)
        if won(p1,p1_disc,p2,p2_disc):
            stop = True
    print_winner(p1wins,p2wins)

war()
