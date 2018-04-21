import rushHour as r
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

                newBoard = self.makingMove(vehicle, i)
                move = vehicle.name + ' ' + str(i)
                self.makingMove(vehicle, -i)
                sucessors.append([newBoard, move])

        return sucessors

    def breadthFirstSearch(self):
        """The breadth first search algorithm"""

        # open possibilities
        openBoards = deque()
        # closed possibilities
        closedBoards = set()
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
                if not newBoard in openBoards:

                    moves[newBoard] = (self.initBoard, move)
                    # add new board state to open boards
                    openBoards.append([newBoard, self.getVehicles(newBoard)])

            # finish processing current board
            closedBoards.add(self.initBoard)
            
    def showMoves(self, endState, moves):
        """Makes a list of moves made to solve the puzzle"""

        moveList = list()

        while True:
            # go back one move
            row = moves[endState]
            if len(row) == 2:
                endState = row[0]
                move = row[1]

                # add move to begin of list
                moveList.append(move)
            else:
                break

        moveList.reverse()
        return moveList