import tkinter as tk

class tableUI:
    def __init__(self):
        self.betAmount = 1  # set to $1 as default
        self.selectedNumbers = list([])
        self.selectedSquares = list([])

        self.root = tk.Tk()
        self.root.title('CSCI 154 Roulette Simulator')
        self.root.resizable(0, 0)  # Makes image non-resizable
        self.root.overrideredirect(True) # disable close window button

        self.image = tk.PhotoImage(file="images/euroBoard.png")
        self.label = tk.Label(image=self.image)
        self.label.pack()

        self.oneDollarButton = tk.Button(text = '$1', fg ='black', command=lambda n = 1: self.amountToBet(n))
        self.oneDollarButton.place(x = 30, y =100)

        self.fiveDollarButton = tk.Button(text = '$5', fg ='black', command=lambda n = 5: self.amountToBet(n))
        self.fiveDollarButton.place(x = 30, y =150)

        self.tenDollarButton = tk.Button(text = '$10', fg ='black', command=lambda n = 10: self.amountToBet(n))
        self.tenDollarButton.place(x = 28, y =200)

        self.twentyDollarButton = tk.Button(text = '$20', fg ='black', command=lambda n = 20: self.amountToBet(n))
        self.twentyDollarButton.place(x = 28, y =250)

        self.fiftyDollarButton = tk.Button(text = '$50', fg ='black', command=lambda n = 50: self.amountToBet(n))
        self.fiftyDollarButton.place(x = 28, y =300)

        self.hundredDollarButton = tk.Button(text = '$100', fg ='black', command=lambda n = 100: self.amountToBet(n))
        self.hundredDollarButton.place(x = 25, y =350)

        self.numberButton = []
        self.numberImage = []
        for i in range(0, 37):
            self.numberImage.append(tk.PhotoImage(file="images/" + str(i) + ".png"))
            self.numberButton.append(tk.Button(image=self.numberImage[i], command=lambda n = i: self.placeNumberBet(n)))

        self.numberButton[0].place(x=395, y=38)

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



    def closeTableWindow(self):
        self.root.destroy()

    def amountToBet(self, amount):
        self.betAmount = amount

    def amountFiveDollar(self):
        self.betAmount = 5

    def placeNumberBet(self, number):
        self.selectedNumbers.append((number, self.betAmount))
        self.numberButton[number].configure(bg='yellow')

    def placeSquareBet(self, number):
        self.selectedSquares.append((number, self.betAmount))
        self.squareButton[number].configure(bg='yellow')

    def receiveSelectedNumbers(self):
        return self.selectedNumbers

    def receiveSquareSelections(self):
        return self.selectedSquares