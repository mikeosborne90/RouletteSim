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
        myBet = ([self.table.numbers[0][colNum], self.table.numbers[1][colNum], self.table.numbers[2][colNum]], 2, betAmt)
        return myBet