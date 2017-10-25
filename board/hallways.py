'''
Created on Oct 10, 2017

@author: Zack
'''

class Location(object):
    '''
    Areas of the game board that a character can occupy.
    
    TODO:  Start Locations?
    '''
    
    def __init__(self, name):
        self.name = name
        self.connectingLocations = set()
        
    def add_connecting_locations(self, connectingLocation):
        self.connectingLocations.add(connectingLocation)
        
    def __str__(self):
        return self.name
    
    def show_connecting_locations(self):
        # Simple function for test
        for k in self.connectingLocations:
            print( "{} is connected to {}".format(self.name, k))

class Hallway(Location):
    '''
    Connections between rooms.
    '''


    def __init__(self, hallwayName):
        '''
        Constructor
        '''
        super().__init__(hallwayName)
        self.occupied = False

    def is_hallway_occupied(self):
        return(self.occupied)
    
    def change_to_occupied(self):
        self.occupied = True
        
    def change_to_not_occupied(self):
        self.occupied = False

        
class Room(Location):
    '''
   Locations that characters can occupy and make suggestions in.
    '''
    
    def __init__(self, roomname):
        '''
        Constructor
        '''
        super().__init__(roomname)

        


    