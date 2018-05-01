import rushHour as r
import BruteForce as bf
import numpy as np

class BranchBound(r.RushHour):

    def __init__(self,board,size):

        r.RushHour.__init__(self, board, size)
        self.currentBoard = self.initBoard
        self.boardHistory = [self.initBoard]
        self.vehiclesHistory = [self.vehicles]
        self.moves = []
        self.moveCount = []

    def solve(self):

        # find upperbound by random solver
        upperBound = self.RandomSolve(self.currentBoard)

        while not self.won(self.currentVehicles):

            # search all possible moves on current board
            possibleMoves = []
            for vehicle in self.vehiclesHistory[-1]:
                possibleMoves.append(self.searchMoves(self.currentBoard, vehicle))

            self.moves.append(possibleMoves)

            for list in self.moves:
                for move in list:
                    self.currentBoard = self.makingMove()

    def RandomSolve(self, board):

        # bruteForce 10 times
        moves = 0
        for j in range(10):
            game = bf.BruteForce(board, self.size)
            moves += game.solver()
        return int(moves/10)

    def branchBoundSolve(self):

        # find upperbound by random solver
        upperBound = self.RandomSolve(self.currentBoard)

        # open possibilities
        openBoards = []
        # closed possibilities
        closedBoards = set()
        # moves done
        moves = dict()

        # initialise search
        openBoards.append(self.currentBoard)
        moves[self.currentBoard] = ()

        while openBoards:

            self.currentBoard = openBoards.pop()

            # if current branch is too big
            if np.sum(self.moveCount) > upperBound:
                moveCount.pop()
                continue

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                return self.showMoves(self.currentBoard, moves)

            for (newBoard, move) in self.getSucessors():

                # board is already processed
                if newBoard in closedBoards:
                    continue

                # if board isn't already in queue
                if not newBoard in openBoards:

                    # add move to moves
                    moves[newBoard] = (self.currentBoard, move)

                    # add new board state to open boards
                    openBoards.append(newBoard)

            # finish processing current board
            closedBoards.add(self.currentBoard)

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

                self.moveCount.append(i)

        return sucessors
