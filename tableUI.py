import tkinter as tk

class tableUI:
    def __init__(self, version):
        self.version = version # 1 for Euro, 2 for American
        self.betAmount = 1  # set to $1 as default
        self.selectedNumbers = list([])
        self.selectedSquares = list([])
        self.lowsBet = (False, 1)  #initialize to $1
        self.highsBet = (False, 1)
        self.evensBet = (False, 1)  #initialize to $1
        self.oddsBet = (False, 1)
        self.redBet = (False, 1)  #initialize to $1
        self.blackBet = (False, 1)
        self.selectedDozens = list([])
        self.selected2to1 = list([])
        self.selectedSplitDir1 = list([])
        self.selectedSplitDir2 = list([])
        self.selectedSixLine = list([])
        self.selectedStreet = list([])

        self.root = tk.Tk()
        self.root.title('CSCI 154 Roulette Simulator')
        self.root.resizable(0, 0)  # Makes image non-resizable
        if(version == 1):
            self.image = tk.PhotoImage(file="images/euroBoard.png")
        elif(version == 2):
            self.image = tk.PhotoImage(file="images/amerBoard.png")
        else:
            self.image = tk.PhotoImage(file="images/noZeroBoard.png")

        self.label = tk.Label(self.root, image=self.image)
        self.label.pack()
#----------------------------- Dollar Amount Buttons ------------------------------------------------------
        self.oneDollarButton = tk.Button(text = '$1', fg ='black', command=self.amountToBet1)
        self.oneDollarButton.place(x = 30, y =100)

        self.fiveDollarButton = tk.Button(text = '$5', fg ='black', command=self.amountToBet5)
        self.fiveDollarButton.place(x = 30, y =150)

        self.tenDollarButton = tk.Button(text = '$10', fg ='black', command=self.amountToBet10)
        self.tenDollarButton.place(x = 28, y =200)

        self.twentyDollarButton = tk.Button(text = '$20', fg ='black', command=self.amountToBet20)
        self.twentyDollarButton.place(x = 28, y =250)

        self.twentyFiveDollarButton = tk.Button(text='$25', fg='black', command=self.amountToBet25)
        self.twentyFiveDollarButton.place(x=28, y=300)

        self.fiftyDollarButton = tk.Button(text = '$50', fg ='black', command=self.amountToBet50)
        self.fiftyDollarButton.place(x = 28, y =350)

        self.seventyDollarButton = tk.Button(text = '$70', fg ='black', command=self.amountToBet70)
        self.seventyDollarButton.place(x = 28, y =400)

        self.hundredDollarButton = tk.Button(text = '$100', fg ='black', command=self.amountToBet100)
        self.hundredDollarButton.place(x = 25, y =450)
# ----------------------------- Outside Bet Buttons ---------------------------------------------------------
        self.oneTo18Image = tk.PhotoImage(file="images/1-18.png")
        self.oneTo18Button = tk.Button(image=self.oneTo18Image, command=lambda n = True: self.placeLowsHighsBet(n))
        self.oneTo18Button.place(x = 124, y = 114)

        self.nineteenTo36Image = tk.PhotoImage(file="images/19-36.png")
        self.nineteenTo36Button = tk.Button(image=self.nineteenTo36Image, command=lambda n = False: self.placeLowsHighsBet(n))
        self.nineteenTo36Button.place(x = 124, y = 698)

        self.evenImage = tk.PhotoImage(file="images/even.png")
        self.evenButton = tk.Button(image=self.evenImage, command=lambda n = True: self.placeEvenOddsBet(n))
        self.evenButton.place(x = 124, y = 226)

        self.oddImage = tk.PhotoImage(file="images/odd.png")
        self.oddButton = tk.Button(image=self.oddImage, command=lambda n = False: self.placeEvenOddsBet(n))
        self.oddButton.place(x = 124, y = 588)

        self.redImage = tk.PhotoImage(file="images/red.png")
        self.redButton = tk.Button(image=self.redImage, command=lambda n = True: self.placeRedBlackBet(n))
        self.redButton.place(x = 124, y = 346)

        self.blackImage = tk.PhotoImage(file="images/black.png")
        self.blackButton = tk.Button(image=self.blackImage, command=lambda n = False: self.placeRedBlackBet(n))
        self.blackButton.place(x = 124, y = 464)
# ----------------------------- Dozen Buttons ---------------------------------------------------------------
        self.dozenButton = []
        self.dozenImage = []
        for i in range(0, 3):
            self.dozenImage.append(tk.PhotoImage(file="images/dozen" + str(i+1) + ".png"))
            self.dozenButton.append(tk.Button(image=self.dozenImage[i], command=lambda n = i: self.placeDozenBet(n)))

        xCoord = 201
        for i in range(0, 3):
            if (i % 3 == 0):
                yCoord = 130
            elif (i % 3 == 1):
                yCoord = 366
            else:
                yCoord = 605
            self.dozenButton[i].place(x=xCoord, y=yCoord)
