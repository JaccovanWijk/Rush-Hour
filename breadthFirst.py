import rushHour as r
from collections import deque

class breadthFirst(r.rushHour):

    def __init__(self,board):

        r.rushHour.__init__(self,board)

    def getSucessors(self):

        sucessors = []
        cars = self.vehicles

        # get all moves of all vehicles
        for vehicle in self.vehicles:

            for i in self.searchMoves(vehicle):

                newBoard = self.makingMove(vehicle, i)
                move = vehicle.name + str(i)
                self.makingMove(vehicle, -i)
                sucessors.append([newBoard, move])

        return sucessors

    def breadthFirstSearch(self):

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
                if not newBoard in openBoards:

                    # add move to moves
                    moves[newBoard] = (self.initBoard, move)
                    openBoards.append([newBoard, self.getVehicles(newBoard)])

            # finish processing current board
            closedBoards.add(self.initBoard)


    def showMoves(self, board, moves):

        moveList = list()

        while True:

            row = moves[board]
            if len(row) == 2:
                board = row[0]
                move = row[1]
                # add move to begin of list
                moveList.append(move)
            else:
                break

        moveList.reverse()
        return moveList