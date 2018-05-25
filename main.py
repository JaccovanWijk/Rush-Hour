"""
main.py: Makes a GUI for the algorithms.

This module makes it easier for the user to use
the algorithms of choice on boards of their choice,
this is done by generating a GUI with choices.
"""
import os, sys
import tkinter as tk
from tkinter import ttk
from time import time

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# import shit
import rushHour as r
import Astar as A
import breadthFirst as br
import RandomSolver as rs
import branchBound as bb

currentAlgorithm = ["branchbound"]
currentGame = ["VisBoard"]
currentAmount = [1]
currentHeuristics = [[]]
solution = [0]

class windows(tk.Tk):
    """ Creates window """
    def __init__(self, *args, **kwargs):

        # initialise and custimize window
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="images\icon.ico")
        tk.Tk.wm_title(self, "Rush Hour")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # determine size of window
        for F in (GamePage, AlgorithmPage, AmountPage, HeuristicsPage,
                  ProgressPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AlgorithmPage, currentAlgorithm, currentGame,
        currentAmount, currentHeuristics)

    def show_frame(self, cont, algorithm, game, amount, heuristics):
        """ Show frame and update info """

        currentAlgorithm.append(algorithm)
        currentGame.append(game)
        currentAmount.append(amount)
        currentHeuristics.append(heuristics)

        frame = self.frames[cont]
        frame.tkraise()

class AlgorithmPage(tk.Frame):
    """ Creates window to show buttons to choose algorithms. """

    def __init__(self, parent, controller):
        """ Sets text and buttons into frame """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Which algorithm would you like to use?")
        label.pack(pady=5, padx=5)

        # make random algorithm button
        self.randomButton = ttk.Button(self, text="Random Algorithm",
        command=lambda: controller.show_frame(GamePage, "random", currentGame,
        currentAmount, currentHeuristics))

        self.randomButton.pack(pady=5, padx=5)

        # make breadth first button
        self.BreadthFirstAlg = ttk.Button(self, text="Breadth First Algorithm",
        command=lambda: controller.show_frame(GamePage, "breadthfirst",
        currentGame, currentAmount, currentHeuristics))

        self.BreadthFirstAlg.pack(pady=5, padx=5)

        # make astar button
        self.AstarAlg = ttk.Button(self, text="A* Algorithm",
        command=lambda: controller.show_frame(GamePage, "astar",
        currentGame, currentAmount, currentHeuristics))

        self.AstarAlg.pack(pady=5, padx=5)

        # make branch and bound button
        self.BranchBoundAlg = ttk.Button(self, text="Branch and Bound Algorithm",
        command=lambda: controller.show_frame(GamePage, "branchbound",
        currentGame, currentAmount, currentHeuristics))

        self.BranchBoundAlg.pack(pady=5, padx=5)

class GamePage(tk.Frame):
    """ Creates window to create buttons to ask the amount of games. """

    def __init__(self, parent, controller):
        """ Sets text and buttons """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What board do you want to solve?")
        label.pack(pady=5, padx=5)

        label1 = tk.Label(self, text="6 x 6:")
        label1.pack(pady=5, padx=5)

        # Game 1 button
        self.Game1Button = ttk.Button(self, text="Game 1",
        command=lambda: self.nextPage("Game 1", controller))

        self.Game1Button.pack(pady=5, padx=5)

        # Game 2 button
        self.Game2Button = ttk.Button(self, text="Game 2",
        command=lambda: self.nextPage("Game 2", controller))

        self.Game2Button.pack(pady=5, padx=5)

        # Game 3 button
        self.Game3Button = ttk.Button(self, text="Game 3",
        command=lambda: self.nextPage("Game 3", controller))

        self.Game3Button.pack(pady=5, padx=5)


        label2 = tk.Label(self, text="9 x 9:")
        label2.pack(pady=5, padx=5)

        # Game 4 button
        self.Game4Button = ttk.Button(self, text="Game 4",
        command=lambda: self.nextPage("Game 4", controller))

        self.Game4Button.pack(pady=5, padx=5)

        # Game 5 button
        self.Game5Button = ttk.Button(self, text="Game 5",
        command=lambda: self.nextPage("Game 5", controller))

        self.Game5Button.pack(pady=5, padx=5)

        # Game 6 button
        self.Game6Button = ttk.Button(self, text="Game 6",
        command=lambda: self.nextPage("Game 6", controller))

        self.Game6Button.pack(pady=5, padx=5)

        label3 = tk.Label(self, text="12 x 12:")
        label3.pack(pady=5, padx=5)

        # Game 7 button
        self.Game7Button = ttk.Button(self, text="Game 7",
        command=lambda: self.nextPage("Game 7", controller))

        self.Game7Button.pack(pady=5, padx=5)

    def nextPage(self, game, controller):
        """ Finds next page to show. """
        if currentAlgorithm[-1] == "astar" or currentAlgorithm[-1] == "branchbound":
            controller.show_frame(HeuristicsPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)
        elif currentAlgorithm[-1] == "breadthfirst":
            currentGame.append(game)
            controller.show_frame(ProgressPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)
        else:
            controller.show_frame(AmountPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)

