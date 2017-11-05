'''
Created on Oct 25, 2017

@author: Zack
'''

class Character(object):
    '''
    Possible suspects that move to varies locations on the game board.
    
    TODO think of something better for location
    '''


    def __init__(self, characterName, location):
        '''
        Constructor
        '''
        self.name = characterName
        self.location = location
        location.add_occupant(self)
        
    def current_location(self):
        print(self.location)
        
    def possible_moves(self):
        
        try:
            print("{} is currently in the {}".format(self.name, self.location))
            self.location.show_connecting_locations()
            connectingLocations = self.location.return_connecting_locations()
        except:
            print("I messed up")
        selection = input("Enter the location you would like to move to:")
        
        for location in connectingLocations:
            if selection == location.name:
                if location.add_occupant(self):
                    print("{} was able to enter the {}".format(self.name, location.name))
                else:
                    print("Could not enter {}".format(location.name))
                break
        else:
            print("Input location not found")
    
        print('End of possible_moves')
        
        
 