import gameLogic as gL
import player as ply
import tableUI
import csv

def intCheck(stringToCheck):
    """Used to verify a string can be converted to an integer."""
    try:
        int(stringToCheck)
        return True
    except ValueError:
        return False

initalPlayerFunds = 1000 #Player starts with arbitrary amount of $1000
player1 = ply.player(initalPlayerFunds)
myGame = gL.gameLogic(player1, 1) # 1 = european version by default
windows = list([])

exitProgram = False

while exitProgram != True:
    print("~~[Current Money:$"+ str(myGame.getTotalMoney())+ "]~~")
    print("<<--Roulette Simulator-->>")
    print("| 1. Place Bets(euro)    |")
    print("| 2. Spin Wheel          |")
    print("| 3. Betting Strategies  |")
    print("| 4. Run 5 times         |")
    print("| 5. Show Bets           |")
    print("| 6. Clear Bets          |")
    print("| 7. Clear Bet Strats    |")
    print("| 8. Reset Money         |")
    print("| 9. Exit                |")
    print("| 4. Show Bets           |")
    print("| 5. Clear Bets          |")
    print("| 6. Clear Bet Strats    |")
    print("| 7. Reset Money         |")
    print("| 8. Exit                |")
    print("| 9. Place Bets(amer)    |")
    print("| 10.Place Bets(no zero) |")
    print("<<---------------------->>")
    print("****[Bottom Line:$"+ str(myGame.getTotalMoney()-1000)+ "]****")

    option = input("Enter Option: ")

    if (option == '1' or option == '9' or option == '10'):
        for aWindow in windows:   # clears any existing windows
            try:
                aWindow.closeTableWindow()
            except:
                pass
        windows.clear()

        if(option == '1'):
            tableUIWindow = tableUI.tableUI(1)  # 1 for european
        elif(option == '9'):
            myGame = gL.gameLogic(player1, 2)
            tableUIWindow = tableUI.tableUI(2)  # 2 for american
        else:
            myGame = gL.gameLogic(player1, 3)
            tableUIWindow = tableUI.tableUI(3)  # 2 for american

        windows.append(tableUIWindow)
        input("Enter any key to end selections.")
        numberChoice = tableUIWindow.receiveSelectedNumbers()
        squareChoice = tableUIWindow.receiveSquareSelections()
        lowsChoice = tableUIWindow.receiveLowsSelection()
        highsChoice = tableUIWindow.receiveHighsSelection()
        evensChoice = tableUIWindow.receiveEvensSelection()
        oddsChoice = tableUIWindow.receiveOddsSelection()
        redChoice = tableUIWindow.receiveRedSelection()
        blackChoice = tableUIWindow.receiveBlackSelection()
        dozensChoice = tableUIWindow.receiveSelectedDozens()
        twoToOneChoice = tableUIWindow.receiveSelected2to1()
        splitBetsDir1 = tableUIWindow.receiveSelectedSplitDir1()
        splitBetsDir2 = tableUIWindow.receiveSelectedSplitDir2()
        sixLineBets = tableUIWindow.receiveSelectedSixLine()
        streetBets = tableUIWindow.receiveSelectedStreet()
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
        # Six Line Bets
        for i in sixLineBets:
            amount = i[1]
            if(i[0] == 0):
                myGame.chooseSixLineBet(1,4,amount);
            elif(i[0] == 1):
                myGame.chooseSixLineBet(4,7,amount);
            elif(i[0] == 2):
                myGame.chooseSixLineBet(7,10,amount);
            elif(i[0] == 3):
                myGame.chooseSixLineBet(10,13,amount);
            elif(i[0] == 4):
                myGame.chooseSixLineBet(13,16,amount);
            elif(i[0] == 5):
                myGame.chooseSixLineBet(16,19,amount);
            elif(i[0] == 6):
                myGame.chooseSixLineBet(19,22,amount);
            elif(i[0] == 7):
                myGame.chooseSixLineBet(22,25,amount);
            elif(i[0] == 8):
                myGame.chooseSixLineBet(25,28,amount);
            elif(i[0] == 9):
                myGame.chooseSixLineBet(28,31,amount);
            else: # i[0] == 10
                myGame.chooseSixLineBet(31,34,amount);
        # Street Bets
        for i in streetBets:
            amount = i[1]
            myGame.chooseColumnBet(i[0],amount)

    elif (option == '2'):
        myGame.saveOriginalBets()  # Used for martingale
        csvData = list([["run", "total"]])
        numberOfRuns = input("How many spins?: ")
        if (intCheck(numberOfRuns)):
            twentyPercentOfRuns = int(int(numberOfRuns) * 0.20)
            for i in range(int(numberOfRuns)):
                myGame.showNumbersChosen()
                myGame.didIWin()
                print("Run#"+str(i+1)+" Current Money: "+ str(myGame.getTotalMoney()))
                csvData.append([i+1, myGame.getTotalMoney()])  # run# and currentMoney
                if(myGame.dAlembertEqualWinLoss is True):
                    if((i+1) >= twentyPercentOfRuns and myGame.returnWinCount() == myGame.returnLossCount()):
                        break
            print("Wins: " + str(myGame.returnWinCount()) + ", Losses: " + str(myGame.returnLossCount()))
            myGame.resetWinAndLossCount()
        else:
            print("Needs to be an integer value!")

        with open('results.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)
        csvFile.close()
        myGame.loadOriginalBets()
        myGame.clearOriginalBets()

    elif (option == '3'):
        print("<<--Roulette Simulator-->>")
        print("| 1. Martingale          |")
        print("| 2. Rev Martingale      |")
        print("| 3. D'Alembert(full run)|")
        print("| 4. D'Alembert(win=loss)|")
        print("| 5. Fibonacci           |")
        print("| 6. Back                |")
        print("<<---------------------->>")

        subOption = input("Enter Option: ")

        if (subOption == '1'):
            myGame.enableMartingale()
            print("Martingale Enabled!")

        elif (subOption == '2'):
            myGame.enableRevMartingale()
            print("Reverse Martingale Enabled!")

        elif (subOption == '3'):
            myGame.disableDAlembertWinsEqualsLosses()
            myGame.enableDAlembert()
            print("D'Alembert(full run) Enabled!")

        elif (subOption == '4'):
            myGame.enableDAlembert()
            myGame.enableDAlembertWinsEqualsLosses()
            print("D'Alembert(win=loss) Enabled!")

        elif (subOption == '5'):
            myGame.enableFibonacci()
            print("Fibonacci Enabled!")

        elif (subOption == '6'):
            print("Going Back to Main Menu!")

        else:
            print("Invalid Option, must enter (1->6)")

    elif (option == '4'):
        numberOfRuns = input("How many spins?: ")

        for x in range(1, 6):
            player1.setMoney(initalPlayerFunds)
            myGame.saveOriginalBets()  # Used for martingale
            csvData = list([["run", "total"]])
            if (intCheck(numberOfRuns)):
                twentyPercentOfRuns = int(int(numberOfRuns) * 0.20)
                for i in range(int(numberOfRuns)):
                    myGame.showNumbersChosen()
                    myGame.didIWin()
                    print("Run#" + str(i + 1) + " Current Money: " + str(myGame.getTotalMoney()))
                    csvData.append([i + 1, myGame.getTotalMoney()])  # run# and currentMoney
                    if (myGame.dAlembertEqualWinLoss is True):
                        if ((i + 1) >= twentyPercentOfRuns and myGame.returnWinCount() == myGame.returnLossCount()):
                            break
                print("Wins: " + str(myGame.returnWinCount()) + ", Losses: " + str(myGame.returnLossCount()))
                myGame.resetWinAndLossCount()
            else:
                print("Needs to be an integer value!")

            with open('results'+str(x)+'.csv', 'w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
            csvFile.close()
            myGame.loadOriginalBets()
            myGame.clearOriginalBets()

    elif (option == '5'):
        for aWindow in windows:   # clears any existing windows
            try:
                aWindow.closeTableWindow()
            except:
                pass
        windows.clear()
        myGame.clearBets()
        print("([#(s) chosen], multiplier, bet amount)")
        myGame.showNumbersChosen()

    elif (option == '6'):
        myGame.clearBets()

    elif (option == '7'):
        myGame.disableBettingStrategies()
        print("All betting strats cleared!")

    elif (option == '8'):
        player1.setMoney(initalPlayerFunds)
        print("Current Money: ", myGame.getTotalMoney())

    elif (option == '9'):
        print("Come back soon. :-)")
        exitProgram = True

    else:
        print("Invalid Option, must enter (1->9)")