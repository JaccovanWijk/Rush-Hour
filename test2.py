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

moves = 0
for j in range(10):
    game = bf.bruteForce(board, 6)
    moves += game.solver(True)
    print(moves)

print(moves/10)
#print(moves1/100 , moves2/100)

# eerste resultaat voor 100 keer 6bij6 Game1(gemiddeld over 100): 17829.65 zonder restrictie tegen 13447.42 met restrictie van rode auto
# tweede resultaat voor 100 keer 6bij6 Game1(gemiddeld over 100): 8403.63 met extra restrictie
# derde resultaat voor 1000 keer 6bij6 Game1(gemiddeld over 1000): 9110.797

# eerste resultaat voor 1000 keer 6bij6 Game2(gemiddeld over 1000): 812.689

# eerste resultaat voor 1 keer 12bij12: met restricties 20565 zetten
