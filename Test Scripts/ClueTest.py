'''
Created on Nov 16, 2017

@author: Erika
'''

from Clues import ClueDeck


if __name__ == '__main__':
    
    
    deck = ClueDeck.ClueDeck()
    print( deck.hasCards() )
    

    FE = deck.dealFinalEvidence()
    for card in FE:
        print( card )
    for i in range(0,18):
        print( deck.dealClue() )
    
   
    
    
    