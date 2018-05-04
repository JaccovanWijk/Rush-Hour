
import rushHour as r
import vehicle as v
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

    def __init__(self, board, point):

        r.rushHour.__init__(self,board)

        self.board = board
        self.point = point
        self.parent = None

        # cost of path from start to end-nodes
        self.G_Cost = {}

        # estimated cost of the cheapest path to goal
        self.H_Cost = {}

    def children(self, point):
        """Get next board states reachable by making one move"""
        children = []
        cars = self.vehicles

        # get all moves of all vehicles
        for vehicle in self.vehicles:
            for i in self.searchMoves(vehicle):
                # determine new state
                newBoard = self.makingMove(vehicle, i)
                self.makingMove(vehicle, -i)
                # make move string
                move = vehicle.name + ' ' + str(i)

                children.append([newBoard, move])

        return children

    # heuristic function
    def distance(self, point1, point2):
        (x1, y1) = point1
        (x2, y2) = point2
        return abs(x1 - x2) + abs(y1 - y2)

    def aStar(self, board, start, won):

        # open and closed possibilities
        openBoards = PriorityQueue()
        closedBoards = set()
        # moves done
        moves = dict()

        # initialise search and cost
        self.currentBoard = start
        self.G_Cost[start] = 0

        while not openBoards.empty():
            currentBoard = openBoards.get()
            #newBoard = self.Board()

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is goal is met
            if self.won(self.currentVehicles):
            #if currentBoard == won:
                break

            # loop through the newBoard's children/siblings
            for newBoard in self.children(currentBoard):

                # if it is already in the closed set, skip it
                if newBoard in closedBoards:
                    continue

                # otherwise if it is already in the queue
                if newBoard in self.openBoards:

                    # Check if we beat the cost and update if so.
                    new_cost = currentBoard.G_Cost + board.cost(currentBoard, newBoard)
                    if newBoard not in self.G_Cost or new_cost < newBoard.G_Cost:
                        newBoard.G_Cost = new_cost
                        priority = new_cost + self.distance(won, next)
                        openBoards.put(next, priority)
                        newBoard.parent = currentBoard

                else:
                    # if it isn't in the open board yet
                    newBoard.G_Cost = currentBoard.G_Cost + currentBoard.cost(newBoard)
                    newBoard.H_Cost = self.distance(newBoard, won)

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
