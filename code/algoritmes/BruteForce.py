import rushHour as r
import random
import math
import visualizer as vis

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

<<<<<<< HEAD
        name = "Groot0"
        self.visualise(self.currentVehicles, name)
=======
        # name = "Random0"
        #vis.drawBoard(self.vehicles, self.size, self.visualizer, name)
>>>>>>> 268867a9df29d838e82487ab564e593f1a81539a

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

                possibleDriveX = self.driveline(self.currentBoard, self.carX)
                if self.won(self.currentVehicles):#ended(possibleDriveX):
                    break

        moveList = self.showMoves(self.currentBoard, self.memory)
        return self.moves, len(moveList) + 1


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

        self.moves += 1
        return True
