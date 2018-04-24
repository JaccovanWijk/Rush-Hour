# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:26:21 2018

@author: Jacco
"""

import rushHour as r
import greedy as gr

f = open("Boards/Test", "r")
board = f.read()
f.close()

game = gr.greedy(board)

game.solve(board)