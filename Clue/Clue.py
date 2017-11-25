'''
Created on Nov 16, 2017

@author: Erika
'''
from enum import Enum

class CardCategories ( Enum ):
    Weapon = 0
    Person = 1
    Room = 2

class Weapon ( Enum ):
    '''
    Enum class of weapons
    '''
    Rope = 0
    LeadPipe = 1
    Knife = 2
    Wrench = 3
    Candlestick = 4
    Revolver = 5

class Person ( Enum ):
    '''
    Enum class of people
    '''
    ColonelMustard = 0
    MissScarlet = 1
    ProfessorPlum = 2
    MrGreen = 3
    MrsWhite = 4
    MrsPeacock = 5

class Room ( Enum ):
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

class Clue(object):
    '''
    A simple clue class
    '''

    def __init__(self, cat, specific):
        '''
        Constructor:  Sets the value based on an integer for category and a specific item
        '''
        
        ''' Sets the position of the card in the deck '''
        self.cardPosition = specific
        if cat == 1:
            self.cardPosition = specific + 6
        if cat == 2:
            self.cardPosition = specific + 12
        
        ''' Sets the category and specific value of the card'''
        if cat == CardCategories.Weapon.value:
            self.cardCategory = CardCategories.Weapon
            if specific == Weapon.Rope.value:
                self.specific = Weapon.Rope
            if specific == Weapon.LeadPipe.value:
                self.specific = Weapon.LeadPipe
            if specific == Weapon.Knife.value:
                self.specific = Weapon.Knife
            if specific == Weapon.Wrench.value:
                self.specific = Weapon.Wrench
            if specific == Weapon.Candlestick.value:
                self.specific = Weapon.Candlestick
            if specific == Weapon.Revolver.value:
                self.specific = Weapon.Revolver
        if cat == CardCategories.Person.value:
            self.cardCategory = CardCategories.Person
            if specific == Person.ColonelMustard.value:
                self.specific = Person.ColonelMustard
            if specific == Person.MissScarlet.value:
                self.specific = Person.MissScarlet
            if specific == Person.ProfessorPlum.value:
                self.specific = Person.ProfessorPlum
            if specific == Person.MrGreen.value:
                self.specific = Person.MrGreen
            if specific == Person.MrsWhite.value:
                self.specific = Person.MrsWhite
            if specific == Person.MrsPeacock.value:
                self.specific = Person.MrsPeacock
        if cat == CardCategories.Room.value:
            self.cardCategory = CardCategories.Room
            if specific == Room.Study.value:
                self.specific = Room.Study
            if specific == Room.Hall.value:
                self.specific = Room.Hall
            if specific == Room.Lounge.value:
                self.specific = Room.Lounge
            if specific == Room.Library.value:
                self.specific = Room.Library
            if specific == Room.BilliardRoom.value:
                self.specific = Room.BilliardRoom
            if specific == Room.DiningRoom.value:
                self.specific = Room.DiningRoom
            if specific == Room.Conservatory.value:
                self.specific = Room.Conservatory
            if specific == Room.Ballroom.value:
                self.specific = Room.Ballroom
            if specific == Room.Kitchen.value:
                self.specific = Room.Kitchen

    def __str__(self):
        return "I'm a " + self.specific.name + " " + self.cardCategory.name
    
