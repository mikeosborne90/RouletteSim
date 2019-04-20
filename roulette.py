import gameLogic as gL
import player as ply
import tableUI

def intCheck(stringToCheck):
    """Used to verify a string can be converted to an integer."""
    try:
        int(stringToCheck)
        return True
    except ValueError:
        return False

initalPlayerFunds = 1000 #Player starts with arbitrary amount of $1000
player1 = ply.player(initalPlayerFunds)
myGame = gL.gameLogic(player1)

exitProgram = False

while exitProgram != True:
    print("~~[Current Money:$"+ str(myGame.getTotalMoney())+ "]~~")
    print("<<--Roulette Simulator-->>")
    print("| 1. Place Bets          |")
    print("| 2. Spin Wheel          |")
    print("| 3. Show Bets           |")
    print("| 4. Clear Bets          |")
    print("| 5. Reset Money         |")
    print("| 6. Exit                |")
    print("<<---------------------->>")
    print("****[Bottom Line:$"+ str(myGame.getTotalMoney()-1000)+ "]****")

    option = input("Enter Option: ")

    if (option == '1'):
        euroTableUI = tableUI.tableUI()
        input("Enter any key to end selections.")
        euroTableUI.closeTableWindow()
        numberChoice = euroTableUI.receiveSelectedNumbers()
        squareChoice = euroTableUI.receiveSquareSelections()
        lowsChoice = euroTableUI.receiveLowsSelection()
        highsChoice = euroTableUI.receiveHighsSelection()
        evensChoice = euroTableUI.receiveEvensSelection()
        oddsChoice = euroTableUI.receiveOddsSelection()
        redChoice = euroTableUI.receiveRedSelection()
        blackChoice = euroTableUI.receiveBlackSelection()
        dozensChoice = euroTableUI.receiveSelectedDozens()
        twoToOneChoice = euroTableUI.receiveSelected2to1()
        splitBetsDir1 = euroTableUI.receiveSelectedSplitDir1()
        splitBetsDir2 = euroTableUI.receiveSelectedSplitDir2()
# Single Number Bets
        for i in range(len(numberChoice)):
            amount = numberChoice[i][1]
            myGame.chooseSingleBet(numberChoice[i][0], amount) #number, amount
# Square Bets
        for i in squareChoice:
            amount = i[1]
            if(i[0] <= 1):
                myGame.chooseSquareBet(i[0] + 1, i[0] + 4, amount)
            elif(i[0] <= 3):
                myGame.chooseSquareBet(i[0] + 2, i[0] + 5, amount)
            elif(i[0] <= 5):
                myGame.chooseSquareBet(i[0] + 3, i[0] + 6, amount)
            elif(i[0] <= 7):
                myGame.chooseSquareBet(i[0] + 4, i[0] + 7, amount)
            elif(i[0] <= 9):
                myGame.chooseSquareBet(i[0] + 5, i[0] + 8, amount)
            elif(i[0] <= 11):
                myGame.chooseSquareBet(i[0] + 6, i[0] + 9, amount)
            elif(i[0] <= 13):
                myGame.chooseSquareBet(i[0] + 7, i[0] + 10, amount)
            elif(i[0] <= 15):
                myGame.chooseSquareBet(i[0] + 8, i[0] + 11, amount)
            elif (i[0] <= 17):
                myGame.chooseSquareBet(i[0] + 9, i[0] + 12, amount)
            elif (i[0] <= 19):
                myGame.chooseSquareBet(i[0] + 10, i[0] + 13, amount)
            else: # i <= 21
                myGame.chooseSquareBet(i[0] + 11, i[0] + 14, amount)
# Lows Bet(1-18)
        if(lowsChoice[0] is True):
            amount = lowsChoice[1]
            myGame.chooseLowsBet(amount)
# Highs Bet (19-36)
        if(highsChoice[0] is True):
            amount = highsChoice[1]
            myGame.chooseHighsBet(amount)
# Evens Bet
        if (evensChoice[0] is True):
            amount = evensChoice[1]
            myGame.chooseEvensBet(amount)
# Odds Bet
        if (oddsChoice[0] is True):
            amount = oddsChoice[1]
            myGame.chooseOddsBet(amount)
# Red Bet
        if (redChoice[0] is True):
            amount = redChoice[1]
            myGame.chooseRedsBet(amount)
# Black Bet
        if (blackChoice[0] is True):
            amount = blackChoice[1]
            myGame.chooseBlacksBet(amount)
# Dozens Bet
        for i in range(len(dozensChoice)):
            amount = dozensChoice[i][1]
            if(dozensChoice[i][0] == 0):
                myGame.chooseDozen1Bet(amount)
            elif(dozensChoice[i][0] == 1):
                myGame.chooseDozen2Bet(amount)
            else:
                myGame.chooseDozen3Bet(amount)
# 2-to-1 Bet
        for i in range(len(twoToOneChoice)):
            amount = twoToOneChoice[i][1]
            row = twoToOneChoice[i][0]
            myGame.chooseRowBet(row, amount)
# Split Direction1 Bets
        for i in splitBetsDir1:
            amount = i[1]
            myGame.chooseDoubleBet(i[0]+1, "W", amount) # W is for west which corresponds dir in table.py

# Split Direction2 Bets
        for i in splitBetsDir2:
            amount = i[1]
            if(i[0] <= 1):
                myGame.chooseDoubleBet(i[0] + 1, "N", amount)  # N is for west which corresponds dir in table.py
            elif(i[0] <= 3):
                myGame.chooseDoubleBet(i[0] + 2, "N", amount)
            elif(i[0] <= 5):
                myGame.chooseDoubleBet(i[0] + 3, "N", amount)
            elif(i[0] <= 7):
                myGame.chooseDoubleBet(i[0] + 4, "N", amount)
            elif(i[0] <= 9):
                myGame.chooseDoubleBet(i[0] + 5, "N", amount)
            elif(i[0] <= 11):
                myGame.chooseDoubleBet(i[0] + 6, "N", amount)
            elif(i[0] <= 13):
                myGame.chooseDoubleBet(i[0] + 7, "N", amount)
            elif(i[0] <= 15):
                myGame.chooseDoubleBet(i[0] + 8, "N", amount)
            elif(i[0] <= 17):
                myGame.chooseDoubleBet(i[0] + 9, "N", amount)
            elif(i[0] <= 19):
                myGame.chooseDoubleBet(i[0] + 10, "N", amount)
            elif(i[0] <= 21):
                myGame.chooseDoubleBet(i[0] + 11, "N", amount)
            else: # i[0] <= 23
                myGame.chooseDoubleBet(i[0] + 12, "N", amount)

    elif (option == '2'):
        numberOfRuns = input("How many spins?: ")

        if (intCheck(numberOfRuns)):
            for i in range(int(numberOfRuns)):
                myGame.showNumbersChosen()
                myGame.didIWin();
                print("Current Money: ",myGame.getTotalMoney())
        else:
            print("Needs to be an integer value!")

    elif (option == '3'):
        print("([#(s) chosen], multiplier, bet amount)")
        myGame.showNumbersChosen()

    elif (option == '4'):
        myGame.clearBets()

    elif (option == '5'):
        player1.setMoney(initalPlayerFunds)
        print("Current Money: ", myGame.getTotalMoney())

    elif (option == '6'):
        print("Come back soon. :-)")
        exitProgram = True

    else:
        print("Invalid Option, must enter (1->6)")