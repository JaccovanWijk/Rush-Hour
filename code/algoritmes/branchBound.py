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
        self.i = 0

        self.visualizer = v.readBoard(self.currentVehicles)


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

        # name = "Branch&Bound" + str(self.i)
        # v.drawBoard(self.currentVehicles, self.size, self.visualizer, name)
        # self.i += 1

        # if won, set new upperlimit
        if self.won(self.currentVehicles):
            self.upperBound = moves
            self.iterations += 1
            self.openBoards = self.tempOpenBoards
            self.done = True
            print("New upperbound =", moves)
            return

        # add current board to queue
        self.tempOpenBoards.append((board, moves))

        # self.currentBoard = board
        for newBoard in self.sortedSucessors(board):

            # request recursive solve
            if (newBoard, moves + 1) not in self.closedBoards:
                self.solver(newBoard, moves + 1)

        if not self.done:
            self.closedBoards.add(self.tempOpenBoards.pop())


    def sortedSucessors(self, boards):
        """Sort list of boards"""
        sucessors = self.getSucessors(boards)
        
        return sucessors

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

                sucessors.append(newBoard)

        return sucessors

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

    def heuristic (self, boards, car):

        goalVehicles = self.getVehicles(self.goalBoard)
        scores = []

        for (board, i) in boards:

            score = 0
            vehicles = self.getVehicles(board)

            for vehicle in vehicles:
                if vehicle.name == car.name:
                    score += abs(vehicle.dominantCoordinate() - car.dominantCoordinate())
            # for vehicle in vehicles:
            #      for goalVehicle in goalVehicles:
            #
            #          if vehicle.name == goalVehicle.name:
            #              score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
            #
            # scores.append((score, (board, i)))

        return

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

# class PriorityQueue(Queue.Queue):
#
#     def _insert(self, item):
#         board, score = item
#         self.place((board, score))
#
#     def _get(self):
#         return self.queue.pop(0)[1]
#
#     def place(self, item):
#         openBoards = self.queue
#         low = 0
#         high = len(openBoards)
#
#         while low < high:
#             mid = (low+high)/2
#             if item[0] < openBoards[mid][0]:
#                 high = mid
#             else:
#                 low = mid + 1
#         openBoards.insert(low, item)
