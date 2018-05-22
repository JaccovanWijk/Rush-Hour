class Vehicle:
    """Represents a vehicle of a rush hour game."""

    def __init__(self, name, xBegin, yBegin, length, orientation):

        self.name = name
        self.xBegin = xBegin
        self.yBegin = yBegin
        self.length = length
        self.orientation = orientation

    def dominantCoordinate(self):
        """Returns the begin coordinate in move direction."""
        if self.orientation == 'H':
            return self.xBegin
        elif self.orientation == 'V':
            return self.yBegin

    def move(self, direction):
        """Move vehicle coordinate by <direction>."""
        if self.orientation == 'H':
            self.xBegin = self.xBegin + direction
        elif self.orientation == 'V':
            self.yBegin = self.yBegin + direction
