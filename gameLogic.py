import wheel
import bet
import betTracker

class gameLogic:
    def __init__(self, amount):
        self.amount = amount
        self.wheel = wheel.wheel()
        self.bet = bet.bet()
        self.betTracker = betTracker.betTracker()

    def chooseRowBet(self, row):
        bet = self.bet.betRow(self.amount, row)
        self.betTracker.betList.append(bet)

    def chooseColumnBet(self, col):
        bet = self.bet.betColumn(self.amount, col)
        self.betTracker.betList.append(bet)

    def didIWin(self):
        numberSelected = self.wheel.spinWheel()
        print("You landed on:", numberSelected)
        win = False

        for i in self.betTracker.betList:
            if numberSelected in i[0]:
                win = True

        if(win):
            print("You Won!")
        else:
            print("Sorry, you lost.")

    def showNumbersChosen(self):
        self.betTracker.displayBetList()