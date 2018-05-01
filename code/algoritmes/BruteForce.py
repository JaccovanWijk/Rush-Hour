import rushHour as r
import random

class bruteForce(r.rushHour):

    def __init__(self, board, size):

        r.rushHour.__init__(self, board, size)

    def solver(self, restrictions=False):

        for vehicle in self.vehicles:
            if vehicle.name == "X":
                carX = vehicle

        moves1 = 0
        moves2 = 0
        # if not restrictions:
        #     while not self.won():
        #
        #         car = random.choice(self.vehicles)
        #
        #         possibleMoves = self.searchMoves(car)
        #         if possibleMoves:
        #             moves1 += 1
        #
        #             move = random.choice(possibleMoves)
        #             self.initBoard = self.makingMove(car, move)
        #
        #     return moves1


        # else:
        lastCar = [""]
        while not self.won():

            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(car)
            if possibleMoves and car.name != lastCar[-1]:
                moves2 += 1

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
                    moves2 += 1
                    break
            # possibleMovesX = self.searchMoves(carX, False)
            #
            # if possibleMovesX:
            #     if possibleMovesX[1] > 0:
            #         moves2 += 1
            #         self.initBoard = self.makingMove(carX, possibleMovesX[1])
            #
            # print(self.won())

        return moves2
