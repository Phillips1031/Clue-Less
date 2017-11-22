'''
Created on Nov 21, 2017

@author: Zack
'''
from PlayerModule import Player
from GameModule import Game
from Character import CharacterN
from RoomEnum import RoomEnum, CharacterEnum
from unittest import case
from _overlapped import NULL

if __name__ == '__main__':
    newGame = Game.Game()
    player1 = Player.Player('player1')
    player2 = Player.Player('player2')
    player3 = Player.Player('player3')
    player4 = Player.Player('player4')
    
    mustard = CharacterN.Character(CharacterEnum.ColonelMustard, 'pretendMustard')
    plum = CharacterN.Character(CharacterEnum.ProfessorPlum, 'precious plum')
    scarlet = CharacterN.Character(CharacterEnum.MissScarlet, 'Scarlet')
    green =  CharacterN.Character(CharacterEnum.MrGreen, 'Green')
    white = CharacterN.Character(CharacterEnum.MrsWhite, 'White')
    Peacock = CharacterN.Character(CharacterEnum.MrsPeacock, 'Peacock')
 
    possibleCharacters = [mustard, plum, scarlet, green, white, Peacock]
    
    startGame = False
   
    while not startGame: 
        print('AddPlayer or StartGame?')
        userInput = input()
    
        if userInput in ['AddPlayer']:
            print('Which player? 1,2,3,4')
            playerName = input()
            if playerName == '1':
                newGame.add_player(player1)
            elif playerName == '2':
                newGame.add_player(player2)
            elif playerName == '3':
                newGame.add_player(player3)
            elif playerName == '4':
                newGame.add_player(player4)
            else:
                print('Invalid Entry\n')
                
        elif userInput in ['StartGame']:
            startGame = newGame.start_game()
        else:
            print('Input not valid')
        
             
    #Game has started
    newGame.generate_turn_order()
    
    #Pick characters
    turnOrder = newGame.return_turn_order()
    print('Turn Order is {}'.format(turnOrder))
    
    while turnOrder:
        playerTurn = turnOrder.pop()
        selection = False
        while not selection:
            print('{} pick your character:'.format(playerTurn))
            print('Possible character options {}'.format(possibleCharacters))
            userInput = input()
            
            if userInput in ['ColonelMustard']:
                character = mustard
            elif userInput in ['MissScarlet']:
                character = scarlet
            elif userInput in ['ProfessorPlum']:
                character = plum
            elif userInput in ['MrGreen']:
                character = green
            elif userInput in ['MrsWhite']:
                character = white
            elif userInput in ['MrsPeacock']:
                character = Peacock
            else:
                print('Invalid Character Selected')
                character = NULL
                
            if character in possibleCharacters:
                playerTurn.add_character(character)   
                possibleCharacters.remove(character)
                selection = True
            else:
                print('Character already selected')
     
    print('Characters Selected Starting Game')   
    
    turnOrder = newGame.return_turn_order()
    print(turnOrder)
        