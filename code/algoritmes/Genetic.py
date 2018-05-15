import rushHour as r

import numpy as np
import random

class Genetic(r.RushHour):
    """A genetic algorithm for Rush Hour"""

    def __init__(self, board, size):

        r.RushHour(self, board, size)

        # model of the game
        self.currentBoard = self.initBoard
        self.currentVehicles = self.vehicles

        # dictionary for value conversions
        symbols = "." + [car.name for car in self.currentVehicles]
        symbolCount = len(symbols)
        self.values = dict()

        for i in range(symbolCount):
            self.values[symbols[i]] = i / symbolCount

        self.currentGen = np.random.uniform(0,1,(100,2,36))

    def convertBoard(self, board):
        """Converts board into an array of floats"""

        # determine car number
        carNumber = self.symbols.length()

        numberBoard = []

        # convert chars to floats
        for char in self.currentBoard:
            numberBoard.append(self.values[char])

        return np.array(numberBoard)

    def solve(self, array):
