import rushHour as r

game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)

def main():

    # find goalcar and start solving
    for vehicle in game.vehicles:
        if vehicle.name == "X":
            goalCar = vehicle
    solve(goalCar)

def solve(vehicle):

    direction = vehicle.orientation
    if direction == "H":
        # pick everything in it's row
        possibleDrive = game.initBoard[vehicle.yBegin - 1]
    elif direction == "V":
        # pick everything in it's column
        possibleDrive = game.initBoard[vehicle.xBegin::game.size]

    moved = 0
    while moved < vehicle.length: #deze voorwaarde moet nog beter

        # keep track of position relative to goalcar
        afterGoal = False
        for letter in possibleDrive:
            if letter == vehicle.name:
                afterGoal = True
            elif letter == ".":
                if afterGoal:
                    # voeg hier nog iets toe aan movehistory
                    vehicle.move(1)
            else:
                # if there's a car in front move it
                for car in game.vehicles:
                    if car.name == letter and afterGoal:
                        solve(car)
                #voeg hier nog iets toe aan movehistory
                vehicle.move(1)