import rushHour as r
import random
import math

class BruteForce(r.RushHour):
    """A random algorithm for Rush Hour"""

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

    def solver(self):
        """Get a random solution"""

        lastCar = None
        while not self.won(self.currentVehicles):

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

                if self.currentBoard not in self.memory:
                    self.memory[self.currentBoard] = (board, "HOI")

                possibleDriveX = self.driveline(self.currentBoard, self.carX)
                if self.ended(possibleDriveX):
                    break

        moveList = self.showMoves(self.currentBoard, self.memory)
        return self.moves, len(moveList)


    def ended(self, possibleDrive):
        """Check if it's possible to end game"""

        # if there's only dots after goalcar, game is won
        afterGoal = False
        for letter in possibleDrive:
            if letter == 'X':
                afterGoal = True
            elif letter != '.':
                if afterGoal:
                    return False
            elif afterGoal and letter == ".":
                self.moves += 1

        return True
