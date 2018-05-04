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

        for vehicle in self.vehicles:
            if vehicle.name == "X":
                carX = vehicle

        lastCar = None
        board = []
        while not self.won(self.currentVehicles):

            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(self.currentBoard,car)
            if possibleMoves and car.name != lastCar:

                move = random.choice(possibleMoves)
                self.moves += 1
                self.currentBoard = self.makingMove(self.currentVehicles,car, move)

                if restriction:
                    if lastCar == car.name:
                        lastCar = None
                    else:
                        lastCar = car.name

                possibleDriveX = self.driveline(self.currentBoard, carX)
                if self.ended(possibleDriveX):
                    break

        return self.moves


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
