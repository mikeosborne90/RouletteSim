import gameLogic

#Example betting $100
myGame = gameLogic.gameLogic(100)
#Example betting on row 1
myGame.chooseRowBet(1)
#Example betting on column 1
myGame.chooseColumnBet(1)
myGame.showNumbersChosen()
myGame.didIWin()