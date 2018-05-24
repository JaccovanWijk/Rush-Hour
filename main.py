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

currentAlgorithm = ""
amount = 0

class Application(Frame):
    def nextPage(self, algorithm):
        currentAlgorithm = algorithm
        self.quit

    def createWidgets(self):
        # make text
        self.welcome = Label(self, text="Which algorithm would you like to use?")
        self.welcome.pack()

        # make random algorithm button
        self.randomAlg = Button(self)
        self.randomAlg["text"] = "Random Algorithm",
        self.randomAlg["command"] = lambda: self.nextPage("Random")

        self.randomAlg.pack(pady=5)

        # make breadth first button
        self.BreadthFirstAlg = Button(self)
        self.BreadthFirstAlg["text"] = "Breadth First Algorithm",
        self.BreadthFirstAlg["command"] = lambda: self.nextPage("BreadthFirst")

        self.BreadthFirstAlg.pack(pady=5)

        # make astar button
        self.AstarAlg = Button(self)
        self.AstarAlg["text"] = "Astar Algorithm",
        self.AstarAlg["command"] = lambda: self.nextPage("Astar")

        self.AstarAlg.pack(pady=5)

        # make branch and bound button
        self.BranchBoundAlg = Button(self)
        self.BranchBoundAlg["text"] = "Branch and Bound Algorithm",
        self.BranchBoundAlg["command"] = lambda: self.nextPage("BranchandBound")

        self.BranchBoundAlg.pack(pady=5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.label = Label(self, text="Menu")
        self.pack()
        self.createWidgets()

def printer(message):
    print(message)

class AmountPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="Menu")
        self.pack()


def main():

    root = Tk()
    app = Application(root)
    app.mainloop()
    root.destroy()

    print(currentAlgorithm)

    root = Tk()
    app = AmountPage(root)
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
