import rushHour as r
import queue
from time import time
from collections import deque

class breadthFirst(r.RushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board):

        r.RushHour.__init__(self,board)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

        self.openBoards = []
        self.closedBoards = set()
        self.count = 0

    def breadthFirstSearch(self):
        """The breadth first search algorithm

        Returns solution, amount of moves and iterations"""

        beginTime = time()

        # initialise search
        self.openBoards.insert(0, self.currentBoard)
        self.moves[self.currentBoard] = ()

        while self.openBoards:

            self.currentBoard = self.openBoards.pop()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                return (self.showMoves(self.currentBoard, self.moves), self.count, time() - beginTime)

            self.count += 1

            for (newBoard, move) in self.getSucessors():

                # board is already processed
                if newBoard in self.closedBoards:
                    continue

                # if board isn't already in queue
                if not newBoard in self.openBoards:

                    # add move to moves
                    self.moves[newBoard] = (self.currentBoard, move)

                    # add new board state to open boards
                    self.openBoards.insert(0, newBoard)

            # finish processing current board
            self.closedBoards.add(self.currentBoard)

    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.currentVehicles

        # get all moves of all vehicles
        for vehicle in self.currentVehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles,vehicle, i)
                self.makingMove(self.currentVehicles,vehicle, -i)
                # make move string
                move = vehicle.name + ' ' + str(i)

                sucessors.append([newBoard, move])

        return sucessors
