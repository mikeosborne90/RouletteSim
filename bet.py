import re
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

    def betLows(self, betAmt):
        """bet = (low#'s, multiplier, amount)"""
        myBet = ([i for i in range(1,19)], 1, betAmt)
        return myBet

    def betHighs(self, betAmt):
        """bet = (high#'s, multiplier, amount)"""
        myBet = ([i for i in range(19,37)], 1, betAmt)
        return myBet

    def betDozen1(self, betAmt):
        """bet = (1-12, multiplier, amount)"""
        myBet = ([i for i in range(1,13)], 2, betAmt)
        return myBet

    def betDozen2(self, betAmt):
        """bet = (13-24, multiplier, amount)"""
        myBet = ([i for i in range(13,25)], 2, betAmt)
        return myBet

    def betDozen3(self, betAmt):
        """bet = (25-36, multiplier, amount)"""
        myBet = ([i for i in range(25,37)], 2, betAmt)
        return myBet

    # def betNumberDirection(self, betAmt, numDirection):
    #     """i.e 3R(right) or 5U(up)"""
    #     #matches numbers in string
    #     numbers = re.findall(r'\d+', numDirection)
    #     #matches letters in string
    #     direction = re.findall(r'\D', numDirection)
    #     num = int(numbers[0])
    #     dir = direction[0]
    #
    #     if (num > 3 and num < 34):
    #         if(dir == 'U'): #up
    #
    #     myBet = ([i for i in range(1,13)], 2, betAmt)
    #     return myBet