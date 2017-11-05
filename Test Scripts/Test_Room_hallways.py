'''
Created on Oct 2, 2017

@author: Zack
'''
from board import location

from location import Hallway

from location import Room

from Character import CharacterN


def connect_locations(location1, location2):   
    location1.add_connecting_locations(location2)
    location2.add_connecting_locations(location1)
    
if __name__ == '__main__':
    #Attempt to initialize board files
   
    #inialize 2 rooms and 2 hallways
    study = Room('study')
    kitchen = Room('kitchen')
    
    hallway1 = Hallway('hallway 1')
    hallway2 = Hallway('hallway 2')
    
    mustard = CharacterN.Character("mustard", study)
    
    #assign both hallways to the study 
    #and assign only hallway 2 to the kitchen
    connect_locations(study, hallway1)
    connect_locations(study, hallway2)
    connect_locations(kitchen, hallway2)

    while True:
        mustard.possible_moves()
    
    #check the hallways initial state
    study.show_connecting_locations()
    kitchen.show_connecting_locations()
    
    #change the hallway 1 to occupied check both rooms
    hallway1.change_to_occupied()
        
    #change hallway2 to occupied and hallway1 to not
    #again check the state of both
    hallway2.change_to_occupied()
    hallway1.change_to_not_occupied()
   

    