# ----------------------------- 2to1 Buttons ---------------------------------------------------------------
        self.twoToOneButton = []
        self.twoToOneImage = []
        for i in range(0, 3):
            self.twoToOneImage.append(tk.PhotoImage(file="images/2to1.png"))
            self.twoToOneButton.append(tk.Button(image=self.twoToOneImage[i], command=lambda n = i: self.place2to1Bet(n)))

        yCoord = 812
        for i in range(0, 3):
            if (i % 3 == 0):
                xCoord = 288
            elif (i % 3 == 1):
                xCoord = 422
            else:
                xCoord = 557

            self.twoToOneButton[i].place(x=xCoord, y=yCoord)
#----------------------------- Number Buttons ---------------------------------------------------------------
        self.numberButton = []
        self.numberImage = []
        for i in range(0, 37):
            self.numberImage.append(tk.PhotoImage(file="images/" + str(i) + ".png"))
            self.numberButton.append(tk.Button(image=self.numberImage[i], command=lambda n = i: self.placeNumberBet(n)))

        if(self.version == 1):
            self.numberButton[0].place(x=426, y=46)
        elif(self.version == 2): # american board
            self.numberButton[0].place(x=354, y=46)
            self.doubleZeroButtonImage = tk.PhotoImage(file="images/00.png")
            self.doubleZeroButton = tk.Button(image=self.doubleZeroButtonImage, command=lambda n = 37: self.placeNumberBet(n)) # 00 represented as 37
            self.doubleZeroButton.place(x=496, y=46)
        #if noZero board no need to place 0 buttons

        yCoord = 102
        for i in range(1, 37):
            if (i % 3 == 1):
                xCoord = 288
                if (i > 1):
                    yCoord += 59
            elif (i % 3 == 2):
                xCoord = 422
            else:
                xCoord = 557
            self.numberButton[i].place(x=xCoord, y=yCoord)
# ----------------------------- Square Buttons ---------------------------------------------------------------
        self.squareButton = []
        self.squareImage = tk.PhotoImage(file="images/dot.png")

        for i in range(0, 22):
            self.squareButton.append(tk.Button(image=self.squareImage, command=lambda n = i: self.placeSquareBet(n)))

        yCoord = 142
        for i in range(0, 22):
            if (i % 2 == 0):
                xCoord = 392
                if (i > 1):
                    yCoord += 60
            else:
                xCoord = 527
            self.squareButton[i].place(x=xCoord, y=yCoord)

# ----------------------------- Six Line Buttons ---------------------------------------------------------------
        self.sixLineButton = []
        self.sixLineImage = tk.PhotoImage(file="images/dot.png")

        for i in range(0, 11):
            self.sixLineButton.append(tk.Button(image=self.sixLineImage, command=lambda n=i: self.placeSixLineBet(n)))

        yCoord = 142
        xCoord = 261
        for i in range(0, 11):
            self.sixLineButton[i].place(x=xCoord, y=yCoord)
            yCoord += 60
# ----------------------------- Split Buttons ---------------------------------------------------------------
        self.splitButtonDir1 = []
        self.splitImageDir1 = tk.PhotoImage(file="images/blackline.png")

        for i in range(0, 36):
            self.splitButtonDir1.append(tk.Button(image=self.splitImageDir1, command=lambda n = i: self.placeSplitDir1Bet(n)))

        yCoord = 90
        for i in range(0, 36):
            if (i % 3 == 0): #left
                xCoord = 324
            elif(i % 3 == 1): #middle
                xCoord = 458
            else:             #right
                xCoord = 594

            self.splitButtonDir1[i].place(x=xCoord, y=yCoord)
            if(i % 3 == 2):
                yCoord += 59
        #Split Dir2-----------------------------
        self.splitButtonDir2 = []
        self.splitImageDir2 = tk.PhotoImage(file="images/blacklineVertical.png")

        for i in range(0, 24):
            self.splitButtonDir2.append(
                tk.Button(image=self.splitImageDir2, command=lambda n=i: self.placeSplitDir2Bet(n)))

        yCoord = 114
        for i in range(0, 24):
            if (i % 2 == 0):
                xCoord = 396
            else:
                xCoord = 530

            self.splitButtonDir2[i].place(x=xCoord, y=yCoord)
            if (i % 2 == 1):
                yCoord += 60

