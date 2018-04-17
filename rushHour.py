import vehicle as v

# Hardcode doelauto (TODO)
GOAL_VEHICLE = v.vehicle('X', 4, 2, 2, 'H')
initboard = []

class rushHour:

    def __init__(self, board, size):

        self.vehicles = []
        self.size = size
        amount = 0
        names = []
        self.testHistory = []

        # read in board
        for i in range(len(board)):
            # current coordinates
            x = i % self.size
            y = i // self.size

            # make new vehicles
            if board[i] != '.' and board[i] not in names:
                self.vehicles.append(v.vehicle(board[i], x, y, 1, 'N'))
                names.append(board[i])

            # change length if vehicle does exist
            elif board[i] in names:
                index = names.index(board[i])
                car = self.vehicles[index]
                car.length += 1
                if x == car.xBegin:
                    car.orientation = 'V'
                else:
                    car.orientation = 'H'

        self.initBoard = self.update()


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

        return board

    def searchMoves(self, board, vehicle):

        moves = []
        # search all moves horizontally
        if vehicle.orientation == 'H':
            i = 0
            # search all moves to the left
            while vehicle.xBegin - i >= 0 and board[vehicle.yBegin][vehicle.xBegin - i] == '.':
                moves.append(i)
                i += 1

            j = 0
            # search all moves to the right
            while vehicle.xBegin + j < 6 and board[vehicle.yBegin][vehicle.xBegin + j] == '.':
                moves.append(j)
                j += 1

        elif vehicle.orientation == 'V':
            i = 0
            # search all moves to above
            while vehicle.yBegin - i >= 0 and board[vehicle.yBegin - i][vehicle.xBegin] == '.':
                moves.append(i)
                i += 1

            j = 0
            # search all moves to below
            while vehicle.xBegin + i < 6 and board[vehicle.yBegin - j][vehicle.xBegin] == '.':
                moves.append(j)
                j += 1

        return moves

    def makingMove(self, direction, car):
        car.move(direction)
        return self.update()


    # return true if game is won
    def won(self):

        return GOAL_VEHICLE in self.vehicles