# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:07:24 2018

@author: Jacco
"""
# NOG GEEN GOEDE MANIER GEVONDEN OM AAN TE GEVEN IN "cars" OF HET DE RODE AUTO IS, MAAR WE WETEN OOK NOG NIET HOE WE HEM MOETEN INLADEN;)

class board(size, cars):
    #lijst van lijst met coordinaten van autos er in gooien (heet cars)
    def __init__(self, size, cars):
        self.emptyboard = [[0 for x in range(size)] for y in range(size)]
        self.board = create(emptyboard, cars)

    #put cars in board
    def create(size, cars):
        for i in cars:
            for j in i:
                if #rode auto:
                    # idk of je board hier al kan aanroepen haha
                    board[i][j] = 2;
                else:
                    board[i][j] = 1

    def __str__(self):
        for row in rows:
            for column in columns:
                #print autos, check of het rode auto is
                if #rode auto:
                    print(|X|, end='')
                else:
                    print(| |, end='')
                print()
        return ""

class car(coordinates):

    def __init__(self, coordinates):
        self.location = coordinates
        self.redcar = redcarcheck()
        self.moved = False
        self.legal = True

    #check if car is the red car
    def redcarcheck():
        if :
            return True
        return False