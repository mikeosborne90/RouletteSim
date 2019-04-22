import wheel
import bet

class gameLogic:
    def __init__(self, player, version):
        self.version = version
        self.player = player
        self.wheel = wheel.wheel()
        self.bet = bet.bet()
        self.betList = list([])
        self.startingBetAmountList = list([])
        self.prevBetAmountList = list([0,1])
        self.martingale = False
        self.revMartingale = False
        self.dAlembert = False
        self.dAlembertEqualWinLoss = False
        self.fibonacci = False
        self.winCount = 0
        self.lossCount = 0

    def chooseRowBet(self, row, betSize):
        bet = self.bet.betRow(betSize, row)
        self.betList.append(bet)
        print("You bet "+str(betSize)+" on row "+str(row))

    def chooseColumnBet(self, col, betSize):
        bet = self.bet.betColumn(betSize, col)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on column " + str(col))

    def chooseSingleBet(self, number, betSize):
        bet = self.bet.betSingle(betSize, number)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on number " + str(number))

    def chooseOddsBet(self, betSize):
        bet = self.bet.betOdds(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on odds")

    def chooseEvensBet(self, betSize):
        bet = self.bet.betEvens(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on evens")

    def chooseRedsBet(self, betSize):
        bet = self.bet.betReds(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on reds")

    def chooseBlacksBet(self, betSize):
        bet = self.bet.betBlacks(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on blacks")

    def chooseLowsBet(self, betSize):
        bet = self.bet.betLows(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on lows(1-18)")

    def chooseHighsBet(self, betSize):
        bet = self.bet.betHighs(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on highs(19-36)")

    def chooseDozen1Bet(self, betSize):
        bet = self.bet.betDozen1(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on highs(1-12)")

    def chooseDozen2Bet(self, betSize):
        bet = self.bet.betDozen2(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on highs(13-24)")

    def chooseDozen3Bet(self, betSize):
        bet = self.bet.betDozen3(betSize)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on highs(25-36)")

    def chooseDoubleBet(self, number, direction, betSize):
        bet = self.bet.betDouble(betSize, number, direction)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on " + str(bet[0][0]) + " and " + str(bet[0][1]))

    def chooseSixLineBet(self, number1, number2, betSize):
        bet = self.bet.betSixLine(betSize, number1, number2)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on Six Line " + str(number1) + " and " + str(number2))

    def chooseSquareBet(self, number1, number2, betSize):
        bet = self.bet.betSquare(betSize, number1, number2)
        self.betList.append(bet)
        print("You bet " + str(betSize) + " on square " + str(number1) + " and " + str(number2))

    def didIWin(self):
        if(self.version == 1): # 1 for European
            numberSelected = self.wheel.spinWheelEuropean()
        elif(self.version == 2): # 2 for American
            numberSelected = self.wheel.spinWheelAmerican()
        else:
            numberSelected = self.wheel.spinWheelNoZeroes()

        print("You landed on:", numberSelected)
        win = False
        result = 0
        totalBetAmount = 0

        for i in self.betList:
            totalBetAmount += i[2]
            if numberSelected in i[0]:
                win = True
                result = result + ((i[1] * i[2]) + i[2])

        if(win):
            self.winCount += 1
        else:
            self.lossCount += 1

        if (self.martingale and win is False):  # if enabled double bet on loss for next bet
            self.martingaleLoss()

        if (self.martingale and win is True):  # if enabled bet initial amount
            self.martingaleWin()

        if (self.revMartingale and win is True): # opposite for reverse
            self.martingaleLoss()                # martingale win does same as rev martingale loss

        if (self.revMartingale and win is False):
            self.martingaleWin()

        if(self.dAlembert and win is True):
            self.dAlembertWin()

        if(self.dAlembert and win is False):
            self.dAlembertLoss()

        if(self.fibonacci and win is False):
            self.fibonacciLoss()

        if(self.fibonacci and win is True):
            self.fibonacciWin()


        self.player.removeFromMoney(totalBetAmount)

        if(win):
            self.player.addToMoney(result)
            print("You Won "+ str(result) +"!")
        else:
            print("Sorry, you lost "+ str(totalBetAmount) +".")

    def getTotalMoney(self):
        return self.player.getMoney()

    def showNumbersChosen(self):
        print(self.betList)

    def clearBets(self):
        self.betList = list([])

    def martingaleLoss(self):
        """If you lose double wager."""
        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] *= 2
            self.betList[i] = tuple(self.betList[i])

    def martingaleWin(self):
        """If you win bet original bet again."""
        if(len(self.betList) == len(self.startingBetAmountList)):
            for i in range(len(self.betList)):
                self.betList[i] = list(self.betList[i])
                self.betList[i][2] = self.startingBetAmountList[i]
                self.betList[i] = tuple(self.betList[i])
        else:
            print("Cannot do martingale when adding more bets than initial bets!")

    def saveOriginalBets(self):
        for i in self.betList:
            self.startingBetAmountList.append(i[2])

    def loadOriginalBets(self):
        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] = self.startingBetAmountList[i]
            self.betList[i] = tuple(self.betList[i])

    def clearOriginalBets(self):
        self.startingBetAmountList.clear()

    def dAlembertWin(self):
        """If you win decrease by 1"""
        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            if(self.betList[i][2] > 1): # don't decrement below $1
                self.betList[i][2] -= 1
            self.betList[i] = tuple(self.betList[i])

    def dAlembertLoss(self):
        """If you lose increase by 1"""
        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] += 1
            self.betList[i] = tuple(self.betList[i])

    def fibonacciWin(self):
        """If you win go 2#'s back in sequence."""
        listLength = len(self.prevBetAmountList)
        if(listLength <= 3):
            betSize = 1
        else:
            betSize = self.prevBetAmountList[listLength-3] # go back to 2 #'s before
            self.prevBetAmountList.pop() # remove last 2 elements on win
            self.prevBetAmountList.pop()

        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] = betSize
            self.betList[i] = tuple(self.betList[i])


    def fibonacciLoss(self):
        """If you lose add prev 2#'s in sequence."""
        listLength = len(self.prevBetAmountList)

        betSize1 = self.prevBetAmountList[listLength-1]
        betSize2 = self.prevBetAmountList[listLength-2]
        self.prevBetAmountList.append(betSize1+betSize2)

        for i in range(len(self.betList)):
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] = betSize1 + betSize2
            self.betList[i] = tuple(self.betList[i])


    def enableMartingale(self):
        self.martingale = True
        self.revMartingale = False
        self.dAlembert = False
        self.fibonacci = False

    def enableRevMartingale(self):
        self.revMartingale = True
        self.martingale = False
        self.dAlembert = False
        self.fibonacci = False

    def enableDAlembert(self):
        self.dAlembert = True
        self.revMartingale = False
        self.martingale = False
        self.fibonacci = False

    def enableDAlembertWinsEqualsLosses(self):
        self.dAlembertEqualWinLoss = True

    def disableDAlembertWinsEqualsLosses(self):
        self.dAlembertEqualWinLoss = False

    def enableFibonacci(self):
        self.fibonacci = True
        self.dAlembert = False
        self.revMartingale = False
        self.martingale = False
        for i in range(len(self.betList)): # if fibonacci, start bet size at 1
            self.betList[i] = list(self.betList[i])
            self.betList[i][2] = 1
            self.betList[i] = tuple(self.betList[i])
        for j in range(len(self.startingBetAmountList)):
            self.startingBetAmountList[j] = 1

    def disableBettingStrategies(self):
        self.martingale = False
        self.revMartingale = False
        self.dAlembert = False
        self.dAlembertEqualWinLoss = False
        self.fibonacci = False

    def returnWinCount(self):
        return self.winCount

    def returnLossCount(self):
        return self.lossCount

    def resetWinAndLossCount(self):
        self.winCount = 0
        self.lossCount = 0