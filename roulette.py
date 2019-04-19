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
    print("| 1. Bet on a number     |")
    print("| 2. Bet on evens        |")
    print("| 3. Bet on odds         |")
    print("| 4. Bet on reds         |")
    print("| 5. Bet on blacks       |")
    print("| 6. Bet on lows         |")
    print("| 7. Bet on highs        |")
    print("| 8. Spin wheel          |")
    print("| 9. Show Bets           |")
    print("| 10. Clear Bets         |")
    print("| 11. Reset Money        |")
    print("| 12. Exit               |")
    print("<<---------------------->>")
    print("****[Bottom Line:$"+ str(myGame.getTotalMoney()-1000)+ "]****")

    option = input("Enter Option: ")

    if (option == '1'):
        euroTableUI = tableUI.tableUI()
        choice = euroTableUI.receiveSelectedNumbers()
        print("Choose a number 0->36:")
        input("Enter any key to end selections.")
        euroTableUI.closeTableWindow()
        for i in range(len(choice)):
            if(intCheck(choice[i])):
                if(int(choice[i]) >= 0 and int(choice[i]) <= 36):
                    amount = input("How much to bet?: ")
                    if (intCheck(amount)):
                        myGame.chooseSingleBet(choice[i], int(amount))
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
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseRedsBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '5'):
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseBlacksBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '6'):
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseLowsBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '7'):
        amount = input("How much to bet?: ")

        if (intCheck(amount)):
            myGame.chooseHighsBet(int(amount))
        else:
            print("Needs to be an integer value!")

    elif (option == '8'):
        numberOfRuns = input("How many spins?: ")

        if (intCheck(numberOfRuns)):
            for i in range(int(numberOfRuns)):
                myGame.showNumbersChosen()
                myGame.didIWin();
                print("Current Money: ",myGame.getTotalMoney())
        else:
            print("Needs to be an integer value!")

    elif (option == '9'):
        print("([#(s) chosen], multiplier, bet amount)")
        myGame.showNumbersChosen()

    elif (option == '10'):
        myGame.clearBets()

    elif (option == '11'):
        player1.setMoney(initalPlayerFunds)
        print("Current Money: ", myGame.getTotalMoney())

    elif (option == '12'):
        print("Come back soon. :-)")
        exitProgram = True

    else:
        print("Invalid Option, must enter (1->12)")