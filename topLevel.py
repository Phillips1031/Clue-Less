'''
Created on Oct 2, 2017

@author: Zack
'''
from board import hallways

ab = hallways.Hallway()

a = hallways.OccupiedStatus.NOT_OCCUPIED

a is ab.is_hallway_occupied()