# ----------------------------- Street Buttons ---------------------------------------------------------------
        self.streetButton = []
        self.streetImage = tk.PhotoImage(file="images/blacklineVertical.png")

        for i in range(0, 12):
            self.streetButton.append(
                tk.Button(image=self.streetImage, command=lambda n=i: self.placeStreetBet(n)))

        yCoord = 114
        xCoord = 263
        for i in range(0, 12):
            self.streetButton[i].place(x=xCoord, y=yCoord)
            yCoord += 60

    def closeTableWindow(self):
        self.root.destroy()

    def amountToBet1(self):
        self.betAmount = 1
        self.oneDollarButton.configure(bg='yellow')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet5(self):
        self.betAmount = 5
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='yellow')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet10(self):
        self.betAmount = 10
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='yellow')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet20(self):
        self.betAmount = 20
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='yellow')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet25(self):
        self.betAmount = 25
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='yellow')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet50(self):
        self.betAmount = 50
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='yellow')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet70(self):
        self.betAmount = 70
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='yellow')
        self.hundredDollarButton.configure(bg='white')

    def amountToBet100(self):
        self.betAmount = 100
        self.oneDollarButton.configure(bg='white')
        self.fiveDollarButton.configure(bg='white')
        self.tenDollarButton.configure(bg='white')
        self.twentyDollarButton.configure(bg='white')
        self.twentyFiveDollarButton.configure(bg='white')
        self.fiftyDollarButton.configure(bg='white')
        self.seventyDollarButton.configure(bg='white')
        self.hundredDollarButton.configure(bg='yellow')

    def placeNumberBet(self, number):
        self.selectedNumbers.append((number, self.betAmount))
        if(number == 37):  #check for 00 aka 37
            self.doubleZeroButton.configure(bg='yellow')
        else:
            self.numberButton[number].configure(bg='yellow')

    def placeSquareBet(self, number):
        self.selectedSquares.append((number, self.betAmount))
        self.squareButton[number].configure(bg='yellow')

    def placeSixLineBet(self, number):
        self.selectedSixLine.append((number, self.betAmount))
        self.sixLineButton[number].configure(bg='yellow')

    def placeSplitDir1Bet(self, number):
        self.selectedSplitDir1.append((number, self.betAmount))
        self.splitButtonDir1[number].configure(bg='yellow')

    def placeSplitDir2Bet(self, number):
        self.selectedSplitDir2.append((number, self.betAmount))
        self.splitButtonDir2[number].configure(bg='yellow')

    def placeLowsHighsBet(self, option):
        if(option):
            self.lowsBet = (True, self.betAmount)
            self.oneTo18Button.configure(bg='yellow')
        else:
            self.highsBet = (True, self.betAmount)
            self.nineteenTo36Button.configure(bg='yellow')

    def placeEvenOddsBet(self, option):
        if(option):
            self.evensBet = (True, self.betAmount)
            self.evenButton.configure(bg='yellow')
        else:
            self.oddsBet = (True, self.betAmount)
            self.oddButton.configure(bg='yellow')

    def placeRedBlackBet(self, option):
        if(option):
            self.redBet = (True, self.betAmount)
            self.redButton.configure(bg='yellow')
        else:
            self.blackBet = (True, self.betAmount)
            self.blackButton.configure(bg='yellow')

    def placeDozenBet(self, number):
        self.selectedDozens.append((number, self.betAmount))
        self.dozenButton[number].configure(bg='yellow')

    def place2to1Bet(self, number):
        self.selected2to1.append((number, self.betAmount))
        self.twoToOneButton[number].configure(bg='yellow')

    def placeStreetBet(self, number):
        self.selectedStreet.append((number, self.betAmount))
        self.streetButton[number].configure(bg='yellow')

    def receiveSelectedNumbers(self):
        return self.selectedNumbers

    def receiveSquareSelections(self):
        return self.selectedSquares

    def receiveLowsSelection(self):
        return self.lowsBet

    def receiveHighsSelection(self):
        return self.highsBet

    def receiveEvensSelection(self):
        return self.evensBet

    def receiveOddsSelection(self):
        return self.oddsBet

    def receiveRedSelection(self):
        return self.redBet

    def receiveBlackSelection(self):
        return self.blackBet

    def receiveSelectedDozens(self):
        return self.selectedDozens

    def receiveSelected2to1(self):
        return self.selected2to1

    def receiveSelectedSplitDir1(self):
        return self.selectedSplitDir1

    def receiveSelectedSplitDir2(self):
        return self.selectedSplitDir2

    def receiveSelectedSixLine(self):
        return self.selectedSixLine

    def receiveSelectedStreet(self):
        return self.selectedStreet