import gameLogic as gL
import player as ply

player1 = ply.player(100)
#Example betting $100
myGame = gL.gameLogic(player1)
# #Example betting on row 1
# myGame.chooseRowBet(1, 30)
# #Example betting on column 1
# myGame.chooseColumnBet(1, 30)
# #Example betting on number 0
# myGame.chooseSingleBet(0, 10)
# #Example betting on odds
# myGame.chooseOddsBet(20)
#Example betting on blacks
myGame.chooseBlacksBet(10)
myGame.showNumbersChosen()
myGame.didIWin()
print("Total Money:", myGame.getTotalMoney())