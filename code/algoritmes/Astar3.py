import rushHour as r
import BruteForce as bf
import queue as Qu

class aStar(r.RushHour):

    def __init__(self, board):

        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.closedBoards = set()
        self.tempOpenBoards = []
        self.openBoards = Qu.PriorityQueue()
        self.moves = dict()
        self.count = 0
        self.Gcost = {}
        game = bf.BruteForce(self.currentBoard)
        x, y, self.endState = game.solver(True)


    def aStarSolve(self):

        self.openBoards.put((0, self.currentBoard))
        self.tempOpenBoards.append(self.currentBoard)

        self.moves[self.currentBoard] = ()

        while not self.openBoards.empty():

            self.currentBoard = self.openBoards.get()[1]
            self.tempOpenBoards.remove(self.currentBoard)
            self.Gcost[self.currentBoard] = 0

            #self.closedBoards.add(self.currentBoard)

            self.currentVehicles = self.getVehicles(self.currentBoard)

            if self.won(self.currentVehicles):
                print("won:", self.currentBoard)
                break

            #self.count += 1

            for (newBoard, move) in self.getSucessors():
                if newBoard in self.closedBoards:
                    continue

                if not newBoard in self.tempOpenBoards:
                    self.moves[newBoard] = (self.currentBoard, move)
                    self.tempOpenBoards.append(newBoard)

                    cost = self.Gcost[self.currentBoard] + 1
                    self.Gcost[newBoard] = (cost)

                    score = cost + self.heuristic(newBoard)

                    self.openBoards.put((1, newBoard))

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

        score = self.heuristic2(board)
        return score


    def heuristic1 (self, board):
        """Afstand van punten naar uitgang"""

        score = 0
        for i in range(self.size*self.size):
            if board[i] == ".":
                # add x difference
                score += self.size - i % self.size
                # add y difference
                score += abs(1 - i // self.size)
        return score/100

    def heuristic2 (self, board):

        score = 0

        goalVehicles = self.getVehicles(self.endState)
        vehicles = self.getVehicles(board)

        for vehicle in vehicles:
            for goalVehicle in goalVehicles:
                if vehicle.name == goalVehicle.name:
                    score -= abs(vehicle.dominantCoordinate() - goalVehicle.dominantCoordinate())
        return score
