"""
breadthFirst.py: An implementation of a breadth first search algorithm.

This implementation uses a breadth frst search algorithm to
solve a rush hour puzzle.
"""
from time import time
from collections import deque

import rushHour as r

class BreadthFirst(r.RushHour):
    """
    A breadth first search algorithm for Rush Hour.

    Attributes:
        currentBoard    -- string representation of board
        currentVehicles -- vehicles of current boards
        openBoards      -- boards in processing
        closedBoards    -- boards already processed
        solved          -- indicates if puzzle is solved
        count           -- amount of iterations
    """

    def __init__(self,board):
        """
        Initialise model.

        Arguments:
            board -- Representation of a rush hour board
        """
        r.RushHour.__init__(self,board)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

        self.openBoards = deque()
        self.closedBoards = set()
        self.solved = False
        self.count = 0


    def solver(self, all=False):
        """
        The breadth first search algorithm.

        Arguments:
            all (bool): Find all reachable states. Defaults to False.

        Returns:

        Returns solution, amount of moves and iterations
        """
        returnVals = []
        beginTime = time()

        # initialise search
        self.openBoards.append(self.currentBoard)
        self.moves[self.currentBoard] = ()

        while self.openBoards:

            self.currentBoard = self.openBoards.popleft()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles) and not self.solved:
                returnVals.append(self.showMoves(self.currentBoard,self.moves))
                self.solved = True

                if not all:
                    break;

            self.count += 1

            for newBoard in self.getSucessors():

                # board is already processed
                if newBoard in self.closedBoards:
                    continue

                # if board isn't already in queue
                if not newBoard in self.openBoards:

                    # add move to moves
                    self.moves[newBoard] = self.currentBoard

                    # add new board state to open boards
                    self.openBoards.append(newBoard)

            # finish processing current board
            self.closedBoards.add(self.currentBoard)

        returnVals.append(self.count)
        returnVals.append(time() - beginTime)

        return self.showMoves(self.winningBoard, self.moves), self.count, time() - beginTime
