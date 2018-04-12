
import vehicle as v

# Hardcode doelauto (TODO)
GOAL_VEHICLE = v.vehicle('X', 4, 2, 2, 'H')

class rushHour:

    def __init__(self, board, size):


        self.vehicles = []
        self.size = size
        amount = 0
        names = []

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


    def show(self):

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