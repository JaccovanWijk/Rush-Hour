import rushHour as r
import breadthFirst as br

f = open("Boards/Test", "r")
board = f.read()
f.close()

game = r.rushHour(board)

print(game.initBoard)

for vehicle in game.vehicles:
    if vehicle.name == "P":
        car = vehicle
game.makingMove(car, -1)

print(game.makingMove(car, -1))
