'''
Created on Oct 3, 2017

@author: Zack
'''

class Room(object):
    '''
    classdocs
    Attempt at building a room
    '''


    def __init__(self, roomname):
        '''
        Constructor
        '''
        self.roomname = roomname
        self.connectingRooms = set()
        self.secretTunnel = set()      

    def whatRoom(self):
        # Simple function for test
        for k in self.connectingRooms:
            print( "Is {} occupied?': {}".format(k.hallwayName, k.is_hallway_occupied()))

    def add_connecting_hallway(self, newHallway):
        #Try to change rooms
        self.connectingRooms.add(newHallway)
        


    
    