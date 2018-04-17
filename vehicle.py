
class vehicle:

    def __init__(self, name, xBegin, yBegin, length, orientation):

        self.name = name
        self.xBegin = xBegin
        self.yBegin = yBegin
        self.length = length
        self.orientation = orientation
        self.moveHistory = []

    # move orientation coord plus or minus 1
    def move(self, direction):

        if self.orientation == 'H':
            self.xBegin + direction
            self.moveHistory.append(self.xBegin)
        elif self.orientation == 'V':
            self.yBegin + direction
            self.moveHistory.append(self.yBegin)