
class vehicle:

    def __init__(self, name, xBegin, yBegin, length, orientation):

        self.name = name
        self.xBegin = xBegin
        self.yBegin = yBegin
        self.length = length
        self.orientation = orientation

    # move orientation coord plus or minus 1
    def move(self, direction):

        if self.orientation == 'H':
            self.xBegin + direction
        elif self.orientation == 'V':
            self.yBegin + direction