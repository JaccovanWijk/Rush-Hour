import rushHour as r
import BruteForce as bf
import breadthFirst as brF
import queue as Qu

class aStar(r.RushHour):

    def __init__(self, board):

        # model game
        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.closedBoards = set()
        self.openBoards = []
        self.priorityQueue = Qu.PriorityQueue()
        self.moves = dict()
        self.count = 0
        self.Gcost = {}
        game = bf.BruteForce(self.currentBoard)
        self.endState = game.solver()[-1]


    def solver(self):

        # initialise search
        self.priorityQueue.put((0, self.currentBoard))
        self.openBoards.append(self.currentBoard)
        self.moves[self.currentBoard] = ()

        # cost of steps from initial to last board
        self.Gcost[self.currentBoard] = 0

        while not self.priorityQueue.empty():

            # update constants
            self.currentBoard = self.priorityQueue.get()[1]
            self.openBoards.remove(self.currentBoard)

            # update cars
            self.currentVehicles = self.getVehicles(self.currentBoard)

            # stop if puzzle is solved
            if self.won(self.currentVehicles):
                print("won:", self.currentBoard)
                break

            for (newBoard, move) in self.getSucessors():

                # board is already processed
                if newBoard in self.closedBoards:
                    continue

                #if board isn't already in priority queue
                if not newBoard in self.openBoards:

                    #add move to moves
                    self.moves[newBoard] = (self.currentBoard, move)

                    # add new board state to open boards
                    self.openBoards.append(newBoard)

                    #calculate the current depth and new G_cost
                    cost = self.Gcost[self.currentBoard] + 1
                    self.Gcost[newBoard] = (cost)

                    #update the queue through the cost and heuristic
                    score = cost + self.heuristic(newBoard)
                    self.priorityQueue.put((score, newBoard))

            # finish processing current board
            self.closedBoards.add(self.currentBoard)

        return len(self.showMoves(self.currentBoard, self.moves))


    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []

        # get all moves of all vehicles
        for vehicle in self.currentVehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles,vehicle, i)
                self.makingMove(self.currentVehicles,vehicle, -i)

                move = vehicle.name + str(i)

                sucessors.append((newBoard, move))

        return sucessors


    def heuristic(self, board):

        score = self.heuristic1(board)
        return score