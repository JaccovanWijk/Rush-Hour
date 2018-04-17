import rushHour as r

f = open("Boards/Game 1", "r")
board = f.read()
f.close()

game = r.rushHour(board)

print(game.initBoard)
game.makingMove("P",1)
print(game.initBoard)