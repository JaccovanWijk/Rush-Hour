
import rushHour as r
import vehicle as v
from time import time
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class A_Star(r.RushHour):
    """"An A* search algorithm for Rush Hour"""

    def __init__(self, board, size):

        r.RushHour.__init__(board, size)

        # model game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        #self.board = board
        #self.size = size
        self.parent = None
        self.map = []

        # cost of path from start to end-nodes
        self.G_Cost = {}

        # estimated cost of the cheapest path to goal
        self.H_Cost = {}

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


class BlockingCarsHeuristic:

    #calculate the number of blocking vehicles
    def obstruction(self, board):
        red_vehicle =
            vehicle for vehicle in board.vehicles if vehicle.name == 'X'][0]
        if red_vehicle.coord['x'] == 4:
            return 0
        blockingvehicles = 1
        for vehicle in board.vehicles:
            if vehicle.orientation == "V"
            and vehicle.coord['x'] >= (red_vehicle.coord['x'] + red_vehicle.length)
            and (vehicle.coord['y'] <= red_vehicle.coord['y']
            and vehicle.coord['y'] + vehicle.length > red_vehicle.coord['y']):
                blockingvehicles += 1
        return blockingvehicles

    def __repr__(self):
        return 'BlockingCarsHeuristic'

    # the searching algorithm
    def solver(self, board):

        # open and closed possibilities
        openBoards = PriorityQueue()
        closedBoards = set()
        # moves done
        moves = dict()

        # iteration counter
        count = 0
        beginTime = time()

        # initialise search and cost
        self.G_Cost[self.currentBoard ] = 0

        while not openBoards.empty():
            currentBoard = openBoards.get()
            #newBoard = self.Board()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is goal is met
            if self.won(self.currentVehicles):
                return (self.showMoves(self.currentBoard, moves), count, time() - beginTime)
            #if currentBoard == won:
                #break

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
                    if newBoard not in self.G_Cost or new_cost < newBoard.G_Cost:
                        newBoard.G_Cost = new_cost
                        priority = new_cost + self.obstruction(won, next)
                        openBoards.put(next, priority)
                        newBoard.parent = currentBoard

                else:
                    # if it isn't in the open board yet
                    newBoard.G_Cost = currentBoard.G_Cost + currentBoard.cost(newBoard)
                    newBoard.H_Cost = self.obstruction(newBoard, won)

                    # set the parent to our currentBoard item
                    newBoard.parent = currentBoard

                    # add it to the queue
                    newBoard = openBoards.get()

            # move the item from the queue and add to the closed set
            currentBoard = openBoards.empty()
            closedBoards.add(currentBoard)

            # resulting costs of moves
            #return self.parent, self.G_Cost
            raise ValueError('No Path Found')

        # recount the path of all moves
        def reconstruct_path(G_Cost, start, won):
            currentBoard = won
            path = []
            while currentBoard != start:
                path.append(currentBoard)
                currentBoard = self.G_Cost[currentBoard]
            # path.append(start)
            # path.reverse()
            return path