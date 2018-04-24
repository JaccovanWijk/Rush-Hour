
class vehicle:

    def __init__(self, name, xBegin, yBegin, length, orientation):

        self.name = name
        self.xBegin = xBegin
        self.yBegin = yBegin
        self.length = length
        self.orientation = orientation

    def dominantCoordinate(self):
        if self.orientation == 'H':
            return self.xBegin
        elif self.orientation == 'V':
            return self.yBegin

    # move orientation coord plus or minus 1
    def move(self, direction):

        if self.orientation == 'H':
            self.xBegin = self.xBegin + direction
        elif self.orientation == 'V':
            self.yBegin = self.yBegin + direction