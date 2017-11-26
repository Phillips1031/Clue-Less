'''
Created on Nov 19, 2017

@author: Zack
'''

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.character = []
        self.face = name
        self.oneMovePerTurn = True
        self.hasLostGame = False
        self.cardsHeld = []
    
    def __str__(self):
        return self.face
    
    def __repr__(self):
        return self.face    
        
    def add_character(self, character):
        self.character = character
        
    def has_character_already_moved(self):
        return not self.oneMovePerTurn   
    
    def add_clue(self,clue):
        self.cardsHeld.append(clue)
        
    def show_hand(self):
        for cards in self.cardsHeld:
            print(cards)
        
    def move_character(self, requestedLocation):
        #Check to see if the player has already moved this Turn
        if self.oneMovePerTurn == True:
            #if the requested location is acceptable complete the move
            if self.character.move_location(requestedLocation):
                #if the move was successful take away the move
                self.oneMovePerTurn = False
        else:
            print('Character has already moved this turn\n')        
    def end_turn(self):
        #Set back the ability to move
        self.oneMovePerTurn = True
        
    def check_accusation(self, finalEvidence, locationGuess, characterGuess, weaponGuess):
        result = False
        if finalEvidence.weapon.specific.name == weaponGuess:
            print('Weapon guess Correct')
            if finalEvidence.character.specific.name == characterGuess:
                print('Character guess Correct')
                if finalEvidence.room.specific.name == locationGuess:
                    result = True
                    print('Location Guess Correct')
                    
        return result