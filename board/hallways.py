'''
Created on Oct 10, 2017

@author: Zack
'''

class Hallway(object):
    '''
    classdocs
    '''


    def __init__(self,name):
        '''
        Constructor
        '''
        self.hallwayName = name
        self.occupied = False
        self.connectingRooms = set()

    def add_connecting_rooms(self,newRoom):
        self.connectingRooms.add(newRoom)
        
    def is_hallway_occupied(self):
        return(self.occupied)
    
    def change_to_occupied(self):
        self.occupied = True
        
    def change_to_not_occupied(self):
        self.occupied = False
        
    def return_connecting_rooms(self):
        return(self.connectingRooms)
        

    