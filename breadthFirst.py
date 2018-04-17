import rushHour as r
import Queue

class breadthFirst(r.rushHour):

    def __init__(self,board,size):

        r.rushHour.__init__(self,board,size)

    def breadthFirstSearch(self):

        # open possibilities
        openBoards = Queue()
        # closed possibilities
        closedBoards = set()
        # moves done
        moves = dict()


        # initialise search
        openBoards.enqueue([self.initBoard, self.vehicles])
        moves[self.initBoard] = (None, None)

        while not openBoards.is_empty():

            currentBoard = openBoards.dequeue()

            # bepaal alle zetten en resulterende borden