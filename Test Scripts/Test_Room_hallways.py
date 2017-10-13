'''
Created on Oct 2, 2017

@author: Zack
'''
from board import hallways

from board import room

if __name__ == '__main__':
    #Attempt to initialize board files
   
    #inialize 2 rooms and 2 hallways
    study = room.Room('study')
    kitchen = room.Room('kitchen')
    
    hallway1 = hallways.Hallway('hallway 1')
    hallway2 = hallways.Hallway('hallway 2')
    
    #assign both hallways to the study 
    #and assign only hallway 2 to the kitchen
    study.add_connecting_hallway(hallway1)
    study.add_connecting_hallway(hallway2)
    kitchen.add_connecting_hallway(hallway2)
    
    #check the hallways initial state
    study.whatRoom()
    kitchen.whatRoom()
    
    #change the hallway 1 to occupied check both rooms
    hallway1.change_to_occupied()
    study.whatRoom()
    kitchen.whatRoom()
    
    #change hallway2 to occupied and hallway1 to not
    #again check the state of both
    hallway2.change_to_occupied()
    hallway1.change_to_not_occupied()
    study.whatRoom()
    kitchen.whatRoom()
    
    

