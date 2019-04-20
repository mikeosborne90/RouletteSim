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
        numberChoice = euroTableUI.receiveSelectedNumbers()
        squareChoice = euroTableUI.receiveSquareSelections()
        euroTableUI.closeTableWindow()
        for i in range(len(numberChoice)):
            amount = numberChoice[i][1]
            myGame.chooseSingleBet(numberChoice[i][0], amount) #number, amount

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