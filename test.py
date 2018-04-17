import rushHour as r
import breadthFirst as br

f = open("Boards/Game 1", "r")
board = f.read()
f.close()

game = r.rushHour(board)

print(game.initBoard)

for vehicle in game.vehicles:
    if vehicle.name == "P":
        game.makingMove(vehicle,1)
print(game.initBoard)

game = br.breadthFirst(board)

moves = game.breadthFirstSearch()
print(moves)