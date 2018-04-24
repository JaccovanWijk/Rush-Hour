import rushHour as r
import random

class bruteForce(r.rushHour):

    def __init__(self,board):

        r.rushHour.__init__(self,board)

    def solver(self):

        moves = 0
        while not self.won():

            car = random.choice(self.vehicles)

            possibleMoves = self.searchMoves(car)
            if possibleMoves:
                moves += 1
                move = random.choice(possibleMoves)
                self.initBoard = self.makingMove(car, move)
        return moves
