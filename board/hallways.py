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
        return(repr(self.occupied))
        
        
from enum import Enum        
class OccupiedStatus(Enum):
    NOT_OCCUPIED = 0
    OCCUPIED = 1
    