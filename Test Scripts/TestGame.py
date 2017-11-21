'''
Created on Nov 21, 2017

@author: Zack
'''
from PlayerModule import Player
from GameModule import Game
from Character import CharacterN
from RoomEnum import RoomEnum, CharacterEnum

if __name__ == '__main__':
    newGame = Game.Game()
    player1 = Player.Player('player1')
    player2 = Player.Player('player2')
    player3 = Player.Player('player3')
    player4 = Player.Player('player4')
    
    mustard = CharacterN.Character(CharacterEnum.ColonelMustard, 'pretendMustard')
    plum = CharacterN.Character(CharacterEnum.ProfessorPlum, 'precious plum')
    
    
    newGame.add_player(player1)
    newGame.add_player(player2)
    newGame.add_player(player3)
    newGame.add_player(player4)
    newGame.add_player(player1)
 
   
    result = newGame.start_game()
    
    