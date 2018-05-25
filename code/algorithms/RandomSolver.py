"""
breadthFirst.py: An implementation of a breadth first search algorithm.

This implementation uses random moves to solve
a rush hour puzzle.
"""

import rushHour as r
import random
import math

class RandomSolve(r.RushHour):
    """
    A random algorithm for Rush Hour.

    Attributes:
    currentBoard    -- string representation of board
    currentVehicles -- vehicles of current board
    count           -- amount of moves made to solve puzzle
    carX            -- goal car of puzzle
    """

    def __init__(self, board):
        """
        Initialise model for the random solver.

        Arguments:
        board -- representation of rush hour board
        """
        # model for game
        r.RushHour.__init__(self, board)
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles
        self.count = 0
        self.carX = self.getCar(self.currentVehicles, "X")
        self.moves[self.currentBoard] = ()


    def solver(self):
        """
        Get a solution by making random moves of random vehicles.

        By saving only the first route to each state, it is
        guaranteed that every unique board state is gone through once
        in the solution.

        Returns the amount of moves to solve randomly, the amount of unique moves
        and the solved state of the board.
        """
        lastCar = None
        while not self.won(self.currentVehicles):

            #initialise search
            board = self.currentBoard
            car = random.choice(self.vehicles)

            # search moves for selected car
            possibleMoves = self.searchMoves(self.currentBoard,car)
            if possibleMoves:

                # make random move
                move = random.choice(possibleMoves)
                # keep track of moves
                self.count += 1
                # update current board
                self.currentBoard = self.makingMove(self.currentVehicles,car, move)

                # memorize moves made
                if self.currentBoard not in self.moves:
                    self.moves[self.currentBoard] = board

                # stop if puzzle is solved
                if self.won(self.currentVehicles):
                    break

        # remove repetitive moves
        moveList = self.showMoves(self.currentBoard, self.moves)
        return self.count, len(moveList) + 1, self.currentBoard
