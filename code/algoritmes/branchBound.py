import rushHour as r
import BruteForce as bf
import time
import random
import math
import visualizer as v
# import Queue

class BranchBound(r.RushHour):

    def __init__(self,board):

        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.endState = ""
        self.currentVehicles = self.vehicles
        self.closedBoards = set()
        self.finalClosedBoards = set()
        self.openBoards = []
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
            timez = time.time()
            self.solver(self.currentBoard, 0)
            self.done = False
            print("time", i, "=", time.time() - timez)
            timez = time.time()

        print("time: ",time.time() - start_time)
        return self.upperBound

    def solver(self, board, moves):
        # check limit
        if moves >= self.upperBound or (board, moves) in self.closedBoards or self.done or self.iterations == self.amount:
            return

        self.currentVehicles = self.getVehicles(board)

        # if won, set new upperlimit
        if self.won(self.currentVehicles):
            self.upperBound = moves
            self.iterations += 1
            self.done = True
            print("New upperbound =", moves)
            return

        # add current board to queue
        self.openBoards.append((board, moves))

        # self.currentBoard = board
        for newBoard in self.sortedSucessors(board):

            # request recursive solve
            if (newBoard, moves + 1) not in self.closedBoards:
                self.solver(newBoard, moves + 1)

        if not self.done:
            self.closedBoards.add(self.openBoards.pop())


    def sortedSucessors(self, board):
        """Sort list of boards"""
        sucessors = self.getSucessors(board)
        sort = []
        sortedSucessors = []

        for board in sucessors:
            sort.append((self.heuristic(board), board))
        sort = sorted(sort, key=lambda score: score[0])

        for (score, board) in sort:
            sortedSucessors.append(board)

        return sortedSucessors

    def getSucessors(self, board):
        """Get next board states reachable by making one move"""
        sucessors = []
        vehicles = self.getVehicles(board)

        # get all moves of all vehicles
        for vehicle in vehicles:
            for i in self.searchMoves(board, vehicle):
                # determine new state
                newBoard = self.makingMove(vehicles, vehicle, i)
                self.makingMove(vehicles,vehicle, -i)

                sucessors.append(newBoard)

        return sucessors

    def RandomSolve(self, board):

        # bruteForce 10 times
        movemin = 100000
        for j in range(10):
            game = bf.BruteForce(board)
            amount, move, self.endState = game.solver(True)
            if move < movemin:
                movemin = move
        return movemin

    def heuristic (self, board):

        score = 0
        score += self.heuristic1(board) + self.heuristic2(board)
        return score

    def heuristic1 (self, board):
        """Afstand van punten naar uitgang"""

        score = 0
        for i in range(self.size*self.size):
            if board[i] == ".":
                # add x difference
                score += self.size - i % self.size
                # add y difference
                score += abs(1 - i // self.size)
        return score

    def heuristic2 (self, board):

        score = 0

        goalVehicles = self.getVehicles(self.endState)
        vehicles = self.getVehicles(board)

        for vehicle in vehicles:
            for goalVehicle in goalVehicles:
                if vehicle.name == goalVehicle.name:
                    score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
        # for vehicle in vehicles:
        #      for goalVehicle in goalVehicles:
        #
        #          if vehicle.name == goalVehicle.name:
        #              score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
        #
        # scores.append((score, (board, i)))
        return score
