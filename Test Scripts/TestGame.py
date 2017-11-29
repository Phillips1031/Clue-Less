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
from location import Hallway, Room, StartLocation
from Clues import ClueDeck

def connect_locations(location1, location2):   
    location1.add_connecting_locations(location2)
    location2.add_connecting_locations(location1)

if __name__ == '__main__':
    
    #Create all the rooms on the board
    Study = Room(RoomEnum.Study)
    Hall =  Room(RoomEnum.Hall)
    Lounge = Room(RoomEnum.Lounge)
    Library = Room(RoomEnum.Library)
    BillardRoom = Room(RoomEnum.BilliardRoom)
    DiningRoom = Room(RoomEnum.DiningRoom)
    Conservatory = Room(RoomEnum.Conservatory)
    Ballroom = Room(RoomEnum.Ballroom)
    Kitchen = Room(RoomEnum.Kitchen)
    
    #Create the starting locations for the characters
    ScarlettStart = StartLocation('ScarletStart')
    MustardStart = StartLocation('MustardStart')
    PlumStart = StartLocation('PlumStart')
    GreenStart = StartLocation('GreenStart')
    PeacockStart = StartLocation('PeacockStart')
    WhiteStart = StartLocation('WhiteStart')
        
    #Create all the hallways on the board    
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
    
    #Connect up all the locations on the board together
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
       
    '''Note that the starting locations are only connected to 1 location
    Add that location does not connect back to the starting location
    Meaning, you can leave the starting area, but not come back in '''  
    
    WhiteStart.add_connecting_locations(hallway12)
    GreenStart.add_connecting_locations(hallway11)
    PeacockStart.add_connecting_locations(hallway8)
    PlumStart.add_connecting_locations(hallway3)
    ScarlettStart.add_connecting_locations(hallway2)
    MustardStart.add_connecting_locations(hallway5)
    
    newGame = Game.Game()
    player1 = Player.Player('player1')
    player2 = Player.Player('player2')
    player3 = Player.Player('player3')
    player4 = Player.Player('player4')
    
    mustard = CharacterN.Character(CharacterEnum.ColonelMustard, MustardStart)
    plum = CharacterN.Character(CharacterEnum.ProfessorPlum, PlumStart)
    scarlet = CharacterN.Character(CharacterEnum.MissScarlet, ScarlettStart)
    green =  CharacterN.Character(CharacterEnum.MrGreen, GreenStart)
    white = CharacterN.Character(CharacterEnum.MrsWhite, WhiteStart)
    Peacock = CharacterN.Character(CharacterEnum.MrsPeacock, PeacockStart)
 
    possibleCharacters = [mustard, plum, scarlet, green, white, Peacock]
    
    startGame = False
   
    while not startGame: 
        print('AddPlayer or StartGame?')
        userInput = input()
    
        if userInput in ['AddPlayer', 'a']:
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
                
        elif userInput in ['StartGame', 's']:
            startGame = newGame.start_game()
        else:
            print('Input not valid')
        
             
    #Game has started
    newGame.generate_turn_order()
    
    #Pick characters
    turnOrder = newGame.return_turn_order()
    print('Turn Order is {}'.format(turnOrder))
    
    for playerTurn in list(turnOrder):
        selection = False
        while not selection:
            print('{} pick your character:'.format(playerTurn))
            print('Possible character options {}'.format(possibleCharacters))
            userInput = input()
            
            if userInput in ['ColonelMustard', 'm']:
                character = mustard
            elif userInput in ['MissScarlet', 's']:
                character = scarlet
            elif userInput in ['ProfessorPlum', 'p']:
                character = plum
            elif userInput in ['MrGreen', 'g']:
                character = green
            elif userInput in ['MrsWhite', 'w']:
                character = white
            elif userInput in ['MrsPeacock', 'pea']:
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
    
    print('Selecting Final Evidence')
    
    deck = ClueDeck.ClueDeck()
    finalEvidence = deck.dealFinalEvidence()
    
    turnOrder = newGame.return_turn_order()
    
    while deck.hasCards():
        dealtClue = deck.dealClue()
        player = newGame.next_turn()
        player.add_clue(dealtClue)
    
    for player in list(turnOrder):
        print('{}\'s hand:\n'.format(player))
        player.show_hand()
        print('\n')
    
    print('{}, {}, {}'.format(finalEvidence.weapon, finalEvidence.character, finalEvidence.room))
    
    gameOver = False
    
    while not gameOver:
        currentPlayer = newGame.next_turn()
        if not currentPlayer.hasLostGame:
            print('{}\'s turn:\n'.format(currentPlayer))
            endOfTurn = False
            while not endOfTurn:
                if currentPlayer.oneMovePerTurn == True:
                    print('Move')
                if currentPlayer.suggestionPossible == True:
                    print('Suggestion')    
                print('EndTurn \n Accusation?')
                userInput = input()
                if userInput in ['Move', 'm']:
                    currentPlayer.character.available_moves()
                    selection = input("Enter a movement: ")
                    currentPlayer.move_character(selection)
                elif userInput in ['EndTurn', 'e']:
                    currentPlayer.end_turn()
                    endOfTurn = True
                elif userInput in ['Suggestion', 's']:
                    currentPlayer.make_suggestion()
                elif userInput in ['Accusation', 'a']:
                    print('Enter the details of the crime\n')
                    print('What was the location?')
                    locationGuess = input()
                    print('\nWho committed the crime?')
                    characterGuess = input()
                    print('\nWhat was the murder weapon')
                    weaponGuess = input()
                    
                    result = currentPlayer.check_accusation(finalEvidence, locationGuess, characterGuess, weaponGuess)
                    
                    if result == True:
                        print('Congraulations {} you have won the game!'.format(currentPlayer))
                        print('The right answer was {}, {}, {}'.format( locationGuess, characterGuess, characterGuess))
                        gameOver = True
                    else:
                        print('Oh no! Wrong Accusation!')
                        print('No more turns for you!')
                        currentPlayer.hasLostGame = True
                        currentPlayer.oneMovePerTurn = False
                        if(isinstance(currentPlayer.character.location, Hallway)):
                            print('You\'re also blocking a hallway. Let\'s get you out of the way.')
                            #popping location and adding it back. This is the only way I know how to 
                            #get a random location from the set 
                            location = currentPlayer.character.location.connectingLocations.pop()
                            currentPlayer.character.location.add_connecting_locations(location)
                            #Reset the players oneMovePerTurn to true to ensure they move
                            currentPlayer.oneMovePerTurn = True
                            currentPlayer.move_character(location.__str__())
                            endOfTurn = True
                else:
                    print("Invalid Selection\n")
        elif not newGame.areAnyPlayersLeft():
            gameOver = True
    print('The Game is over!')
        