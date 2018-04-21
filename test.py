import rushHour as r
import breadthFirst as br

f = open("Boards/Game 1", "r")
board = f.read()
f.close()

game = br.breadthFirst(board)

moves = game.breadthFirstSearch()
print(moves)