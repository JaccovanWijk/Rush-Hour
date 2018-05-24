import vehicle as v
import math
import visualizer as vis

class RushHour:
    """A single Rush Hour board"""

    def __init__(self, board):

        # create board
        self.initBoard = board.replace("\n", "")
        self.size = int(math.sqrt(len(self.initBoard)))
        self.vehicles = self.getVehicles(self.initBoard)
        if self.size % 2 == 0:
            self.yGoal = self.size//2 - 1
        else:
            self.yGoal = self.size//2
        self.moves = dict()
        self.huemap = vis.readBoard(self.vehicles)


    def update(self, vehicles):
        """Update board with new set of cars"""

        # initialise board
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append('.')
            board.append(row)

        # show all vehicles
        for vehicle in vehicles:
            for i in range(vehicle.length):
                if vehicle.orientation == 'V':
                    board[vehicle.yBegin + i][vehicle.xBegin] = vehicle.name
                elif vehicle.orientation == 'H':
                    board[vehicle.yBegin][vehicle.xBegin + i] = vehicle.name

        # convert char array to string
        boardStr = ""
        for i in board:
            for j in i:
                boardStr += j

        return boardStr


    def getVehicles(self, board):
        """Read in vehicle of a given board"""

        names = []
        vehicles = []
        # read in board
        for i in range(len(board)):
            # current coordinates
            x = i % self.size
            y = i // self.size

            # make new vehicles
            if board[i] != '.' and board[i] not in names:
                vehicles.append(v.Vehicle(board[i], x, y, 1, 'N'))
                names.append(board[i])

            # change length if vehicle does exist
            elif board[i] in names:
                index = names.index(board[i])
                car = vehicles[index]
                car.length += 1
                if x == car.xBegin:
                    car.orientation = 'V'
                else:
                    car.orientation = 'H'
        return vehicles


    def searchMoves(self, board, vehicle, allMoves=True):

        """Search for available moves for a given vehicle"""

        moves = []

        # get line of view
        lineOfView = self.driveline(board, vehicle)
        beginC = vehicle.dominantCoordinate()

        # search for moves down/right
        i = 1
        while beginC + vehicle.length + i - 1 < len(lineOfView):
            if lineOfView[beginC + vehicle.length + i - 1] == '.':
                moves.append(i)
            else:
                break
            i += 1

        j = 1
        while beginC - j >= 0:
            if lineOfView[beginC - j] == '.':
                moves.append(-j)
            else:
                break
            j += 1

        # return all or maximum moves
        if allMoves:
            return moves
        else:
            return [-j,i]

    def makingMove(self, vehicles, car, direction):
        """Move a car in a given direction"""

        car.move(direction)

        return self.update(vehicles)

    def getCar(self, vehicles, name):
        """Returns the vehicle with corresponding name"""

        for vehicle in vehicles:
            if vehicle.name == name:
                return vehicle

    def won(self, vehicles):
        """Returns true if winning condition is satisfied"""

        for vehicle in vehicles:
            if vehicle.name == 'X' and vehicle.xBegin == self.size - 2 and vehicle.yBegin == self.yGoal:
                return True
        return False

    def driveline(self, board, vehicle):
        """Return possible driveline"""
        possibleDrive = ""
        if vehicle.orientation == "H":
            # pick everything in it's row
            possibleDrive = board[vehicle.yBegin * self.size: vehicle.yBegin * self.size + self.size]
        elif vehicle.orientation == "V":
            # pick everything in it's column
            possibleDrive = board[vehicle.xBegin::self.size]
        return possibleDrive

    def showMoves(self, endState, moves):
        """Makes a list of moves made to solve the puzzle"""

        moveList = list()

        while True:

            # go back one move
            row = moves[endState]
            if len(row) == 2:
                endState = row[0]
                move = row[1]

                # add move to list
                moveList.append(move)
            else:
                break

        moveList.reverse()
        return moveList

    def showBoard(self, board):
        """Print board in a better way"""
        for i in range(self.size):
            print(board[i*self.size:(i+1)*self.size])
        print("")

    def visualise(self, vehicles, fileName):
        """Creates an image of the board, named <fileName>"""

        vis.drawBoard(vehicles, self.size, self.huemap, fileName)

    def heuristic1 (self, board):
        """Returns score for a given board, looks at average distance
        from all empty spots to the exit"""

        score = 0
        amount = 0
        for i in range(self.size*self.size):
            if board[i] == ".":
                # add x difference
                score += self.size - i % self.size
                # add y difference
                score += abs(1 - i // self.size)
                amount += 1
        return score/amount

    def heuristic2 (self, board, endState):
        """Returns score for a given board, looks at the average difference
        from a random endState"""

        score = 0

        goalVehicles = self.getVehicles(endState)
        vehicles = self.getVehicles(board)

        for vehicle in vehicles:
            for goalVehicle in goalVehicles:
                if vehicle.name == goalVehicle.name:
                    score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
        return score/len(vehicles)

    def heuristic3 (self, board):
        """Returns score for a given board,
        looks at the number of vehicles blocking the red car"""

        score = 0

        vehicles = self.getVehicles(board)
        redVehicle = [vehicle for vehicle in vehicles if vehicle.name == 'X'][0]
        if redVehicle.xBegin == self.size - 2:
            return 0

        for vehicle in vehicles:
            if vehicle.orientation == "V" and vehicle.xBegin >= (redVehicle.xBegin
            + redVehicle.length) and (vehicle.yBegin <= redVehicle.yBegin
            and vehicle.yBegin + vehicle.length > redVehicle.yBegin):
                score += 1
        return score

    def heuristic4(self, board):
        """Returns score for a given board,
        looks at moves to free up blocking cars"""

        score = 0
        vehicles = self.getVehicles(board)
        goalCar = getCar(vehicles, "X")

        if self.won(vehicles):
            return score

        lineOfView = self.driveline(board, vehicle)

        # search for blocking cars
        names = []
        for i in range(goalCar.dominantCoordinate() + goalCar.length, self.size):
            if lineOfView[i] != ".":
                names.append(lineOfView[i])
        blockingCars = [self.getCar(vehicles, name) for name in names]
