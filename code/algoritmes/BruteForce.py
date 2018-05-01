import rushHour as r
import random

class bruteForce(r.rushHour):

    def __init__(self, board, size):

        r.rushHour.__init__(self, board, size)

    def solver(self):

        for vehicle in self.vehicles:
            if vehicle.name == "X":
                carX = vehicle

        moves = 0

        lastCar = [""]
        while not self.won():

            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(car)
            if possibleMoves and car.name != lastCar[-1]:
                moves += 1

                move = random.choice(possibleMoves)
                self.initBoard = self.makingMove(car, move)

                lastCar.append(car.name)

                possibleDriveX = self.driveline(carX)

                afterGoal = False
                ended = True
                for letter in possibleDriveX:
                    if letter == 'X':
                        afterGoal = True
                    elif letter != '.':
                        if afterGoal:
                            ended = False

                if ended:
                    moves += 1
                    break

        return moves