class HeuristicsPage(tk.Frame):
    """ Creates window to show heuristics. """

    def __init__(self, parent, controller):
        """ Sets checkboxes for heuristics. """
        if currentAlgorithm[-1] == "random" or currentAlgorithm[-1] == "breadthfirst":
            controller.show_frame(AmountPage, currentAlgorithm[-1],
            currentGame[-1], currentAmount[-1], currentHeuristics[-1])
        else:
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="What heuristics do you want to use?")
            label.pack(pady=5, padx=5)

            # create checkbutton heuristic1
            var1 = tk.IntVar()
            self.checkBox1 = tk.Checkbutton(self, text="Average distance empty "+
            "spot to exit (could be admissible)", variable=var1)
            self.checkBox1.pack(pady=5, padx=5)

            # create checkbutton heuristic2
            var2 = tk.IntVar()
            self.checkBox2 = tk.Checkbutton(self, text="Average difference" +
            " position cars with a solution (could be admissible)",
            variable=var2)
            self.checkBox2.pack(pady=5, padx=5)

            # create checkbutton heuristic3
            var3 = tk.IntVar()
            self.checkBox3 = tk.Checkbutton(self, text="Amount of cars blocking"+
            " the red car (not admissible)", variable=var3)
            self.checkBox3.pack(pady=5, padx=5)

            # create checkbutton heuristic4
            var4 = tk.IntVar()
            self.checkBox4 = tk.Checkbutton(self, text="Lowerbound for the " +
            "amount of moves left (admissible)", variable=var4)
            self.checkBox4.pack(pady=5, padx=5)

            self.submitButton = ttk.Button(self, text="Submit",
            command=lambda: self.checkboxCheck([var1.get(),
            var2.get(), var3.get(), var4.get()], controller))
            self.submitButton.pack(pady=5, padx=5)

    def nextPage(self, heuristics, controller):
        """ Finds next page to show. """
        if currentAlgorithm[-1] == "branchbound":
            controller.show_frame(AmountPage, currentAlgorithm[-1],
            currentGame[-1], currentAmount[-1], heuristics)
        else:
            controller.show_frame(ProgressPage, currentAlgorithm[-1],
            currentGame[-1], currentAmount[-1], heuristics)


    def checkboxCheck(self, checkboxes, controller):
        """ Checks which checkboxes are checked. """
        heuristics = []
        for i in range(len(checkboxes)):
            if checkboxes[i] == 1:
                string = "heuristic" + str(i + 1)
                heuristics.append(string)
        self.nextPage(heuristics, controller)

class AmountPage(tk.Frame):
    """ Creates window to ask the amount of iterations. """

    def __init__(self, parent, controller):
        """ Sets buttons for the amount of iterations. """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="How many times do you want to run it?")
        label.pack(pady=5, padx=5)

        self.amount1Button = ttk.Button(self, text="1 time",
        command=lambda: self.setAmount(1, controller))
        self.amount1Button.pack(pady=5, padx=5)

        self.amount10Button = ttk.Button(self, text="10 times",
        command=lambda: self.setAmount(10, controller))
        self.amount10Button.pack(pady=5, padx=5)

        self.amount100Button = ttk.Button(self, text="100 times",
        command=lambda: self.setAmount(100, controller))
        self.amount100Button.pack(pady=5, padx=5)

        self.amount1000Button = ttk.Button(self, text="1000 times",
        command=lambda: self.setAmount(1000, controller))
        self.amount1000Button.pack(pady=5, padx=5)

    def setAmount(self, amount, controller):

        controller.show_frame(ProgressPage, currentAlgorithm[-1], currentGame[-1], amount, currentHeuristics[-1])

class ProgressPage(tk.Frame):
    """ Creates window where the user can start running the code. """

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="After pressing the button, please " +
        "wait a few seconds. The terminal will display whats's next.")
        label.pack(pady=5, padx=5)

        self.runButton = ttk.Button(self, text="Press to run!",
        command=lambda: self.quit())
        self.runButton.pack(pady=5, padx=5)
        # controller.show_frame(ShowPage, currentAlgorithm[-1], currentGame[-1], currentAmount[-1], currentHeuristics[-1])

def main():

    app = windows()
    app.mainloop()


    location = "data/Boards/" + currentGame[-1]

    f = open(location, "r")
    board = f.read()
    f.close()
    solution = []

    if currentAlgorithm[-1] == "random":

        runRandom(board)

    elif currentAlgorithm[-1] == "breadthfirst":

        start_time = time()
        game = br.BreadthFirst(board)
        print("Shortest amount of moves possible: ", len(game.solver()[0]),
        ". Found in", time() - start_time, " seconds.",sep='')

    elif currentAlgorithm[-1] == "astar":

        game = A.AStar(board)
        print("Solution found by Astar:", game.solver(currentHeuristics[-1]))

    else:

        runBranchAndBound(board)


def runRandom(board):

    # run random and check for max and min
    allMoves = []
    maxMove = 0
    minMove = 1000000
    for i in range(currentAmount[-1]):
        game = rs.RandomSolve(board)
        move = game.solver()[1]
        allMoves.append(move)
        if move > maxMove:
           maxMove = move
        if move < minMove:
           minMove = move
        # show user how much times it's run
        print(str(i + 1) + "/" + str(currentAmount[-1]))

    if len(allMoves) > 1:
        # plot results
        bins = [minMove+x*(maxMove-minMove) /10 for x in range(11)]

        plt.hist(allMoves, bins, rwidth=0.8)

        plt.xlabel('Amount of moves')
        plt.ylabel('Amount of games')
        plt.title('Distribution of moves by random algorithm')
        plt.show()

    else:
        print("Solved " + str(currentGame[-1]) + " in " + str(allMoves[0]) +
        " moves.")

def runBranchAndBound(board):

    game = bb.BranchBound(board)
    upperbound, upperbounds, totalTime, times = game.solver(currentAmount[-1],
    currentHeuristics[-1])

    if len(times) > 1:
        plt.plot(upperbounds, times)
        plt.gca().invert_xaxis()
        plt.xlabel('Upper bounds')
        plt.ylabel('Time in seconds')
        plt.title('Time in which branch and bound finds a new upperbound')

        plt.show()
    else:
        print("New upperbound found is " + str(upperbound) + " moves.")


if __name__ == "__main__":
    main()
