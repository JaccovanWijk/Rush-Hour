import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# import shit
from vehicle import vehicle # moet dit?
from rushHour import rushHour as r
from greedy import greedy as gr
from Astar import aStar as A
from breadthFirst import BreadthFirst as br

def main():
    f = open("data/Boards/Test", "r")
    board = f.read()
    f.close()

    game = gr.greedy(board)
    gr.greedysolve()

if __name__ == "__main__":
    main()
