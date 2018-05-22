import rushHour as r
import vehicle as v
from time import time
from copy import deepcopy
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def empty(self):
        return len(self._queue) == 0

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class ZeroHeuristic:
    """Zero Heuristcs, same as a Breadth First search"""

    def calculate(self, board):
        return 0

    def __repr__(self):
        return 'ZeroHeuristic'

class BlockingCarsHeuristic:

    #Calculate the number of blocking vehicles
    def obstruction(self, board):
        red_vehicle = [
            vehicle for vehicle in board.vehicles if vehicle.name == 'X'][0]
        if red_vehicle.coord['x'] == 4:
            return 0
        blockingvehicles = 1
        for vehicle in board.vehicles:
            if vehicle.orientation == "V" and vehicle.coord['x'] >= (red_vehicle.coord['x']
            + red_vehicle.length) and (vehicle.coord['y'] <= red_vehicle.coord['y']
            and vehicle.coord['y'] + vehicle.length > red_vehicle.coord['y']):
                blockingvehicles += 1
        return blockingvehicles

    def __repr__(self):
        return 'BlockingCarsHeuristic'

class A_Star(r.RushHour):
    """"An A* search algorithm for Rush Hour"""

    def __init__(self, board, heuristic):

        r.RushHour.__init__(board, heuristic)

        # model game
        self.board = board
        self.heuristic = heuristic
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.weights = {}
        #self.parent = None
        #self.map = []


    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    # the searching algorithm
    def solver(self):

        # open and closed possibilities
        openBoards = PriorityQueue()
        board = self.board
        closedBoards = set()
        # moves done
        moves = dict()

        # cost of path from start to end-nodes
        G_Cost = {}

        # estimated cost of the cheapest path to goal
        #H_Cost = {}

        # iteration counter
        count = 0

        # returns solution, amount of moves, G_Cost and iterations
        beginTime = time()

        # initialise search, move count and cost
        self.openBoards.insert(0, self.currentBoard)
        self.moves[self.currentBoard] = ()
        self.G_Cost[self.currentBoard] = 0

        while not openBoards.empty():
            currentBoard = openBoards.pop()
            #newBoard = self.Board()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is goal is met
            if self.won(self.currentVehicles):
                return (self.showMoves(self.currentBoard, moves), count, time() - beginTime)
            count += 1

            # loop through the newBoard's sucessors/siblings
            for newBoard in self.getSucessors(currentBoard):

                # if it is already in the closed set, skip it
                if newBoard in closedBoards:
                    continue

                # otherwise if it is already in the queue
                if newBoard in self.openBoards:

                    # Check if we beat the cost and update if so.
                    new_cost = currentBoard.G_Cost + board.cost(currentBoard, newBoard)
                    priority = new_cost + self.heuristic.obstruction(newBoard)
                    if newBoard not in self.G_Cost or new_cost < newBoard.G_Cost:
                        newBoard.G_Cost = new_cost
                        openBoards.push(next, priority)
                        #closedBoards.add(currentBoard)
                        newBoard.parent = currentBoard

                else:
                    # if it isn't in the open board yet
                    newBoard.G_Cost = currentBoard.G_Cost + currentBoard.cost(newBoard)
                    #newBoard.H_Cost = self.obstruction(newBoard, won)

                    # set the parent to our currentBoard item
                    newBoard.parent = currentBoard

                    # add it to the queue
                    newBoard = openBoards.pop()

            # move the item from the queue and add to the closed set
            currentBoard = openBoards.empty()
            closedBoards.add(currentBoard)

            # check for errors
            raise ValueError('Not Solvable')

        # step by step guide of all moves used to solve the puzzle
        def solution(self, board, won):
            output = ''
            output += "; ".join(["{} {}".format(move[0], move[1]) for move in moves])
            vehicles = deepcopy(board.vehicles)
            for move in moves:
                vehicle = [x for x in vehicles if x.vehicles == move[0]][0]
                output += '\nMOVE {} {}\n'.format(move[0], move[1])
                vehicle.move(move[1], 1)
                output += self.board.prettify(vehicles)
            return output



    def getSucessors(self, point):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.vehicles

        # get all moves of all vehicles
        for vehicle in self.vehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles, vehicle, i)
                self.makingMove(self.currentVehicles, vehicle, -i)
                # make move string
                move = vehicle.name + ' ' + str(i)

                sucessors.append([newBoard, move])

        return sucessors
