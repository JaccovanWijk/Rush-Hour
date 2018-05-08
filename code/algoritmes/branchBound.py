import rushHour as r
import BruteForce as bf

class BranchBound(r.RushHour):

    def __init__(self,board):

        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.moves = []
        self.moveSum = 0
        self.openBoards = []
        self.closedBoards = set()


    def branchBoundSolve(self, amount):

        # find upperbound by random solver
        upperBound = self.RandomSolve(self.currentBoard)

        for i in range(amount):

            print("U", upperBound)

            self.__init__(self.initBoard)

            # initialise search
            self.openBoards.append(self.currentBoard)
            while self.openBoards:
                self.currentBoard = self.openBoards[-1]

                #print(self.moveSum)
                # if current branch is too big
                if self.moveSum >= upperBound:
                    self.moveSum -= 1
                    self.openBoards.pop()
                    continue
                #print("hoi", self.moveSum)
                # update cars
                self.currentVehicles = self.getVehicles(self.currentBoard)

                # stop if puzzle is solved
                if self.won(self.currentVehicles):
                    #return self.showMoves(self.currentBoard, moves)
                    upperBound = self.moveSum
                    print("win")
                    break

                self.closedBoards.add(currentBoard)

                for (newBoard, move) in self.getSucessors():

                    # board is already processed
                    #if newBoard in closedBoards:
                        #continue

                    # if board isn't already in queue
                    if not newBoard in self.openBoards:
                        # add move to movesum
                        self.moveSum += 1

                        # add new board state to open boards
                        self.openBoards.append(newBoard)

                # finish processing current board
                self.closedBoards.add(self.currentBoard)

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
        movemin = 100000
        for j in range(10):
            game = bf.BruteForce(board)
            amount, move = game.solver()
            if move < movemin:
                movemin = move
        return movemin
