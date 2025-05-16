import random

#SETTINGS
CHIPS = 10

#DICE VISUALS
CLOSING_BOX_LINE = " ----- "
diceVisual = {
    1 : { "Line1" : "|     |",
         "Line2" :  "|  @  |",
         "Line3" :  "|     |" ,
         },
    2 : { "Line1" : "| @   |",
         "Line2" :  "|     |",
         "Line3" :  "|   @ |" ,
         },
    3 : { "Line1" : "| @   |",
         "Line2" :  "|  @  |",
         "Line3" :  "|   @ |" ,
         },
    4 : { "Line1" : "| @ @ |",
         "Line2" :  "|     |",
         "Line3" :  "| @ @ |" ,
         },
    5 : { "Line1" : "| @ @ |",
         "Line2" :  "|  @  |",
         "Line3" :  "| @ @ |" ,
         },
    6 : { "Line1" : "| @ @ |",
         "Line2" :  "| @ @ |",
         "Line3" :  "| @ @ |" ,
         },
}

def displayDices(currentRoll):
    lines = []
    for roll in currentRoll:
        for i in range(5):
            if i == 0 or i == 4:
                if len(lines) < i + 1:
                    lines.append(CLOSING_BOX_LINE)
                else:
                    lines[i] += CLOSING_BOX_LINE
            else:
                if len(lines) < i + 1:
                    lines.append(diceVisual[i+1]["Line" + str(i)])
                else:
                    lines[i] += diceVisual[i+1]["Line" + str(i)]

    for line in lines:
        print(line)
                
    
displayDices([3,2,1])

def Roll():
    return random.randint(1,6)
    
    
def DetermineDices(commands, currentRoll):
    #determine what dices to roll
    for char in commands:
        if not char in "0123":
            continue
        if char == "0":
            return None
        elif int(char) <= 3 and int(char) >= 1:
            currentRoll[int(char)] = Roll()
    return currentRoll

def EvaluatePoints(currentRoll):
    rollList = sorted(currentRoll.values())
    if rollList == [1,2,3]:
        print("You got a LOCO")
        return 290
    elif rollList == [4,5,6]:
        print("You got a POCO")
        return 999
    elif rollList[0] == rollList[1] == rollList[2]:
        print("You got a Mirror" , end="")
        print(f" {rollList[0]} " * 3)
        return (rollList[0] + 3) * 100 #goes from 400 > than LOCO, to 900 less than POCO.
    else:
        points = 0 #max is 260
        for dice in rollList:
            if dice == 1:
                points += 100
            elif dice == 6:
                points += 60
            else:
                points += dice
        return points
        
                
def ResetPoints(players):
    players["Points"] = []
                
    
def main():
    #Player amount, naming.
    playerCount = int(input("Enter the amount of players"))
    players = {}
    for index in range(playerCount):
        gameIndex = index + 1
        players[gameIndex] = {"Name" : input(f"You are player {gameIndex}. What is your name?"), "Chips" : CHIPS, "Points" : []}

    """
    #roll dices and display using commands
    for i in range(10): 
        currentRoll = DetermineDices("123", {})
        EvaluatePoints(currentRoll)
    """

    #Get who starts the round
    
    #Start the round.
    
    #Get the first first roll and display
    
    #shows options to change dices 0 - keep dice, 1 - first dice , 2 second dice and 3 third dice. add them to roll more than one.
    
    #go to next player.
        
    





