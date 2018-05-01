import rushHour as r
import random

class BruteForce(r.rushHour):

    def __init__(self, board, size):

        r.rushHour.__init__(self, board, size)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

    def solver(self, restrictie=False):

        for vehicle in self.vehicles:
            if vehicle.name == "X":
                carX = vehicle

        moves = 0

        lastCar = None
        board = []
        while not self.won():

            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(car)
            if possibleMoves and car.name != lastCar:
                moves += 1

                move = random.choice(possibleMoves)
                self.currentBoard = self.makingMove(self.CurrentVehicles,car, move)

                if restrictie:
                    lastCar = car.name

                possibleDriveX = self.driveline(carX)
                if ended(possibleDriveX):
                    break

        return moves


    def ended(self, possibleDrive):

        afterGoal = False
        ended = True
        for letter in possibleDrive:
            if letter == 'X':
                afterGoal = True
            elif letter != '.':
                if afterGoal:
                    return False
            elif afterGoal and letter == ".":
                moves += 1

        return True
