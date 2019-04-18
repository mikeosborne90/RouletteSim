import gameLogic as gL
import player as ply

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
    print("| 1. Bet on a number     |")
    print("| 2. Bet on evens        |")
    print("| 3. Bet on odds         |")
    print("| 4. Spin wheel          |")
    print("| 5. Show Bets           |")
    print("| 6. Clear Bets          |")
    print("| 7. Reset Money         |")
    print("| Any other Key = exit   |")
    print("<<---------------------->>")
    print("****[Bottom Line:$"+ str(myGame.getTotalMoney()-1000)+ "]****")

    option = input("Enter Option: ")

    if (option == '1'):
        choice = input("Choose a number 0->36: ")

        if(intCheck(choice)):
            if(int(choice) >= 0 and int(choice) <= 36):
                amount = input("How much to bet?: ")
                if (intCheck(amount)):
                    myGame.chooseSingleBet(int(choice), int(amount))
                else:
                    print("Needs to be an integer value!")
            else:
                print("Number has to be betweem 0 and 36!")
        else:
            print("Needs to be an integer value!")

    elif (option == '2'):
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseEvensBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '3'):
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseOddsBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '4'):
        numberOfRuns = input("How many spins?: ")

        if (intCheck(numberOfRuns)):
            for i in range(int(numberOfRuns)):
                myGame.showNumbersChosen()
                myGame.didIWin();
                print("Current Money: ",myGame.getTotalMoney())
        else:
            print("Needs to be an integer value!")

    elif (option == '5'):
        print("([#(s) chosen], multiplier, bet amount)")
        myGame.showNumbersChosen()

    elif (option == '6'):
        myGame.clearBets()

    elif (option == '7'):
        player1.setMoney(initalPlayerFunds)
        print("Current Money: ", myGame.getTotalMoney())

    else:
        exitProgram = True