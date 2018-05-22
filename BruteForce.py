import rushHour as r
import random
import math
import visualizer as vis

class BruteForce(r.RushHour):
    """A random algorithm for Rush Hour."""

    def __init__(self, board):

        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.moves = 0
        for vehicle in self.vehicles:
            if vehicle.name == "X":
                self.carX = vehicle

        # initialise move memory
        self.memory = dict()
        self.memory[self.currentBoard] = ()

    def solver(self, endState=False):
        """Get a random solution."""

        name = "Groot0"
        self.visualise(self.currentVehicles, name)

        lastCar = None
        # i = 0
        while not self.won(self.currentVehicles):

            # i += 1
            # name = "Random" + str(i)
            # print(name)

            board = self.currentBoard
            car = random.choice(self.vehicles)

            # search moves selected car
            possibleMoves = self.searchMoves(self.currentBoard,car)
            if possibleMoves:

                # make random move
                move = random.choice(possibleMoves)
                # keep track of moves
                self.moves += 1
                # update current board
                self.currentBoard = self.makingMove(self.currentVehicles,car, move)

                #vis.drawBoard(self.vehicles, self.size, self.visualizer, name)

                if self.currentBoard not in self.memory:
                    self.memory[self.currentBoard] = (board, "HOI")

                if self.won(self.currentVehicles):
                    break

        moveList = self.showMoves(self.currentBoard, self.memory)
        if endState:
            return self.moves, len(moveList), self.currentBoard
        return self.moves, len(moveList) + 1
