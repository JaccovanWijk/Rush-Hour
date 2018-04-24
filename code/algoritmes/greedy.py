import rushHour as r
import vehicle as v

class greedy(r.rushHour):

    def __init__(self, board):

        r.rushHour.__init__(self,board)
        self.board = self.initBoard
        self.goalVehicles = []
        self.testedVehicles = []
        self.errorCar = v.vehicle('Error',2,0,0,'H')
        self.errorBoard = 'Error'

    def neighboursFinder(self, vehicle):

        possibleDrive = self.driveline(vehicle)

        neighbours = []
        length = len(possibleDrive)
        for i in range(length):
            if possibleDrive[i] == vehicle.name:
                if i != length - 1:
                    if possibleDrive[i + vehicle.length] != ".":
                        neighbours.append(possibleDrive[i + vehicle.length])
                if i != 0:
                    if possibleDrive[i - 1] != ".":
                        neighbours.append(possibleDrive[i - 1])

        # find car for neighbours name
        neighbourCars = []
        for car in neighbours:
            for vehicle in self.vehicles:
                if car == vehicle.name:
                    neighbourCars.append(vehicle)

        return neighbourCars

    def greedysolve(self):

        for car in self.vehicles:
                if car.name == "X":
                    currentCar = car

        board = self.greedysolver(self.board, currentCar)

        if board == self.errorBoard:
            print("something went wrong")
        return board


    def greedysolver(self,board,car):

        # test hier of je een stap terug moet?

        print(board)

        # keep track of the cars
        self.goalVehicles.append(car)
        self.testedVehicles.append(car.name)

        possibleMoves = self.searchMoves(car, False)

        if len(possibleMoves) == 0:
            print(1)
            nextCar = self.testNeighbours(car)
            if nextCar == self.errorCar:
                return self.errorBoard

            #FIX NOG FF DAT DIT WERKT
            return self.greedysolver(board, nextCar)

        elif len(possibleMoves) == 1:
            print(2)
            if possibleMoves[0] < 0:

                nextCar = self.testNeighbours(car)
                if nextCar == self.errorCar:
                    board = self.makingMove(car,possibleMoves[0])

                    return self.greedysolver(board, car)
                else:
                    return self.greedysolver(board, nextCar)
        else:
            print(3)
            board = self.makingMove(car,possibleMoves[0])
            return self.greedysolver(board, car)

        return board


    def testNeighbours(self,car):

        neighbours = self.neighboursFinder(car)
        for neighbour in neighbours:
            # maak deze check beter
            if self.goalVehicles.count(neighbour) > 1:
                neighbours.remove(neighbour)

        if neighbours:
            return neighbours[0]
        else:
            return self.errorCar













        #
