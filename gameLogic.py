import wheel
import bet

class gameLogic:
    def __init__(self, player):
        self.player = player
        self.wheel = wheel.wheel()
        self.bet = bet.bet()
        self.betList = list([])

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

    def didIWin(self):
        numberSelected = self.wheel.spinWheelEuropean()
        print("You landed on:", numberSelected)
        win = False
        result = 0
        totalBetAmount = 0

        for i in self.betList:
            totalBetAmount += i[2]
            if numberSelected in i[0]:
                win = True
                result = result + ((i[1] * i[2]) + i[2])

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