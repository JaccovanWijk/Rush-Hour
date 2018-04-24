import rushHour as r
import breadthFirst as br
import greedy as gr

f = open("Boards/Test", "r")
board = f.read()
f.close()

game = gr.greedy(board)
game.greedysolve()

print(game.board)

for vehicle in game.vehicles:
    if vehicle.name == "P":
        car = vehicle
game.makingMove(car, -1)

print(game.board)
