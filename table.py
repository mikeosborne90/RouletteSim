class table:
    def __init__(self):
        self.numbers = \
                [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
                 [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                 [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]

        self.greensEuro = [0]
        self.greensAmer = [0, 37]

        self.colors = \
           [[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]]

    def printTable(self):
        print(self.numbers[0])
        print(self.numbers[1])
        print(self.numbers[2])