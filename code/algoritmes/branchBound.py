import rushHour as r
import BruteForce as bf
import time
import random
import math

class BranchBound(r.RushHour):

    def __init__(self,board):

        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.goalBoard = ""
        self.currentVehicles = self.vehicles
        self.closedBoards = set()
        self.finalClosedBoards = set()
        self.openBoards = []
        self.tempOpenBoards = []
        self.upperBound = 0
        self.amount = 0
        self.iterations = 0
        self.done = False


    def branchBoundSolve(self, amount):
        start_time = time.time()
        # find upperbound by random solver
        self.upperBound = self.RandomSolve(self.currentBoard)
        self.upperBound = 35
        print("Random upperbound =", self.upperBound)

        self.amount = amount

        for i in range(amount):
            self.solver(self.currentBoard, 0)
            self.done = False

        print("time: ",time.time() - start_time)
        return self.upperBound

    def solver(self, board, moves):
        # check limit
        if moves >= self.upperBound or (board, moves) in self.closedBoards or self.done or self.iterations == self.amount:
            return

        # if won, set new upperlimit
        if self.won(self.getVehicles(board)):
            self.upperBound = moves
            self.iterations += 1
            self.openBoards = self.tempOpenBoards
            self.done = True
            print("New upperbound =", moves)
            return

        # add current board to stack
        #self.closedBoards.add((board, moves))
        self.tempOpenBoards.append((board, moves))

        # self.currentBoard = board
        for (j, (newBoard, move)) in self.getSucessors(board):

            # request recursive solve
            if (newBoard, moves + 1) not in self.closedBoards:
                self.solver(newBoard, moves + 1)

        if not self.done:
            self.closedBoards.add(self.tempOpenBoards.pop())

    def getSucessors(self, board):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.getVehicles(board)

        # get all moves of all vehicles
        for vehicle in cars:
            for i in self.searchMoves(board, vehicle):
                # determine new state
                newBoard = self.makingMove(cars,vehicle, i)
                self.makingMove(cars,vehicle, -i)

                sucessors.append([newBoard, i])

        #random.shuffle(sucessors)
        return self.heuristic2(sucessors)

    def RandomSolve(self, board):

        # bruteForce 10 times
        movemin = 100000
        for j in range(10):
            game = bf.BruteForce(board)
            amount, move = game.solver()
            if move < movemin:
                movemin = move
                self.goalBoard = board
        return movemin

    def heuristic (self, boards):

        goalVehicles = self.getVehicles(self.goalBoard)
        scores = []

        for (board, i) in boards:

            score = 0
            vehicles = self.getVehicles(board)
            for vehicle in vehicles:
                 for goalVehicle in goalVehicles:

                     if vehicle.name == goalVehicle.name:
                         score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())

            scores.append((score, (board, i)))

        return sorted(scores, key=lambda score: score[0])

    def heuristic2 (self, boards):
        """Afstand van punten naar uitgang"""

        scores = []
        for (board, i) in boards:

            score = 0
            for j in range(self.size*self.size):
                if board[j] == ".":

                    # add x difference
                    score += self.size - j % self.size
                    # add y difference
                    score += abs(1 - j // self.size)

            scores.append((score, (board, i)))

        return sorted(scores, key=lambda score: score[0])
