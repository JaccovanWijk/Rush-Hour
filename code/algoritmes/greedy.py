import rushHour as r

class greedy(r.rushHour):

    def __init__(self, board):

        r.rushHour.__init__(self,board)
        self.board = self.initBoard


    # def solve(self, board):
    #
    #     print(self.initBoard, 1)
    #     for car in self.vehicles:
    #             if car.name == "X":
    #                 currentCar = car
    #
    #     goalVehicles = []
    #     testedVehicles = []
    #     move = 0
    #
    #      while move < 3:#not self.won():
    #          print(self.initBoard, 2)
    #          # zorg dat deze de maximale moves naar beide kanten wordt
    #          # DIT KLOPT NIET AL HIJ ALLEEN POSITIEF HEEFT/ALLEEN NEGATIEF HEEFT
    #          possibleMoves = self.searchMoves(currentCar)
    #          x = max(s for s in possibleMoves)
    #          y = min(s for s in possibleMoves)
    #          moves = [x,y]
    #          print(self.initBoard,3)
    #          if currentCar not in testedVehicles:
    #              goalVehicles.append(currentCar)
    #              testedVehicles.append(currentCar)
    #          #elif len(moves) > 0:
    #          #    moves.pop(0)
    #          #else:
    #          print(self.initBoard,4)
    #          if len(moves) == 0:
    #              print(self.initBoard,5)
    #              neighbours = self.neighboursFinder(currentCar)
    #
    #              currentCar = neighbours[0]
    #
    #              #currentCar = goalVehicles[-2]
    #              #goalVehicles.pop()
    #          elif len(moves) == 1:
    #              self.makingMove(currentCar, moves[0])
    #              print(self.initBoard,6)
    #          else:
    #              # take first argument of moves
    #              self.makingMove(currentCar,moves[0])
    #              print(self.initBoard,7)
    #          print(self.initBoard, 8)
    #
    #          move += 1


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

        goalVehicles = []
        testedVehicles = []
        print("Voor whileloop")

        board = self.initBoard

        move = 0
        while move < 3:#not self.won:

            print("begin Whileloop")
            # check of de vorige nu wel kan rijden
            if len(goalVehicles) > 1:
                print("Meer dan 1 bekeken")
                prevPossibleDrive = self.driveline(goalVehicles[-2])
                if goalVehicles[-1] not in prevPossibleDrive:
                    currentCar = goalVehicles[-2]
                    goalVehicles.pop()

            # check of current car nog wel een kant op kan die nuttig is/ nog niet is geweest
            #if currentCar.name in testedVehicles:
                #if


            # check if current car is already tested
            if currentCar.name not in testedVehicles:
                print("is huidige auto al getest?")
                goalVehicles.append(currentCar)
                testedVehicles.append(currentCar.name)


            # find possible moves for current car
            possibleMoves = self.searchMoves(currentCar)

            if len(possibleMoves) == 0:
                print("geen zetten mogelijk met huidige auto")
                # find neighbours and
                neighbours = self.neighboursFinder(currentCar)
                # for neighbour in neighbours:
                #     if neighbour.name in testedVehicles:
                #         # check of die buur nog een andere move kan doen, zo niet verwijder hem
                #         neighbours.pop(0)
                # MAAK NOG EEN CHEKCER OM TE KIJKEN OF DE BUUR AL GECHECKT IS

                if len(neighbours) != 0:

                    currentCar = neighbours[0]
                    print("HUIDIGE AUTO HEEFT ALLEEN MAAR BUREN OMG")
                else:
                    # ga terug naar de laatste auto die twee opties had
                    currentCar = goalVehicles[-2]
                    goalVehicles.pop()

            elif len(possibleMoves) == 1:

                maxStep = max(x for x in possibleMoves)
                if maxStep < 0:
                    print("HUIDIGE AUTO KAN ZETJE NAAR LINKS/BOVEN EN HEEFT RECHTS/ONDER EEN BUURTJE")
                    neighbours = self.neighboursFinder(currentCar)
                    minStep = min(x for x in possibleMoves)

                    if len(neighbours) != 0:
                        if neighbours[0] not in testedVehicles:
                            currentCar = neighbours[0]
                        else:
                            board = self.makingMove(currentCar, minStep)
                            print(board)
                    else:
                        board = self.makingMove(currentCar, minStep)
                        print(board)

                else:
                    print("stapje naar rechts rechts rechts")
                    board = self.makingMove(currentCar, maxStep)
                    print(board)

            else:
                maxStep = max(x for x in possibleMoves)
                board = self.makingMove(currentCar, maxStep)
                print(board)
                print("zetje naar RECHTS")

            move += 1
        return board

    def greedy(self):

        for car in self.vehicles:
                if car.name == "X":
                    currentCar = car

        goalVehicles = []
        testedVehicles = []

        board = self.initBoard


    def greedysolver(self,board,car):

        