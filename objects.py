# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:07:24 2018

@author: Jacco
"""
# NOG GEEN GOEDE MANIER GEVONDEN OM AAN TE GEVEN IN "cars" OF HET DE RODE AUTO IS, MAAR WE WETEN OOK NOG NIET HOE WE HEM MOETEN INLADEN;)

class Board:
    #lijst van lijst met coordinaten van autos er in gooien (heet cars)
    def __init__(self, size, cars):
        self.board = [[0 for x in range(size)] for y in range(size)]

        # fill board with cars
        for i in range(len(cars)):
            for j in range(cars[i].length):
                if cars[i].vertical:
                    self.board[cars[i].y + j][cars[i].x] = i + 1
                else:
                    self.board[cars[i].y][cars[i].x + j] = i + 1

    def show(self):
        for row in self.board:
            for column in row:
                #print autos, check of het rode auto is
                print (column, end="")
            print ("")


class Car:

    def __init__(self, x, y, length, vertical, red):
        # position of upper or leftmost part
        self.x = x
        self.y = y

        self.length = length
        self.vertical = vertical
        self.red = red