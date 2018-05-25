"""
Astar.py: An implementation of an A* algorithm.

This module implements an A* algorithm with different
heuristics, which are defined in the module 'rushHour.py'.
"""
import rushHour as r
import RandomSolver as rs
import queue as Qu

class AStar(r.RushHour):
    """The A* model used by the corresponding algorithm."""

    def __init__(self, board):
        """Initialise model for A*."""
        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.closedBoards = set()
        self.openBoards = []
        self.priorityQueue = Qu.PriorityQueue()
        self.moves = dict()
        self.Gcost = {}
        game = rs.RandomSolve(self.currentBoard)
        self.endState = game.solver()[-1]
        self.heuristics = []


    def solver(self, heuristics):
        """
        The A* search algorithm.

        Arguments:
        heuristics -- a list of heuristics used by A*

        Returns:
        amount of moves needed to solve the puzzle
        """
        # set heuristics
        self.heuristics = heuristics

        # initialise search
        self.priorityQueue.put((0, self.currentBoard))
        self.openBoards.append(self.currentBoard)
        self.moves[self.currentBoard] = ()

        # cost of steps from initial to last board
        self.Gcost[self.currentBoard] = 0

        while not self.priorityQueue.empty():

            # update constants
            self.currentBoard = self.priorityQueue.get()[1]
            self.openBoards.remove(self.currentBoard)

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                print("won:", self.currentBoard)
                break

            for newBoard in self.getSucessors(self.currentBoard):

                # board is already processed
                if newBoard in self.closedBoards:
                    continue

                #if board isn't already in priority queue
                if not newBoard in self.openBoards:

                    # add move to moves
                    self.moves[newBoard] = self.currentBoard

                    # add new board state to open boards
                    self.openBoards.append(newBoard)

                    #calculate the current depth and new G_cost
                    cost = self.Gcost[self.currentBoard] + 1
                    self.Gcost[newBoard] = (cost)

                    #update the queue through the cost and heuristic
                    score = cost + self.heuristic(newBoard)
                    self.priorityQueue.put((score, newBoard))

            # finish processing current board
            self.closedBoards.add(self.currentBoard)

        return len(self.showMoves(self.currentBoard, self.moves))

    def heuristic(self, board):
        """Return estimated amount of moves to solution."""
        score = 0
        for heuristic in self.heuristics:
            if heuristic == "heuristic1":
                score += self.heuristic1(board)
            if heuristic == "heuristic2":
                score += self.heuristic2(board, self.endState)
            if heuristic == "heuristic3":
                score += self.heuristic3(board)

        return score
