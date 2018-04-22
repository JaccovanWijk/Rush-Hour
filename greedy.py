import rushHour as r

class greedy(r.rushHour):
    
    def __init__(self, board):
        
        r.rushHour.__init__(board)
        
        
    def solve(self, board):
        
        print(self.initBoard)
        for car in self.vehicles:
                if car.name == "X":
                    currentCar = car
    
        goalVehicles = []
        testedVehicles = []
        move = 0
        while move < 3:#not self.won():
            
            # zorg dat deze de maximale moves naar beide kanten wordt
            possibleMoves = self.searchMoves(currentCar)
            x = max(s for s in possibleMoves)
            y = min(s for s in possibleMoves)
            moves = [x,y]
            
            if currentCar not in testedVehicles:
                goalVehicles.append(currentCar)
                testedVehicles.append(currentCar)
                
            if len(moves) == 0:
                
                neighbours = self.neighboursFinder(currentCar)
                
                currentCar = neighbours[0]
                
                #currentCar = goalVehicles[-2]
                #goalVehicles.pop()
            elif len(moves) == 1:
                
            
            else:
                # take first argument of moves
                self.makingMove(currentCar,moves[0])
                

            move += 1
        print(self.initBoard)
        
        
    def neighboursFinder(self, vehicle):
    
        possibleDrive = self.driveline(vehicle)
        
        neighbours = []
        length = len(possibleDrive)
        for i in range(length):
            if possibleDrive[i] == vehicle.name:
                if i != length - 1 and possibleDrive[i + length] != ".":
                    neighbours.append(possibleDrive[i + length])
                if i != 0 and possibleDrive[i - 1] != ".":
                    neighbours.append(possibleDrive[i - 1])
                    
        # find car for neighbours name
        neighbourCars = []
        for car in neighbours:
            for vehicle in self.vehicles:
                if car == vehicle.name:
                    neighbourCars.append(vehicle)
            
        return neighbourCars        
        

            
        
        
        
        
        
        