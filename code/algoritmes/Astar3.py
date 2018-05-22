import rushHour as r
import BruteForce as bf
import queue as Qu

class aStar(r.RushHour):

    def __init__(self, board):

        r.RushHour.__init__(self, board)
        self.currentBoard = board
        self.closedBoards = set()
        self.priorityQueue = Qu.PriorityQueue()
        self.moves = dict()
        self.count = 0


    def aStarSolve(self):

        self.priorityQueue.put((self.currentBoard, 0))

        self.moves[self.currentBoard] = ()

        while not self.priorityQueue.empty():

            self.currentBoard = self.priorityQueue.get()
            self.closedBoards.add(self.currentBoard)

            self.currentVehicles = self.getVehicles(self.currentBoard)

            if self.won(self.currentVehicles):
                break

            self.count += 1

            for newBoard in self.getSucessors():

                if newBoard in self.closedBoards:
                    continue

                self.moves[newBoard] = (self.currentBoard)

                score = 0
                self.priorityQueue.put((score, newBoard))



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
                move = vehicle.name + " " + str(i)

                sucessors.append(newBoard)

        return sucessors


# class PriorityQueue(Queue.Queue):
#
#     def _put(self, item):
#         self.place(item)
#
#     def _get(self):
#         return self.queue.pop(0)[1]
#
#     def place(self, item):
#         openBoards = self.queue
#         low = 0
#         high = len(openBoards)
#
#         while low < high:
#             mid = (low+high)/2
#             if item[0] < openBoards[mid][0]:
#                 high = mid
#             else:
#                 low = mid + 1
#         openBoards.insert(low, item)
