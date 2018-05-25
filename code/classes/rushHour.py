"""
rushHour.py: Implements a general rush hour board.

In this module a general rush hour board and some
methods with it are implemented
"""

import vehicle as v
import math
import visualizer as vis

class RushHour:
    """A single Rush Hour board."""

    def __init__(self, board):
        """Initialise rush hour game."""
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
        """Update board with new set of cars."""
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
        """Read in vehicle of a given board."""
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
        """Search for available moves for a given vehicle."""
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
        """Move a car in a given direction."""
        car.move(direction)

        return self.update(vehicles)

    def getCar(self, vehicles, name):
        """Return the vehicle with corresponding name."""
        for vehicle in vehicles:
            if vehicle.name == name:
                return vehicle

    def won(self, vehicles):
        """Return true if winning condition is satisfied."""
        for vehicle in vehicles:
            if vehicle.name == 'X' and vehicle.xBegin == self.size - 2 and vehicle.yBegin == self.yGoal:
                return True
        return False

    def driveline(self, board, vehicle):
        """Return possible driveline."""
        possibleDrive = ""
        if vehicle.orientation == "H":
            # pick everything in it's row
            possibleDrive = board[vehicle.yBegin * self.size: vehicle.yBegin * self.size + self.size]
        elif vehicle.orientation == "V":
            # pick everything in it's column
            possibleDrive = board[vehicle.xBegin::self.size]
        return possibleDrive

    def showMoves(self, endState, moves):
        """Make a list of moves made to solve the puzzle."""
        moveList = list()

        while True:

            # go back one move
            row = moves[endState]
            if len(row) != 0:
                endState = row

                # add move to list
                moveList.append(endState)
            else:
                break

        moveList.reverse()
        return moveList

    def getSucessors(self):
        """Get next board states reachable by making one move."""
        sucessors = []

        # get all moves of all vehicles
        for vehicle in self.currentVehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles,vehicle, i)
                self.makingMove(self.currentVehicles,vehicle, -i)

                sucessors.append(newBoard)

        return sucessors

    def showBoard(self, board):
        """Print board in a better way."""
        for i in range(self.size):
            print(board[i*self.size:(i+1)*self.size])
        print("")

    def visualise(self, vehicles, fileName):
        """Create an image of the board, named <fileName>."""
        vis.drawBoard(vehicles, self.size, self.huemap, fileName)

    def heuristic0(self, board):
        """The null-heuristic."""
        return 0

    def heuristic1 (self, board):
        """Estimate moves to solution by distance of open spots to goal."""
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
        """Estimate moves to solution by difference to an endstate."""
        score = 0

        goalVehicles = self.getVehicles(endState)
        vehicles = self.getVehicles(board)

        for vehicle in vehicles:
            for goalVehicle in goalVehicles:
                if vehicle.name == goalVehicle.name:
                    score += abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
        return score/len(vehicles)

    def heuristic3 (self, board, score=True):
        """Estimate moves to solution by the amount of cars blocking the goal."""
        vehicles = self.getVehicles(board)
        if self.won(vehicles) and score:
            return 0

        goalCar = self.getCar(vehicles, "X")
        lineOfView = self.driveline(board, goalCar)

        # search for blocking cars
        names = []
        afterCar = goalCar.dominantCoordinate() + goalCar.length
        for i in range(afterCar, self.size):
            if lineOfView[i] != ".":
                names.append(lineOfView[i])
        blockingCars = [self.getCar(vehicles, name) for name in names]

        if score:
            return len(blockingCars) + 1
        else:
            return blockingCars

    def heuristic4(self, board):
        """Estimate moves to solution by moves required to move the goal a spot."""
        vehicles = self.getVehicles(board)
        goalCar = self.getCar(vehicles, "X")
        if self.won(vehicles):
            return 0

        blockingCars = self.heuristic3(board, False)

        scores = []
        for car in blockingCars:
            scores.append(self.searchMovable(vehicles, car, {goalCar}, 1))
        return min(scores)

    def searchMovable(self, vehicles, vehicle, prevVehicles, N):
        """Recursively search for movable vehicles."""
        board = self.update(vehicles)
        lineOfView = self.driveline(self.update(vehicles), vehicle)
        beginC = vehicle.dominantCoordinate()

        neighbours = []
        if beginC - 1 >= 0:
            neighbours.append(lineOfView[beginC - 1])
        if beginC + vehicle.length < self.size:
            neighbours.append(lineOfView[beginC + vehicle.length])

        if "." in neighbours or vehicle in prevVehicles:
            return N + 1

        prevVehicles.add(vehicle)
        scores = []
        for name in neighbours:
            newVehicle = self.getCar(vehicles, name)
            score = self.searchMovable(vehicles, newVehicle, prevVehicles, N + 1)
            scores.append(score)
        return min(scores)
