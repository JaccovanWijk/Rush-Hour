import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# import shit
import rushHour as r
import greedy as gr
import Astar as A
#import breadthFirst as br
import BruteForce as bf

def main():
    f = open("data/Boards/Game 1", "r")
    board = f.read()
    f.close()

    game = bf.bruteForce(board, 6)
    moves = game.solver()
    print(moves)

if __name__ == "__main__":
    main()
