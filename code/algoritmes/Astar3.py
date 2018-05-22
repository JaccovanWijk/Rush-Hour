import rushHour as r
import BruteForce as bf
import queue

class aStar(r.RushHour):

    def __init__(self, board):

        r.RushHour.__init__(self, board)
        self.currentBoard = board
        self.openBoards = set()
        self.closedBoards = set()
        self.queue =

    def solver(self)





class PriorityQueue(Queue.Queue):

    def _insert(self, item):
        board, score = item
        self.place((board, score))

    def _get(self):
        return self.queue.pop(0)[1]

    def place(self, item):
        openBoards = self.queue
        low = 0
        high = len(openBoards)

        while low < high:
            mid = (low+high)/2
            if item[0] < openBoards[mid][0]:
                high = mid
            else:
                low = mid + 1
        openBoards.insert(low, item)
