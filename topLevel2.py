'''
Created on Oct 2, 2017

@author: Zack
'''
from board import hallways

from board import room

def initialize_board():
    study = room.Room()
    hall = room.Room()
    lounge = room.Room()
    library = room.Room()
    billardRoom = room.Room()
    diningRoom = room.Room()
    conservatory = room.Room()
    ballroom = room.Room()
    kitchen = room.Room()

if __name__ == '__main__':
    #Attempt to initialize board files
    
    study = room.Room('study')
    hall = room.Room('hall')
    lounge = room.Room('lounge')
    library = room.Room('library')
    billardRoom = room.Room('billardRoom')
    diningRoom = room.Room('diningRoom')
    conservatory = room.Room('conservatory')
    ballroom = room.Room('ballroom')
    kitchen = room.Room('kitchen')
    
    hallway1 = hallways.Hallway('hallway 1')
    hallway2 = hallways.Hallway('hallway 2')
    
    study.add_connecting_hallway(hallway1)
    study.add_connecting_hallway(hallway2)
    
    kitchen.add_connecting_hallway(hallway2)
    

    

