import random

class wheel:
    def __init__(self):
        self.selectedNumber = 0

    def spinWheel(self):
        self.selectedNumber = random.randint(0, 36)
        return self.selectedNumber