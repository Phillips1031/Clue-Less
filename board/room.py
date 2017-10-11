'''
Created on Oct 3, 2017

@author: Zack
'''

class Room(object):
    '''
    classdocs
    Attempt at building a room
    '''


    def __init__(self, roomType):
        '''
        Constructor
        '''
        self.roomType = roomType
        self.connectingRooms = set()
        self.secretTunnel = set()      

    def whatRoom(self):
        # Simple function for test
        for k in self.connectingRooms:
            print(k.name)

    def addConnectingRooms(self, newRoom):
        #Try to change rooms
        self.connectingRooms.add(newRoom)
        
def initalizeSTUDY():
    study = Room(RoomType.STUDY)
    study.addConnectingRooms(RoomType.HALL)
    study.addConnectingRooms(RoomType.LIBRARY)
    return(study)

from enum import Enum        
class RoomType(Enum):
    STUDY = 1
    HALL = 2
    LOUNGE = 3
    LIBRARY = 4 
    BILLIARDS = 5
    DINING = 6
    CONSERVATORY = 7
    BALLROOM = 8 
    KITCHEN = 9
    
    