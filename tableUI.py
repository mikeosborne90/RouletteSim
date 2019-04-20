import tkinter as tk

class tableUI:
    def __init__(self):
        self.selectedNumbers = list([])
        self.selectedSquares = list([]
                                    )
        self.root = tk.Tk()
        self.root.title('CSCI 154 Roulette Simulator')
        self.root.resizable(0, 0)  # Makes image non-resizable
        self.root.overrideredirect(True) # disable close window button

        self.image = tk.PhotoImage(file="images/euroBoard.png")
        self.label = tk.Label(image=self.image)
        self.label.pack()

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
        self.squareImage = tk.PhotoImage(file="images/037.png")

        for i in range(0, 22):
            self.squareButton.append(tk.Button(image=self.squareImage, command=lambda n = i: self.placeSquareBet(n)))

        yCoord = 138
        for i in range(0, 22):
            if (i % 2 == 0):
                xCoord = 386
                if (i > 1):
                    yCoord += 59
            else:
                xCoord = 520
            self.squareButton[i].place(x=xCoord, y=yCoord)



    def closeTableWindow(self):
        self.root.destroy()

    def placeNumberBet(self, number):
        self.selectedNumbers.append(number)
        self.numberButton[number].configure(bg='yellow')

    def placeSquareBet(self, number):
        self.selectedSquares.append(number)
        self.squareButton[number].configure(bg='yellow')

    def receiveSelectedNumbers(self):
        return self.selectedNumbers

    def receiveSquareSelections(self):
        return self.selectedSquares

    # For Reference Only
    # Board GUI ---------------------------------------------------------------------------
    # root = tk.Tk()
    # root.title('CSCI 154 Roulette Simulator')
    # root.resizable(0,0) # Makes image non-resizable
    #
    # image = tk.PhotoImage(file="images/euroBoard.png")
    # label = tk.Label(image=image)
    # label.pack()
    #
    # numberButton = []
    # numberImage = []
    # for i in range(0, 37):
    #     numberImage.append(tk.PhotoImage(file = "images/" + str(i) + ".png"))
    #     numberButton.append(tk.Button(image = numberImage[i]))
    #
    # numberButton[0].place(x = 395, y = 38)
    #
    # yCoord = 102
    # for i in range(1,37):
    #     if(i % 3 == 1):
    #         xCoord = 288
    #         if(i > 1):
    #             yCoord +=59
    #     elif(i % 3 == 2):
    #         xCoord = 422
    #     else:
    #         xCoord = 557
    #     numberButton[i].place( x = xCoord, y = yCoord)

    # oneDollar = tk.Button(root, text = '$1', fg ='black')
    # oneDollar.place(x = 25, y =200)
    #
    # fiveDollar = tk.Button(root, text = '$5', fg ='black')
    # fiveDollar.place(x = 25, y =300)
    #
    # tenDollar = tk.Button(root, text = '$10', fg ='black')
    # tenDollar.place(x = 25, y =400)
    #
    # twentyDollar = tk.Button(root, text = '$20', fg ='black')
    # twentyDollar.place(x = 25, y =500)
    #
    # fiftyDollar = tk.Button(root, text = '$50', fg ='black')
    # fiftyDollar.place(x = 25, y =600)
    #
    # hundredDollar = tk.Button(root, text = '$100', fg ='black')
    # hundredDollar.place(x = 10, y =700)
    #
    # redbutton = tk.Button(root, text = 'Red', fg ='red')
    # redbutton.place(x = 110, y =360)

    # root.mainloop()

    # End of Board GUI ------------------------------------------------------------------