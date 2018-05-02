import rushHour as r
import BruteForce as bf

class BranchBound(r.RushHour):

    def __init__(self,board,size):

        r.RushHour.__init__(self, board, size)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.moves = []
        self.moveCount = []
        self.moveSum = 0


    def branchBoundSolve(self, amount):

        # find upperbound by random solver
        upperBound = self.RandomSolve(self.currentBoard)

        moves = None

        for i in range(amount):

            print(upperBound)
            # open possibilities
            openBoards = []
            # closed possibilities
            closedBoards = set()
            # moves done
            moves = dict()

            self.currentBoard = self.initBoard
            self.currentVehicles = self.vehicles
            self.moveSum = 0
            self.moveCount = []
            self.moves = []

            # initialise search
            openBoards.append(self.currentBoard)
            moves[self.currentBoard] = ()
            while openBoards:

                self.currentBoard = openBoards.pop()

                # if current branch is too big
                if self.moveSum > upperBound:
                    self.moveSum -= moveCount.pop()
                    continue

                # update cars
                self.currentVehicles = self.getVehicles(self.currentBoard)

                # stop if puzzle is solved
                if self.won(self.currentVehicles):
                    #return self.showMoves(self.currentBoard, moves)
                    upperBound = self.moveSum
                    print(upperBound)
                    break

                for (newBoard, move) in self.getSucessors():

                    # board is already processed
                    if newBoard in closedBoards:
                        continue

                    # if board isn't already in queue
                    if not newBoard in openBoards:
                        # add move to moves
                        moves[newBoard] = (self.currentBoard, move)
                        self.moveCount.append(move)
                        self.moveSum += abs(move)

                        # add new board state to open boards
                        openBoards.append(newBoard)

                # finish processing current board
                closedBoards.add(self.currentBoard)

        return upperBound

    def getSucessors(self):
        """Get next board states reachable by making one move"""
        sucessors = []
        cars = self.currentVehicles

        # get all moves of all vehicles
        for vehicle in self.currentVehicles:
            for i in self.searchMoves(self.currentBoard, vehicle):
                # determine new state
                newBoard = self.makingMove(self.currentVehicles,vehicle, i)
                self.makingMove(self.currentVehicles,vehicle, -i)

                sucessors.append([newBoard, i])

        return sucessors

    def RandomSolve(self, board):

        # bruteForce 10 times
        moves = 0
        for j in range(10):
            game = bf.BruteForce(board, self.size)
            moves += game.solver()
        return int(moves/10)
