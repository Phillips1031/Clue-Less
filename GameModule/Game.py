'''
Created on Nov 21, 2017

@author: Zack
'''
from collections import deque
from random import choice

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        print('Adding player {}'.format(player))
        
    def start_game(self):
        result = False
        #Start the game if more than 2 players
        if len(self.players) > 1 and len(self.players) < 7:
            result = True
            print("Starting the game!\n")
        else:
            print("Not enough players!\n")
        return result
    
    def generate_turn_order(self):
       
        self.turnOrder = deque()
        #While our set still has player, choose one at random and add them to turn list
        while self.players:
            randomplayer = choice(self.players)
            self.turnOrder.append(randomplayer)
            self.players.remove(randomplayer)
        print(self.turnOrder)
        
    def return_turn_order(self):
        return self.turnOrder
        
        
    def next_turn(self):
        nextplayer = self.turnOrder.pop()
        self.turnOrder.appendleft(nextplayer)
        return nextplayer
    
    #Returns True if any players are still playing, meaning they have
    #not lost. Returns false if all players have lost
    def areAnyPlayersLeft(self):
        result = False
        for player in list(self.turnOrder):
            if player.hasLostGame == False:
                result = True
                break
        return result    
        