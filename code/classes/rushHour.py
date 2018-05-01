import vehicle as v
import math

class RushHour:
    """A single Rush Hour board"""

    def __init__(self, board, size):

        self.testHistory = []
        self.initBoard = board.replace("\n", "")
        self.size = size
        self.vehicles = self.getVehicles(self.initBoard)
        if size % 2 == 0:
            self.yGoal = self.size//2 - 1
        else:
            self.yGoal = self.size//2
        self.moves = dict()


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
                vehicles.append(v.vehicle(board[i], x, y, 1, 'N'))
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


    def searchMoves(self, vehicle, allMoves=True):

        """Search for available moves for a given vehicle"""

        moves = []

        # get line of view
        lineOfView = self.driveline(vehicle)
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


    def won(self, vehicles):
        """Returns true if winning condition is satisfied"""

        for vehicle in vehicles:
            if vehicle.name == 'X' and vehicle.xBegin == self.size - 2 and vehicle.yBegin == self.yGoal:
                return True
        return False

    def driveline(self, vehicle):
        """Return possible driveline"""
        possibleDrive = ""
        if vehicle.orientation == "H":
            # pick everything in it's row
            possibleDrive = self.initBoard[vehicle.yBegin * self.size: vehicle.yBegin * self.size + self.size]
        elif vehicle.orientation == "V":
            # pick everything in it's column
            possibleDrive = self.initBoard[vehicle.xBegin::self.size]
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

    def showBoard(self):

        for i in range(self.size):
            print(self.initBoard[i*self.size:(i+1)*self.size])
