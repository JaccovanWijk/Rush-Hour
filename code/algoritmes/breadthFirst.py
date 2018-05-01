import rushHour as r
import queue
from collections import deque

class breadthFirst(r.RushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board,size):

        r.RushHour.__init__(self,board,size)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

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

    def breadthFirstSearch(self):
        """The breadth first search algorithm"""

        # open possibilities
        openBoards = []
        # closed possibilities
        closedBoards = set()
        # moves done
        moves = dict()
        # iteration counter
        count = 0

        # initialise search
        openBoards.insert(0, self.currentBoard)
        moves[self.currentBoard] = ()

        while openBoards:

            self.currentBoard = openBoards.pop()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                return (self.showMoves(self.currentBoard, moves), count)

            count += 1

            for (newBoard, move) in self.getSucessors():

                # board is already processed
                if newBoard in closedBoards:
                    continue

                # if board isn't already in queue
                if not newBoard in openBoards:

                    # add move to moves
                    moves[newBoard] = (self.currentBoard, move)

                    # add new board state to open boards
                    openBoards.insert(0, newBoard)

            # finish processing current board
            closedBoards.add(self.currentBoard)
