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
        self.occupants = set()
        
    def add_connecting_locations(self, connectingLocation):
        self.connectingLocations.add(connectingLocation)
        
    def add_occupant(self, character):
        pass
    
    def remove_occupant(self, character):
        self.occupants.remove(character)
                
    def __str__(self):
        return self.name
    
    def show_connecting_locations(self):
        # Simple function for test
        for k in self.connectingLocations:
            print( "{} is connected to {}".format(self.name, k))
            
    def return_connecting_locations(self):
        return self.connectingLocations

class Hallway(Location):
    '''
    Connections between rooms.
    '''


    def __init__(self, hallwayName):
        '''
        Constructor
        '''
        super().__init__(hallwayName)

    def add_occupant(self, character):
        #Return true if the set is empty, false if occupied
        if self.occupants:
            result = False
        else:
            self.occupants.add(character)
            result = True
        return result
         
        

        
class Room(Location):
    '''
   Locations that characters can occupy and make suggestions in.
    '''
    
    def __init__(self, roomname):
        '''
        Constructor
        '''
        super().__init__(roomname)
    
    def add_occupant(self, character):
        self.occupants.add(character)
        return True


    