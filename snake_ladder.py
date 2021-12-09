#
# snake and ladder game
import time
import random
import sys

SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 0
DICE_FACE = 6
snakes = {}

ladders = {}


def getBoardSize():
    global MAX_VAL
    MAX_VAL = int(input("Enter the size of the board: \n").strip())


def getPlayerName():
    noOfPayer = int(input("Enter number of players wants to join: \n").strip())
    players = []
    for i in range(0,noOfPayer):
        players.append(input("Enter player "+str(i+1)+" : \n").strip())

    return players


def getSnakeMoves():
    checkConfirmation = input("Do you want to enter snake moves(Y/N): \n").strip()
    global snakes
    if checkConfirmation.upper() == "Y":
        noOfMoves = int(input("Enter number of moves: \n").strip())
        print("Enter "+ str(noOfMoves) +" moves (Eg. 14 4 : any player at 14 will come down to 4)")
        for i in range(0,noOfMoves):
            inpData = input().strip()
            inpArr = inpData.split()
            snakes[int(inpArr[0])]=int(inpArr[1])
    else:
        snakes = {
            17: 5,
            34: 10,
            51: 19,
            62: 50,
            82: 32,
            88: 60,
            95: 73,
            98: 69,
            
        }

def getLadderMoves():
    checkConfirmation = input("Do you want to enter ladder moves(Y/N): \n").strip()
    global ladders
    if checkConfirmation.upper() == "Y":
        noOfMoves = int(input("Enter number of moves: \n").strip())
        print("Enter "+ str(noOfMoves) +" moves (Eg. 4 14 : any player at 4 will goes up to 14)")
        for i in range(0,noOfMoves):
            inpData = input().strip()
            inpArr = inpData.split()
            ladders[int(inpArr[0])]=int(inpArr[1])
    else:
        ladders = {
            4: 14,
            9: 31,
            13: 38,
            21: 60,
            28: 84,
            51: 67,
            72: 99,
            80: 92   
        }


def getDiceValue():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    return dice_value


def snakeLadder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value
    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        current_value = old_value
    if current_value in snakes:
        final_value = snakes.get(current_value)
        print(player_name +" rolled: " + str(dice_value) + " OOPS! SNAKE BITE, RETURN TO "+str(final_value)+" moved to  :"+ str(final_value))
    elif current_value in ladders:
        final_value = ladders.get(current_value)
        print(player_name +" rolled: " + str(dice_value) + " HURRY! CLIMBED THE LADDER from :"+ str(old_value) +" moved to " + str(final_value))
    else:
        print(player_name +" rolled: " + str(dice_value) + " moved to  :"+ str(current_value))
        final_value = current_value
    return final_value

def checkWin(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. Hope you enjoyed the time with your friend\n\n")
        sys.exit(1)


def startGame():
    getBoardSize()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    players = getPlayerName()
    playersValue = []
    for player in players:
        playersValue.append({player:0})
    getSnakeMoves()
    getLadderMoves()
    print("SETTING DICE AS CROOCKED\n")
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    print("Starting Snakes and Ladder\n")
    while True:
        for i in range(len(players)): 
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            dice_value = getDiceValue()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            player_current_position = snakeLadder(players[i], playersValue[i][players[i]], dice_value)
            playersValue[i][players[i]] = player_current_position
            checkWin(players[i], playersValue[i][players[i]])


if __name__ == "__main__":
    startGame()
