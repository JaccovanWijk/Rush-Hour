import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# import shit
import rushHour as r
import greedy as gr
import Astar as A
import breadthFirst as br
import BruteForce as bf

f = open("data/Boards/Game 3", "r")
board = f.read()
f.close()

game = bf.bruteForce(board, 6)
print(game.solver())
game.showBoard()
