# Algorithms
You can find these algorithms in this file:
## RandomSolver.py
This algorithm takes a random car and selects a random move that's possible. It'll keep doing this untill the game is won. We don't use an archive to prevent loops, but we keep track of the moves and find the shortest path afterwards.
## breadthfirst.py
This algorithm looks at all possible moves on a board and constructs all boards after this move. It repeats this process untill it finds a boards that has won. This way it'll always find the shortest solution for a beginstate.
## Astar.py
This algorithm works just like **breadth first**, with a small difference. That difference is the use of **heuristics**. In stead of looking at all next boards, it also calculates a score which determines the order of the boards you are looking at.

There is one thing to note here: used heuristics must be **admissible**, which means the heuristic doesn't influence the solution, but only the time in which it's found. Luckily we made one heuristic from which we can prove it's admissibility. This heuristic is called **heuristic4** or **Estimate moves to solution by amount of cars blocking the goal** (a very creative name). This heuristic (with all others) can be found in the file **rushHour.py** in the directory "code/classes". Using nonadmissible heuristics will officially make it a **Best First algorithm** that just looks like a Astar.
## branchBound.py
This algorithm also looks at all possible moves on a board and constructs all boards after this move, but after that it focusses on one of these boards instead of all of them. He repeats this process for the next board, the one after that, etc. In other words, it's going *depth first* instead of *breadth first*. To prevent going to deep it sets a upperbound with the **random algorithm** which he may nog pass. To try an make this process a little faster it sorts the order of boards to look at with heuristics. For this algorithm nonadmissible heuristics are viable.
