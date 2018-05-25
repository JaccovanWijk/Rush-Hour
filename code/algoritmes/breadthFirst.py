from time import time
from collections import deque

import rushHour as r

class BreadthFirst(r.RushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board):

        r.RushHour.__init__(self,board)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

        self.openBoards = deque()
        self.closedBoards = set()
        self.winningBoard = ""
        self.solved = False
        self.count = 0


    def solver(self, all=False):
        """The breadth first search algorithm

        Returns solution, amount of moves and iterations"""
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
                self.winningBoard = self.currentBoard
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

        return (self.showMoves(self.winningBoard, self.moves), self.count, time() - beginTime)


    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []

        # get all moves of all vehicles
        for vehicle in self.currentVehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles,vehicle, i)
                self.makingMove(self.currentVehicles,vehicle, -i)

                sucessors.append(newBoard)

        return sucessors
