'''
Created on Oct 10, 2017

@author: Zack
'''

class Hallway(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.occupied = OccupiedStatus.NOT_OCCUPIED
        self.connectingRooms = set()
        
    def add_connecting_rooms(self,newRoom):
        self.connectingRooms.add(newRoom)
        
    def is_hallway_occupied(self):
        return(self.occupied is OccupiedStatus.OCCUPIED)
    
    def change_to_occupied(self):
        self.occupied = OccupiedStatus.OCCUPIED
        
    def change_to_not_occupied(self):
        self.occupied = OccupiedStatus.NOT_OCCUPIED
        
    def return_connecting_rooms(self):
        return(self.connectingRooms)
        
from enum import Enum        
class OccupiedStatus(Enum):
    NOT_OCCUPIED = 1
    OCCUPIED = 2
    