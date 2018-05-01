import rushHour as r
import queue
from collections import deque

class breadthFirst(r.rushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board):

        r.rushHour.__init__(self,board)

    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.vehicles

        # get all moves of all vehicles
        for vehicle in self.vehicles:
            for i in self.searchMoves(vehicle):
                # determine new state
                newBoard = self.makingMove(vehicle, i)
                self.makingMove(vehicle, -i)
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

        count = 0

        # initialise search
        openBoards.insert(0 ,self.initBoard)
        moves[self.initBoard] = ()

        while openBoards:

            self.initBoard = openBoards.pop()

            # update cars
            self.vehicles = self.getVehicles(self.initBoard)

            # stop if puzzle is solved
            count += 1
            if self.won():
                return [self.showMoves(self.initBoard, moves), count]
            current_generation = []
            for (newBoard, move) in self.getSucessors():

                cars = self.getVehicles(newBoard)

                # board is already processed
                if newBoard in closedBoards:
                    continue

                # if board isn't already in queue
                if not newBoard in openBoards:

                    # add move to moves
                    moves[newBoard] = (self.initBoard, move)

                    # add new board state to open boards
                    openBoards.insert(0, newBoard)
                    current_generation.append(newBoard)

            # finish processing current board
            closedBoards.add(self.initBoard)
