import rushHour as r
import vehicle as v

class greedy(r.RushHour):

    def __init__(self, board):

        r.RushHour.__init__(self,board)
        self.board = self.initBoard
        self.goalVehicles = []
        self.testedVehicles = []
        self.errorCar = v.vehicle('Error',2,0,0,'H')
        self.errorBoard = 'Error'
        self.closedBoards = set()

    def neighboursFinder(self, board, vehicle):

        possibleDrive = self.driveline(board, vehicle)

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


    # def testNeighbours(self, board, car):
    #
    #     neighbours = self.neighboursFinder(board, car)
    #     for neighbour in neighbours:
    #         # maak deze check beter, MAYBE DICT, DAN KAN JE DE ZET ALS WAARDE DOEN BIJ DE AUTO TODO
    #         if self.goalVehicles.count(neighbour) > 1:
    #             neighbours.remove(neighbour)
    #
    #     if neighbours:
    #         return neighbours
    #     else:
    #         return self.errorCar



    def solver(self, currentBoard, car):

        if currentBoard in self.closedBoards:
            return (self.errorBoard,self.errorCar)

        self.closedBoards.add(currentBoard)

        while True:

            maxMove = max(x for x in possibleMoves)
            minMove = min(x for x in possibleMoves)

            possibleMoves = self.searchMoves(car)
            neighbours = self.neighboursFinder(currentBoard, car)

            if not possibleMoves:

                # check if he has neighbours
                if not neighbours:
                    return (self.errorBoard, self.errorCar)

                # check next car TODO nextState met of zonder auto?
                nextState, nextCar = self.solver(currentBoard, neighbours[0])
                # check for error
                if nextState == self.errorBoard:
                    return nextState

                else:
                    currentBoard = nextState

            else:
                if maxMove > 0 and minMove < 0:
                    maxMove = maxMove
                    # pas heuristiek toe
                elif maxMove < 0:

                    nextState, nextCar = self.solver(currentBoard, car)












        #
