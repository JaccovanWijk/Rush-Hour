import rushHour as r
from collections import deque

class breadthFirst(r.rushHour):
    """A breadth first search algorithm for Rush Hour"""

    def __init__(self,board):

        r.rushHour.__init__(self,board)

    def sortMoves(self, directions):
        return sorted(directions, key=abs, reverse=True)

    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.vehicles

        # get all moves of all vehicles
        for vehicle in self.vehicles:

            for i in self.sortMoves(self.searchMoves(vehicle)):

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
        openBoards = deque()
        # closed possibilities
        closedBoards = set()
        # moves done
        moves = dict()

        # initialise search
        openBoards.append([self.initBoard, self.vehicles])
        moves[self.initBoard] = ()

        while openBoards:

            (self.initBoard, self.vehicles) = openBoards.popleft()

            # stop if puzzle is solved
            if self.won():
                return self.showMoves(self.initBoard, moves)

            for (newBoard, move) in self.getSucessors():

                # board is already processed
                if newBoard in closedBoards:
                    continue

                # if board isn't already in queue
                if newBoard not in openBoards:

                    # add move to moves
                    moves[newBoard] = (self.initBoard, move)

                    # add new board state to open boards
                    openBoards.append([newBoard, self.getVehicles(newBoard)])

            # finish processing current board
            closedBoards.add(self.initBoard)
