'''
Created on Nov 16, 2017

@author: Erika
'''

from Clues import Clue
from random import randint

class ClueDeck(object):
    '''
    This deck contains all possible clues.
    It can deal out final evidence (assumes these are the first cards dealt)
    It can deal out one card one at a time and keep track of which cards have been dealt
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.cards = []
        self.inUse = []
        i = 0
        for j in range(0,6):
            self.cards.append( Clue.Clue( i, j ))
            self.inUse.append(False)
        i = 1
        for j in range(0,6):
            self.cards.append( Clue.Clue( i, j ))
            self.inUse.append(False)
        i = 2
        for j in range(0,9):
            self.cards.append( Clue.Clue( i, j ))
            self.inUse.append(False)
        
        
    def dealFinalEvidence(self):
        
        finalEvidence = []
        
        '''Get weapon evidence'''
        i = randint(0, 5)
        finalEvidence.append( self.cards[i] )
        self.inUse[i] = True
        '''Get person evidence'''
        i = randint(0, 5)
        finalEvidence.append( self.cards[i + 6])
        self.inUse[i+5] = True
        '''Get room evidence'''
        i = randint(0, 8)
        finalEvidence.append( self.cards[i + 12] )
        self.inUse[i+11] = True
        
        '''Return the set of final evidence'''
        return finalEvidence
        
    def dealClue(self):
        '''
        Deals a clue
        Updates that the clue has been dealt (self.inUse)
        Returns False if all cards have been dealt
        '''
        card = False
        if self.hasCards() == True:
            dealt = False
            while dealt == False:
                i = randint(0, 20)
                #print( i )
                if self.inUse[i] == False:
                    card = self.cards[i]
                    self.inUse[i] = True
                    dealt = True
        
        return card
        
    def hasCards(self):
        cardsLeft = False
        for card in self.inUse:
            if card == False:
                cardsLeft = True
        return cardsLeft
        
        
    def outputAll(self):
        for card in self.cards:
            print( card.cardPosition )
            print( card )
            print( self.inUse[ card.cardPosition ] )
        
        
        
        
        