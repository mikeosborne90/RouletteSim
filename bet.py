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

    def betDouble(self, betAmt, numberChoice, direction):
        """bet = (number & nextNumber, multiplier, amount)"""
        rowLocation = -1 # initializer
        rowNumber = -1 #initializer

        for j in range(len(self.table.numbers)):
            for i in range(len(self.table.numbers[j])):
                if(self.table.numbers[j][i] == numberChoice):
                    rowLocation = i
                    rowNumber = j

        if(direction == "N"): # N for North
            secondNumberRowLocation = rowLocation
            secondNumberRow = rowNumber - 1
        elif(direction == "S"): # S for South
            secondNumberRowLocation = rowLocation
            secondNumberRow = rowNumber + 1
        elif(direction == "E"): # E for East
            secondNumberRowLocation = rowLocation + 1
            secondNumberRow = rowNumber
        elif(direction == "W"): # W for West
            secondNumberRowLocation = rowLocation - 1
            secondNumberRow = rowNumber
        else: #invalid location
            print("Bad Direction")
            secondNumberRowLocation = -1
            secondNumberRow = -1

        if(secondNumberRowLocation >= 0 and secondNumberRowLocation <= 11): # valid
            if(secondNumberRow >= 0 and secondNumberRow <= 2): # valid
                myBet = ([numberChoice, self.table.numbers[secondNumberRow][secondNumberRowLocation]], 17, betAmt)
            else:
                print("row#:", secondNumberRow)
                myBet = [[-1, -1], 17, betAmt] # invalid bet
                print("Invalid row for double bet!")
        else:
            myBet = [[-1, -1], 17 ,betAmt] # invalid bet
            print("Invalid row location for double bet!")

        return myBet

    def betStreet(self, betAmt, numberChoice):
        """bet = (3#'s in a column, multiplier, amount)"""
        if (numberChoice % 3 == 1): # valid choice
            myBet = [[numberChoice, numberChoice+1, numberChoice+2], 11, betAmt]

        else:
            myBet = [[-1, -1], 11, betAmt]  # invalid bet
            print("Invalid location for street bet!")

        return myBet

    def betSixLine(self, betAmt, numberChoice1, numberChoice2):
        """bet = (3#'s in a column, multiplier, amount)"""
        if(abs(numberChoice1 - numberChoice2) == 3): # column to left or right
            if (numberChoice1 % 3 == 1): # valid choice
                if(numberChoice1 > numberChoice2): # verify lower number is added to
                    numberChoice1 = numberChoice2
                myBet = [[numberChoice1, numberChoice1+1, numberChoice1+2], 11, betAmt]
                myBet[0].append(numberChoice1+3)
                myBet[0].append(numberChoice1+4)
                myBet[0].append(numberChoice1+5)

            else:
                myBet = [[-1, -1, -1, -1, -1, -1], 11, betAmt]  # invalid bet
                print("Invalid location for street bet!(1)")
        else:
            myBet = [[-1, -1, -1, -1, -1, -1], 11, betAmt]  # invalid bet
            print("Invalid location for street bet!(2)")

        return myBet