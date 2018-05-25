"""vehicle.py: A representation of a vehicle in a rush hour game."""

class Vehicle:
    """
    Represents a vehicle of a rush hour game.

    Attributes:
    name        -- character of car in board string
    xBegin      -- x coordinate of upperleft corner
    yBegin      -- y coordinate of upperleft corner
    length      -- length of car
    orientation -- 'H' horizontal, or 'V' vertical
    """

    def __init__(self, name, xBegin, yBegin, length, orientation):
        """Initialise the vehicle."""
        self.name = name
        self.xBegin = xBegin
        self.yBegin = yBegin
        self.length = length
        self.orientation = orientation

    def dominantCoordinate(self):
        """Return the begin coordinate in move direction."""
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
