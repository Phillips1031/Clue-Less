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
    
    def __str__(self):
        return self.face
    
    def __repr__(self):
        return self.face    
        
    def add_character(self, character):
        self.character = character
        
    def has_character_already_moved(self):
        return not self.oneMovePerTurn   
        
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