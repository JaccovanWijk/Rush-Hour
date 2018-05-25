"""
branchBound.py: Implements a branch and bound algorithm.

This module implements a branch and bound algorithm with
heuristics to lower the computation time.
"""

import rushHour as r
import RandomSolver as rs
from time import time
import random
import math
import visualizer as v

class BranchBound(r.RushHour):
    """
    The branch and bound model for its algorithm.

    Attributes:
    currentBoard    -- string representation of board
    currentVehicles -- vehicles of current board
    endState        -- end state of a random solution
    openBoards      -- boards in processing
    closedBoards    -- boards already processed
    upperBound      -- current best upper bound
    upperBounds     -- all improved upper bound steps
    amount          -- amount of improvements on the upper bound requested
    iterations      -- amount of improvements on the upper bound done
    heuristics      -- list of heuristics used for this run of branch and bound"""

    def __init__(self,board):
        """
        Initialise model for branch and bound.

        Arguments:
        board -- representation of a rush hour board
        """
        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.endState = ""
        self.currentVehicles = self.vehicles
        self.closedBoards = set()
        self.openBoards = []
        self.upperBound = 0
        self.upperBounds = []
        self.amount = 0
        self.iterations = 0
        self.done = False
        self.heuristics = []

    def solver(self, amount, heuristics):
        """The branch and bound search algorithm.

        Arguments:
        amount      -- amount of improvements on the upper bound
        heuristics: -- list of heuristics used

        Returns least upperbound, improvements and computation time.
        """
        self.heuristics = heuristics

        start_time = time()
        # find upperbound by random solver
        self.upperBound = self.RandomSolve(self.currentBoard)
        self.upperBounds.append(self.upperBound)
        print("First upperbound =",self.upperBound)

        self.amount = amount

        for i in range(amount):
            # timez = time()
            self.branchBoundSolve(self.currentBoard, 0)
            self.done = False
            # print("time", i, "=", time() - timez)
            # timez = time()

        return self.upperBound, self.upperBounds, time() - start_time

    def branchBoundSolve(self, board, moves):
        """Recursive branch and bound solver."""
        # check limit
        if moves >= self.upperBound or (board, moves) in self.closedBoards or self.done or self.iterations == self.amount:
            return

        self.currentVehicles = self.getVehicles(board)

        # if won, set new upperlimit
        if self.won(self.currentVehicles):
            self.upperBound = moves
            self.upperBounds.append(self.upperBound)
            self.iterations += 1
            self.done = True
            print("New upperbound =", moves)
            return

        # add current board to queue
        self.openBoards.append((board, moves))

        for newBoard in self.sortedSucessors(board):

            # request recursive solve
            if (newBoard, moves + 1) not in self.closedBoards:
                self.branchBoundSolve(newBoard, moves + 1)

        if not self.done:
            self.closedBoards.add(self.openBoards.pop())


    def sortedSucessors(self, board):
        """Sort list of boards."""
        sucessors = self.getSucessors(board)
        sort = []
        sortedSucessors = []

        for board in sucessors:
            sort.append((self.heuristic(board), board))
        #sort = sorted(sort, key=lambda score: score[0])

        return [item[1] for item in sorted(sort, key=lambda score: score[0])]

    def RandomSolve(self, board):
        """Solve board randomly ten times.

        Arguments:
            board -- board to solve

        Returns minimum amount of moves of solutions
        """
        # bruteForce 10 times
        movemin = 100000
        for j in range(10):
            game = rs.RandomSolve(board)
            amount, move, self.endState = game.solver()
            if move < movemin:
                movemin = move
        return movemin

    def heuristic(self, board):
        """Return estimated amount of moves from board to solution."""
        score = 0
        for heuristic in self.heuristics:
            if heuristic == "heuristic1":
                score += self.heuristic1(board)
            if heuristic == "heuristic2":
                score += self.heuristic2(board, self.endState)
            if heuristic == "heuristic3":
                score += self.heuristic3(board)

        return score
