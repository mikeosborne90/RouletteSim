import table

class bet:
    def __init__(self):
        self.table = table.table()

    def betRow(self, betAmt, rowNum):
        """bet = (row#, multiplier, amount)"""
        myBet = (self.table.numbers[rowNum - 1], 2, betAmt)
        return myBet

    def betColumn(self, betAmt, colNum):
        """bet = (col#, multiplier, amount)"""
        myBet = ([self.table.numbers[0][colNum], self.table.numbers[1][colNum], self.table.numbers[2][colNum]], 11, betAmt)
        return myBet

    def betSingle(self, betAmt, numberChoice):
        """bet = (number, multiplier, amount)"""
        myBet = ([numberChoice], 35, betAmt)
        return myBet

    def betOdds(self, betAmt):
        """bet = (odd#'s, multiplier, amount)"""
        myBet = ([i for i in range(1,37) if i%2 == 1], 1, betAmt) #fetches odd numbers 1->35
        return myBet

    def betEvens(self, betAmt):
        """bet = (even#'s, multiplier, amount)"""
        myBet = ([i for i in range(1,37) if i%2 == 0], 1, betAmt) #fetches odd numbers 1->35
        return myBet

    def betReds(self, betAmt):
        """bet = (red#'s, multiplier, amount)"""
        reds = []
        for j in range(3):
            for i in range(12):
                if (self.table.colors[j][i] == 0):
                    reds.append(self.table.numbers[j][i])

        myBet = (reds, 1, betAmt)
        return myBet

    def betBlacks(self, betAmt):
        """bet = (black#'s, multiplier, amount)"""
        blacks = []
        for j in range(3):
            for i in range(12):
                if (self.table.colors[j][i] == 1):
                    blacks.append(self.table.numbers[j][i])

        myBet = (blacks, 1, betAmt)
        return myBet