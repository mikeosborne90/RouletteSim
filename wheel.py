import random

class wheel:
    def __init__(self):
        self.selectedNumber = 0

    def spinWheelEuropean(self):
        self.selectedNumber = random.randint(0, 36)
        return self.selectedNumber

    def spinWheelAmerican(self):
        self.selectedNumber = random.randint(0, 37)
        return self.selectedNumber

    def spinWheelNoZeroes(self):
        self.selectedNumber = random.randint(1, 36)
        return self.selectedNumber