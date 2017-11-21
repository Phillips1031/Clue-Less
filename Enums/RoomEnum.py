'''
Created on Nov 18, 2017

@author: Zack
'''
from enum import Enum

class RoomEnum ( Enum ):
    '''
    Enum class of weapons
    '''
    Study = 0
    Hall = 1
    Lounge = 2
    Library = 3
    BilliardRoom = 4
    DiningRoom = 5
    Conservatory = 6
    Ballroom = 7
    Kitchen = 8
    
class CharacterEnum ( Enum ):
    '''
    Enum class of people
    '''
    ColonelMustard = 0
    MissScarlet = 1
    ProfessorPlum = 2
    MrGreen = 3
    MrsWhite = 4
    MrsPeacock = 5