import rushHour as r
import random
import math

class BruteForce(r.RushHour):
    """A random algorithm for Rush Hour."""

    def __init__(self, board):

        # model for game
        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.moves = 0
        self.carX = self.getCar(self.currentVehicles, "X")

        # initialise move memory
        self.memory = dict()
        self.memory[self.currentBoard] = ()


    def solver(self):
        """Get a random solution."""

        lastCar = None
        while not self.won(self.currentVehicles):

            #initialise search
            board = self.currentBoard
            car = random.choice(self.vehicles)

            # search moves for selected car
            possibleMoves = self.searchMoves(self.currentBoard,car)
            if possibleMoves:

                # make random move
                move = random.choice(possibleMoves)
                # keep track of moves
                self.moves += 1
                # update current board
                self.currentBoard = self.makingMove(self.currentVehicles,car, move)

                # memorize moves made
                if self.currentBoard not in self.memory:
                    self.memory[self.currentBoard] = board

                # stop if puzzle is solved
                if self.won(self.currentVehicles):
                    break

        # remove repetitive moves
        moveList = self.showMoves(self.currentBoard, self.memory)
        return self.moves, len(moveList) + 1, self.currentBoard
