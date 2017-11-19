'''
Created on Oct 2, 2017

@author: Zack
'''
from board import location

from location import Hallway

from location import Room

from RoomEnum import RoomEnum

from Character import CharacterN


def connect_locations(location1, location2):   
    location1.add_connecting_locations(location2)
    location2.add_connecting_locations(location1)
    
if __name__ == '__main__':
    #Attempt to initialize board files
   
    #inialize 2 rooms and 2 hallways
    Study = Room(RoomEnum.Study)
    Hall =  Room(RoomEnum.Hall)
    Lounge = Room(RoomEnum.Lounge)
    Library = Room(RoomEnum.Library)
    BillardRoom = Room(RoomEnum.BilliardRoom)
    DiningRoom = Room(RoomEnum.DiningRoom)
    Conservatory = Room(RoomEnum.Conservatory)
    Ballroom = Room(RoomEnum.Ballroom)
    Kitchen = Room(RoomEnum.Kitchen)
        
    hallway1 = Hallway('hallway 1')
    hallway2 = Hallway('hallway 2')
    hallway3 = Hallway('hallway 3')
    hallway4 = Hallway('hallway 4')
    hallway5 = Hallway('hallway 5')
    hallway6 = Hallway('hallway 6')
    hallway7 = Hallway('hallway 7')
    hallway8 = Hallway('hallway 8')
    hallway9 = Hallway('hallway 9')
    hallway10 = Hallway('hallway 10')
    hallway11 = Hallway('hallway 11')
    hallway12 = Hallway('hallway 12')
    
    connect_locations(Study, hallway1)
    connect_locations(Study, hallway3)
    connect_locations(Study, Kitchen)
    
    connect_locations(Hall, hallway1)
    connect_locations(Hall, hallway2)
    connect_locations(Hall, hallway4)
    
    connect_locations(Lounge, hallway2)
    connect_locations(Lounge, hallway5)
    connect_locations(Lounge, Conservatory)
    
    connect_locations(Library, hallway3)
    connect_locations(Library, hallway6)
    connect_locations(Library, hallway8)
    
    connect_locations(BillardRoom, hallway4)
    connect_locations(BillardRoom, hallway6)
    connect_locations(BillardRoom, hallway7)
    connect_locations(BillardRoom, hallway9)
    
    connect_locations(DiningRoom, hallway5)
    connect_locations(DiningRoom, hallway7)
    connect_locations(DiningRoom, hallway10)
    
    connect_locations(Conservatory, hallway8)
    connect_locations(Conservatory, hallway11)
    
    connect_locations(Ballroom, hallway9)
    connect_locations(Ballroom, hallway11)
    connect_locations(Ballroom, hallway12)
    
    connect_locations(Kitchen, hallway10)
    connect_locations(Kitchen, hallway12)
    
    mustard = CharacterN.Character("mustard", Study)
    plum = CharacterN.Character("plum", hallway1)
    hallway1.occupied = True
       
   

    while True:
        mustard.possible_moves()
        plum.possible_moves()
    

   

    

