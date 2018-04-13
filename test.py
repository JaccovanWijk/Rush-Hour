import rushHour as r

def main():

    game = r.rushHour("AA...OP..Q.OPXXQ.OP..Q..B...CCB.RRR.", 6)
    # solve met rode auto

def solve(car):

    while not game.won():
        row = game.initBoard[2]

        for letter in row:
            # zorg dat hij alleen na de rode kijkt
            if letter != "X" and letter != ".":
                # kijk welke auto het is en gooi die in solve
                for car in game.vehicles:
                    if car.name == letter:
                        solve()
