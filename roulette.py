import random

table = [[3,6,9,12,15,18,21,24,27,30,33,36],
		 [2,5,8,11,14,17,20,23,26,29,32,35],
		 [1,4,7,10,13,16,19,22,25,28,31,34]]

#0 = red, 1 = black
colors = [[0,1,0,0,1,0,0,1,0,0,1,0],
		  [1,0,1,1,0,1,1,0,1,1,0,1],
		  [0,1,0,1,1,0,0,1,0,1,1,0]]

#0 for Euro, 0 and 00 for American
greensEuro =[0]
greensAmer =[0, 37]

#example bet: ([3,6,9,12,15,18,21,24,27,30,33,36],2,20.00)
bets = []
money = 100.00

def printTable():
	print(table[0])
	print(table[1])
	print(table[2])

def spinWheel():
	selectedNumber = random.randint(0,36)
	return selectedNumber
	
def betRow(betAmt, rowNum):
	global bets
	myBet = (table[rowNum-1],2,betAmt)
	bets.append(myBet)
	
def didIWin(numberChosen):
	win = False
	
	for i in bets:
		if numberChosen in i[0]:
			win = True
	return win

selectedNumber = spinWheel()
	
betRow(20.00,1)
print("Landed on", selectedNumber)
print("Did I win?", didIWin(selectedNumber))