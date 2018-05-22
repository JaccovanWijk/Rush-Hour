from time import time
from copy import deepcopy

import rushHour as r
import visualizer as v
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
    def calculate(self, board):
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

    def __init__(self, board, heuristic, size):

        r.RushHour.__init__(self, board)

        # model game
        self.heuristic = heuristic
        self.size = size
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.G_Cost = {}
        self.visualizer = v.readBoard(self.currentVehicles)

    # the searching algorithm
    def solver(self):

        # initial state plus open and closed possibilities
        openBoards = PriorityQueue()
        closedBoards = set()

        # estimated cost of the cheapest path to goal
        #H_Cost = {}

        # initiate counter, timer and visualizer
        count = 0
        beginTime = time()

        # initialise search, move count and cost
        openBoards.push([[], self.currentBoard], 0)
        self.moves[self.currentBoard] = ()
        self.G_Cost[self.currentBoard] = 0

        name = "A_Star0"
        v.drawBoard(self.vehicles, self.size, self.visualizer, name)
        i = 0

        while not openBoards.empty():

            #update board and cars
            currentBoard = openBoards.pop()
            self.currentVehicles = self.getVehicles(self.currentBoard)

            name = "A_Star" + str(count) + "-" + str(i)
            v.drawBoard(self.currentVehicles, self.size, self.visualizer, name)
            i += 1

            # stop if puzzle is puzzle is solved
            if self.won(self.currentVehicles):
                return (self.showMoves(self.currentBoard, self.moves), count, time() - beginTime)
            count += 1

            # loop through the newBoard's sucessors/siblings
            for (newBoard, move) in self.getSucessors(currentBoard):

                # if it is already in the queue
                new_cost = self.G_Cost[newBoard] + self.cost(currentBoard, newBoard)
                #new_cost = currentBoard.G_Cost + currentBoard.cost(currentBoard, newBoard)
                self.visualizer = v.readBoard(self.currentVehicles)
                priority = new_cost + self.heuristic.calculate(newBoard)
                if newBoard not in closedBoards:
                    self.moves[newBoard] = (self.currentBoard, move)
                    openBoards.push([self.moves + move, newBoard], priority)
                    closedBoards.add(newBoard)

                else:
                    # check if we beat the cost and update if so.
                    if newBoard not in self.G_Cost or new_cost < newBoard.G_Cost:
                        openBoards.push([self.moves + move, newBoard], priority)
                        # add it to the queue
                        newBoard = openBoards.pop()

                    # if it is already in the closed set, skip it
                    else:
                        continue

                newBoard.G_Cost = new_cost

            # move the item from the queue and add to the closed set
            currentBoard = openBoards.empty()
            #closedBoards.add(currentBoard)

            # check for errors
            raise ValueError('Not Solvable')

        # step by step guide of all moves used to solve the puzzle
        def solution(self, board):
            output = ''
            output += "; ".join(["{} {}".format(move[0], move[1]) for move in self.moves])
            vehicles = deepcopy(board.vehicles)
            for move in self.moves:
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