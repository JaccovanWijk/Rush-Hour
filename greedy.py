import rushHour as r

# class greedy(r.rushHour):

#     boardFile = open("Game 1", "r")

#     game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)

#     def solve(self,vehicle):

#         game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)

#         game.testHistory.append(vehicle)
#         print(game.initBoard)

#         direction = vehicle.orientation
#         if direction == "H":
#             # pick everything in it's row
#             possibleDrive = game.initBoard[vehicle.yBegin - 1]
#         elif direction == "V":
#             # pick everything in it's column
#             possibleDrive = game.initBoard[vehicle.xBegin::game.size]

#         moved = 0
#         while moved < 3:#not game.won():
#             moved +=1

#             # keep track of position relative to goalcar
#             afterGoal = False
#             for letter in possibleDrive:
#                 if letter == vehicle.name:
#                     afterGoal = True
#                 elif letter == ".":
#                     if afterGoal:
#                         begin = [vehicle.xBegin,vehicle.yBegin]
#                         vehicle.moveHistory.append(begin)
#                         game.makingMove(1, vehicle.name)
#                 else:
#                     # if there's a car in front move it
#                     for car in game.vehicles:
#                         if car.name == letter and afterGoal:
#                             self.solve(car)

#                     begin = [vehicle.xBegin,vehicle.yBegin]
#                     vehicle.moveHistory.append(begin)
#                     game.makingMove(1, vehicle.name)
#         print(game.initBoard)

#     def solver(self,vehicle):

#         game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)

#         game.testHistory.append(vehicle)

#         print(vehicle)
#         self.drive(vehicle)
#         print(vehicle)


#     def drive(self,vehicle):

#         orientation = vehicle.orientation
#         if orientation == "H":
#             # pick everything in it's row
#             possibleDrive = game.initBoard[vehicle.yBegin - 1]

#             if possibleDrive[vehicle.xBegin - 1 + vehicle.length] == "." and vehicle.xBegin != vehicle.moveHistory[-1]:
#                 vehicle.move(1)
#                 drive(vehicle)
#             elif possibleDrive[vehicle.xBegin - 1 + vehicle.length] == "." and vehicle.xBegin != vehicle.moveHistory[-1]:
#                 vehicle.move(1)
#                 drive(vehicle)
#             else:
#                 return -1

#         elif orientation == "V":
#             # pick everything in it's column
#             possibleDrive = game.initBoard[vehicle.xBegin::game.size]

#             if possibleDrive[vehicle.yBegin - 1 + vehicle.length] == "." and vehicle.yBegin != vehicle.moveHistory[-1]:
#                 vehicle.move(1)
#                 drive(vehicle)
#             elif possibleDrive[vehicle.yBegin - 1 + vehicle.length] == "." and vehicle.yBegin != vehicle.moveHistory[-1]:
#                 vehicle.move(1)
#                 drive(vehicle)
#             else:
#                 return -1

class greedy(r.rushHour):
    
    def __init__(self, board):
        
        r.rushHour.__init__(board)
        
        
    def solve(self, board):
    
        for car in self.vehicles:
                if car.name == "X":
                    newCar = car
    
        goalVehicles = []
    
        while not self.won():
            
            directions = self.pref(newCar)
            
            if newCar not in goalVehicles:
                goalVehicles.append(newCar)
                currentCar = newCar
            else:
                if len(self.neighbours(newCar)) < 2:
                    currentCar = goalVehicles[-2]
                else:
                    # move to other option

        
    def pref(self, vehicle):
        
        possibleDrive = self.driveline(vehicle)
        directions = []
        if possibleDrive[0] == vehicle.name:
            return 1
        elif possibleDrive[-1] == vehicle.name:
            return -1
        else:
            # Pas hier verschillende heuristieken toe
            return 1
        
        
    def neighboursFinder(self, vehicle):
    
        possibleDrive = self.driveline(vehicle)
        
        neighbours = []
        length = len(possibleDrive)
        for i in range(length):
            if possibleDrive[i] == vehicle.name:
                if i != length - 1:
                    neighbours.append(possibleDrive[i + length])
                if i != 0:
                    neighbours.append(possibleDrive[i - 1])
        return neighbours        
        
    def nextMove(self, vehicle, directions):
        
        possibleMoves = self.searchMoves(vehicle)
        
        if len(possibleMoves) == 0:
            # Choose a car
        elif len(possibleMoves) == 1:
            
        
        
        
        
        
        