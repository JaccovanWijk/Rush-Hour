import rushHour as r

game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)

def solve(vehicle):

    game.testHistory.append(vehicle)
    print(game.initBoard)

    direction = vehicle.orientation
    if direction == "H":
        # pick everything in it's row
        possibleDrive = game.initBoard[vehicle.yBegin - 1]
    elif direction == "V":
        # pick everything in it's column
        possibleDrive = game.initBoard[vehicle.xBegin::game.size]

    moved = 0
    while moved < 3:#not game.won():
        moved +=1

        # keep track of position relative to goalcar
        afterGoal = False
        for letter in possibleDrive:
            if letter == vehicle.name:
                afterGoal = True
            elif letter == ".":
                if afterGoal:
                    begin = [vehicle.xBegin,vehicle.yBegin]
                    vehicle.moveHistory.append(begin)
                    game.makingMove(1, vehicle.name)
            else:
                # if there's a car in front move it
                for car in game.vehicles:
                    if car.name == letter and afterGoal:
                        solve(car)

                begin = [vehicle.xBegin,vehicle.yBegin]
                vehicle.moveHistory.append(begin)
                game.makingMove(1, vehicle.name)
    print(game.initBoard)

def solver(vehicle):

    game.testHistory.append(vehicle)

    print(vehicle)
    drive(vehicle)
    print(vehicle)


def drive(vehicle):

    orientation = vehicle.orientation
    if orientation == "H":
        # pick everything in it's row
        possibleDrive = game.initBoard[vehicle.yBegin - 1]

        if possibleDrive[vehicle.xBegin - 1 + vehicle.length] == "." and vehicle.xBegin != vehicle.moveHistory[-1]:
            vehicle.move(1)
            drive(vehicle)
        elif possibleDrive[vehicle.xBegin - 1 + vehicle.length] == "." and vehicle.xBegin != vehicle.moveHistory[-1]:
            vehicle.move(1)
            drive(vehicle)
        else:
            return -1

    elif orientation == "V":
        # pick everything in it's column
        possibleDrive = game.initBoard[vehicle.xBegin::game.size]

        if possibleDrive[vehicle.yBegin - 1 + vehicle.length] == "." and vehicle.yBegin != vehicle.moveHistory[-1]:
            vehicle.move(1)
            drive(vehicle)
        elif possibleDrive[vehicle.yBegin - 1 + vehicle.length] == "." and vehicle.yBegin != vehicle.moveHistory[-1]:
            vehicle.move(1)
            drive(vehicle)
        else:
            return -1


# find goalcar and start solving
for vehicle in game.vehicles:
    if vehicle.name == "X":
        goalCar = vehicle
solver(goalCar)