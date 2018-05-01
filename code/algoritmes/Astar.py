
import rushHour as r
#from heapq import PriorityQueue (Import wont cooperate?)

class aStar(r.RushHour):

    def __init__(self, value, point):

        r.RushHour.__init__(self,board)

        self.value = value
        self.point = point
        self.parent = None

    #Not yet done converting this to a rush hour board.
    #def children(self, point):
        #(x1, y1) = point
        #(x2, y2) = point2
    #def distance(self, point, point2):
        #return abs(x1 - x2) + abs(y1 - y2)

    def aStar(self, board, start, goal):

        # Open and closed possibilities
        openBoards = set()
        #openBoards = PriorityQueue()
        closedBoards = set()
        #moves = dict()

        # Create the starting point
        current = start
        openBoards.add(current)

        # Set movement values
        self.parent= None

        # Cost of path from start to end-nodes
        self.G_cost = 0

        # Estimated cost of the cheapest path to goal
        self.H_cost = 0

        #while openBoards:

            #if current == goal:
                #break

            #Remove the item from the open set
            #openBoards.remove(current)

            #Add it to the closed set
            #closedBoards.add(current)

            #Loop through the newBoard's children/siblings
            #for newBoard in children(currentd):

                #If it is already in the closed set, skip it
                #if newBoard in closedBoards:
                    #continue

                #Otherwise if it is already in the open set
                #if newBoard in openBoards:

                    #Check if we beat the cost and update if so.
                    #new_cost = current.G_cost + board.G_cost(newBoard)
                    #if newBoard.G_cost > new_cost or newBoard not in cost:
                        #newBoard.G_cost = new_cost
                        #priority = new_cost + children(goal, next)
                        #frontier.put(next, priority)
                        #newBoard.parent = current

                #else:
                    #If it isn't in the open board yet
                    #newBoard.G_cost = current.G_cost + board.G_cost(newBoard)
                    #newBoard.H_cost = distance(newBoard, goal)

                    #Set the parent to our current item
                    #newBoard.parent = current

                    #Add it to the set
                    #openBoards.add(newBoard)

            # Resulting costs of moves
            #return parent, cost
