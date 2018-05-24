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


    def aStarSolve(self):

        # initialise search
        self.priorityQueue.put((0, self.currentBoard))
        self.openBoards.append(self.currentBoard)
        self.moves[self.currentBoard] = ()
        self.Gcost[self.currentBoard] = 0

        while not self.priorityQueue.empty():

            # update constants
            self.currentBoard = self.priorityQueue.get()[1]
            self.openBoards.remove(self.currentBoard)

            #self.closedBoards.add(self.currentBoard)

            self.currentVehicles = self.getVehicles(self.currentBoard)

            if self.won(self.currentVehicles):
                print("won:", self.currentBoard)
                break

            #self.count += 1

            for (newBoard, move) in self.getSucessors():
                if newBoard in self.closedBoards:
                    continue

                if not newBoard in self.openBoards:
                    self.moves[newBoard] = (self.currentBoard, move)
                    self.openBoards.append(newBoard)

                    cost = self.Gcost[self.currentBoard] + 1
                    self.Gcost[newBoard] = (cost)

                    score = cost #+ self.heuristic(newBoard)

                    self.priorityQueue.put((score, newBoard))

            self.closedBoards.add(self.currentBoard)
        print(self.showMoves(self.currentBoard, self.moves))
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

        score = self.heuristic2(board, self.endState)
        return score



#state > children > inside queue
#get from queue, check if closed, if not make children, put children in closedboard
#best possible random endstate?
#pay attention to cars
#what happens when?
