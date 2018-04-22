import rushHour as r
import breadthFirst as br

f = open("Boards/Test", "r")
board = f.read()
f.close()


game = br.breadthFirst(board)

moves = game.breadthFirstSearch()
print(moves)
