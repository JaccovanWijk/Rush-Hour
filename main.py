import os, sys
import tkinter as tk
from tkinter import ttk
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# import shit
import rushHour as r
import Astar as A
import breadthFirst as br
import BruteForce as bf
import branchBound as bb

currentAlgorithm = [0]
currentGame = [0]
currentAmount = [0]
currentHeuristics = [0]

class windows(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Rush Hour")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GamePage, AlgorithmPage, AmountPage, HeuristicsPage, EndPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AlgorithmPage, currentAlgorithm, currentGame, currentAmount, currentHeuristics)

    def show_frame(self, cont, algorithm, game, amount, heuristics):

        currentAlgorithm.append(algorithm)
        currentGame.append(game)
        currentAmount.append(amount)
        currentHeuristics.append(heuristics)

        frame = self.frames[cont]
        frame.tkraise()

class AlgorithmPage(tk.Frame):

    def __init__(self, parent, controller):

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
        self.AstarAlg = ttk.Button(self, text="Astar Algorithm",
        command=lambda: controller.show_frame(GamePage, "astar",
        currentGame, currentAmount, currentHeuristics))

        self.AstarAlg.pack(pady=5, padx=5)

        # make branch and bound button
        self.BranchBoundAlg = ttk.Button(self, text="Branch and Bound Algorithm",
        command=lambda: controller.show_frame(GamePage, "branchbound",
        currentGame, currentAmount, currentHeuristics))

        self.BranchBoundAlg.pack(pady=5, padx=5)

class GamePage(tk.Frame):

    def __init__(self, parent, controller):

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

        if currentAlgorithm[-1] == "astar" or currentAlgorithm[-1] == "branchbound":
            controller.show_frame(HeuristicsPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)
        elif currentAlgorithm[-1] == "breadthfirst":
            currentGame.append(game)
            controller.show_frame(EndPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)
        else:
            controller.show_frame(AmountPage, currentAlgorithm[-1],
            game, currentAmount, currentHeuristics)

class HeuristicsPage(tk.Frame):

    def __init__(self, parent, controller):

        if currentAlgorithm[-1] == "random" or currentAlgorithm[-1] == "breadthfirst":
            controller.show_frame(AmountPage, currentAlgorithm[-1], currentGame[-1], currentAmount[-1], currentHeuristics[-1])
        else:
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="What heuristics do you want to use?")
            label.pack(pady=5, padx=5)

            var1 = tk.IntVar()
            self.checkBox1 = tk.Checkbutton(self, text="Average distance empty spot to exit (could be admissible)", variable=var1)
            self.checkBox1.pack(pady=5, padx=5)

            var2 = tk.IntVar()
            self.checkBox2 = tk.Checkbutton(self, text="Average difference position cars with a solution (could be admissible)", variable=var2)
            self.checkBox2.pack(pady=5, padx=5)

            var3 = tk.IntVar()
            self.checkBox3 = tk.Checkbutton(self, text="Amount of cars blocking the red car (not admissible)", variable=var3)
            self.checkBox3.pack(pady=5, padx=5)

            self.submitButton = ttk.Button(self, text="Submit",
            command=lambda: self.checkboxCheck([var1.get(),
            var2.get(), var3.get()], controller))
            self.submitButton.pack(pady=5, padx=5)

    def nextPage(self, heuristics, controller):

        if currentAlgorithm[-1] == "branchbound":
            controller.show_frame(AmountPage, currentAlgorithm[-1], currentGame[-1], currentAmount[-1], heuristics)
        else:
            controller.show_frame(EndPage, currentAlgorithm[-1], currentGame[-1], currentAmount[-1], heuristics)


    def checkboxCheck(self, checkboxes, controller):

        heuristics = []
        for i in range(len(checkboxes)):
            if checkboxes[i] == 1:
                string = "heuristic" + str(i + 1)
                heuristics.append(string)
        self.nextPage(heuristics, controller)

class AmountPage(tk.Frame):

    def __init__(self, parent, controller):

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

        controller.show_frame(EndPage, currentAlgorithm[-1], currentGame[-1], amount, currentHeuristics[-1])

class EndPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please wait a moment, then close this window.")
        label.pack(pady=5, padx=5)

        self.quit()

def main():

    app = windows()
    app.mainloop()

    location = "data/Boards/" + currentGame[-1]

    f = open(location, "r")
    board = f.read()
    f.close()

    if currentAlgorithm[-1] == "random":

        moves = 0
        maxmove = 0
        minmove = 1000000
        for i in range(currentAmount[-1]):
            game = bf.BruteForce(board)
            move = game.solver()[1]
            if move > maxmove:
               maxmove = move
            if move < minmove:
               minmove = move
            moves += move
        print("Average amount of moves over", currentAmount[-1], "games:",int(moves/currentAmount[-1]))
        print("Lowest amount of moves over", currentAmount[-1], "games:",minmove)
        print("Highest amount of moves over", currentAmount[-1], "games:",maxmove)

    elif currentAlgorithm[-1] == "breadthfirst":

        game = br.BreadthFirst(board)
        print("Shortest amount of moves possible:", len(game.solver()[0]))

    elif currentAlgorithm[-1] == "astar":

        game = A.aStar(board)
        print("Solution found by Astar:", game.solver(currentHeuristics[-1]))

    else:

        game = bb.BranchBound(board)
        print("Solution found by Branch and Bound:", game.solver(currentAmount[-1], currentHeuristics[-1])[0])


if __name__ == "__main__":
    main()
