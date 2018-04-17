import vehicle as v
import math

# Hardcode doelauto (TODO)
GOAL_VEHICLE = v.vehicle('X', 4, 2, 2, 'H')

class rushHour:

    def __init__(self, board):

        self.testHistory = []
        self.initBoard = board.replace("\n", "")
        self.size = int(math.sqrt(len(self.initBoard)))
        self.vehicles = self.getVehicles(self.initBoard)


    def update(self):

        # initialise board
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append('.')
            board.append(row)
        # show all vehicles
        for vehicle in self.vehicles:
            for i in range(vehicle.length):
                if vehicle.orientation == 'V':
                    board[vehicle.yBegin + i][vehicle.xBegin] = vehicle.name
                elif vehicle.orientation == 'H':
                    board[vehicle.yBegin][vehicle.xBegin + i] = vehicle.name

        boardStr = ""
        for i in board:
            for j in i:
                boardStr += j


        return boardStr

    def getVehicles(self, board):

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


    def searchMoves(self, vehicle):

        moves = []
        # search all moves horizontally
        if vehicle.orientation == 'H':

            # search move left
            if vehicle.xBegin - 1 >= 0:
                if self.initBoard[vehicle.yBegin * 6 + vehicle.xBegin - 1] == ".":
                    moves.append(-1)

            # search move right
            elif vehicle.xBegin + vehicle.length < 6:
                if self.initBoard[vehicle.yBegin * 6 + vehicle.xBegin + vehicle.length] == ".":
                    moves.append(1)

        elif vehicle.orientation == 'V':

            # search move up
            if vehicle.yBegin - 1 >= 0:
                if self.initBoard[(vehicle.yBegin - 1) * 6 + vehicle.xBegin] == ".":
                    moves.append(-1)

            # search move down
            elif vehicle.yBegin + vehicle.length < 6:
                if self.initBoard[(vehicle.yBegin + vehicle.length) * 6 + vehicle.xBegin] == ".":
                    moves.append(1)

        return moves

    def makingMove(self, car, direction):
        car.move(direction)
        return self.update()

    # return true if game is won
    def won(self):

        return GOAL_VEHICLE in self.vehicles