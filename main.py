import os, sys
from tkinter import *
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# import shit
import rushHour as r
import Astar as A
import breadthFirst as br
import BruteForce as bf

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def main():

    root = Tk()
    app = Application(root)
    app.mainloop()
    root.destroy()

    # f = open("data/Boards/Game 1", "r")
    # board = f.read()
    # f.close()
    #
    # moves = 0
    # for i in range(10):
    #     game = bf.BruteForce(board)
    #     moves += game.solver()[1]
    # print(moves/10)


if __name__ == "__main__":
    main()
    print("HOi")
