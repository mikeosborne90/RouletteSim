import gameLogic as gL
import player as ply

player1 = ply.player(100)
#Example betting $100
myGame = gL.gameLogic(player1)
#Example betting on row 1
myGame.chooseRowBet(1, 50)
#Example betting on column 1
myGame.chooseColumnBet(1, 50)
myGame.showNumbersChosen()
myGame.didIWin()
print("Total Money:", myGame.getTotalMoney())