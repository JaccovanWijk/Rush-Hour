import rushHour as r
import random
import math

class BruteForce(r.RushHour):

    def __init__(self, board, size):

        r.RushHour.__init__(self, board, size)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.moves = 0

    def solver(self, restriction=False):

        memory = dict()
        memory[self.currentBoard] = ()

        for vehicle in self.vehicles:
            if vehicle.name == "X":
                carX = vehicle

        lastCar = None
        while not self.won(self.currentVehicles):

            board = self.currentBoard
            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(self.currentBoard,car)
            if possibleMoves and car.name != lastCar:

                move = random.choice(possibleMoves)
                self.moves += 1
                self.currentBoard = self.makingMove(self.currentVehicles,car, move)

                if self.currentBoard not in memory:
                    memory[self.currentBoard] = (board, "HOI")

                if restriction:
                    if lastCar == car.name:
                        lastCar = None
                    else:
                        lastCar = car.name

                possibleDriveX = self.driveline(self.currentBoard, carX)
                if self.ended(possibleDriveX):
                    break

        moveList = self.showMoves(self.currentBoard, memory)
        return self.moves, len(moveList)


    def ended(self, possibleDrive):

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
