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
    
    def __str__(self):
        return self.face    
        
    def add_character(self, character):
        self.character = character
        
    def move_character(self, requestedLocation):
        
        return self.character.move_location(requestedLocation)