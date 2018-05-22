import queue
from time import time
from collections import deque

import rushHour as r
import visualizer as v

class BreadthFirst(r.RushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board):

        r.RushHour.__init__(self,board)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

        self.openBoards = []
        self.closedBoards = set()
        self.count = 0

        self.visualizer = v.readBoard(self.currentVehicles)

    def breadthFirstSearch(self, all=False):
        """The breadth first search algorithm

        Returns solution, amount of moves and iterations"""

        beginTime = time()

        # initialise search
        self.openBoards.insert(0, self.currentBoard)
        self.moves[self.currentBoard] = ()

        name = "BreadthFirst0"
        v.drawBoard(self.vehicles, self.size, self.visualizer, name)
        i = 0

        while self.openBoards:

            self.currentBoard = self.openBoards.pop()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            name = "BreadthFirst" + str(self.count) + "-" + str(i)
            v.drawBoard(self.currentVehicles, self.size, self.visualizer, name)
            i += 1

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                if not all:
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

        return self.count

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
