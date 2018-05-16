import pygame
import random

# size constant
CAR_SIZE = 500
# color constants
WHITE = (255,255,255)
GREY = (127,127,127)
RED = (255,0,0)

def drawBoard(vehicles, size, huemap, name):
    """Visualises a rush-hour board"""
    # initialise image
    image = pygame.Surface((size * CAR_SIZE, size * CAR_SIZE))
    image.fill(GREY)

    # draw all cars
    for vehicle in vehicles:

        drawRect(image, huemap, vehicle)

        if vehicle.name == 'X':
            drawCross(image, vehicle, 20)

    # save image
    pygame.image.save(image, name + ".png")

def drawCross(image, vehicle, width):
    """Marks a vehicle with a cross"""
    # calculate rectangle bounds
    up = vehicle.yBegin * CAR_SIZE + CAR_SIZE//10 + width//2 - 1
    down = vehicle.yBegin * CAR_SIZE + CAR_SIZE*9//10 - width//2 - 1
    left = vehicle.xBegin * CAR_SIZE + CAR_SIZE//10
    right = (vehicle.xBegin + vehicle.length) * CAR_SIZE - CAR_SIZE//10 - 1

    # draw a cross
    pygame.draw.line(image, WHITE, [left,up], [right,down], width)
    pygame.draw.line(image, WHITE, [right,up], [left,down], width)

def drawRect(image, huemap, vehicle):
    """Draws a rectangle to represent the vehicle"""
    rect = []
    # x of NW corner
    rect.append(vehicle.xBegin * CAR_SIZE + CAR_SIZE//10)
    # y of NW corner
    rect.append(vehicle.yBegin * CAR_SIZE + 50)

    if vehicle.orientation == 'H':
        # width of rect
        rect.append(CAR_SIZE * vehicle.length - CAR_SIZE//5)
        # length of rect
        rect.append(CAR_SIZE*4//5)
    elif vehicle.orientation == 'V':
        # width of rect
        rect.append(CAR_SIZE*4//5)
        # length of rect
        rect.append(CAR_SIZE * vehicle.length - CAR_SIZE//5)

    image.fill(huemap[vehicle.name], rect)

def readBoard(vehicles):
    """Read in board and make hue map"""

    # read in all unique names
    names = [vehicle.name for vehicle in vehicles]
    nameCount = len(names) - 1
    # move goal car to the front
    random.shuffle(names)
    names.remove('X')

    # make huemap
    huemap = dict()
    for i in range(nameCount):
        huemap[names[i]] = (hue(i / nameCount))
    huemap['X'] = (RED)
    return huemap

def hue(number):
    """Returns a hue for a given number between 0 and 1"""

    # Orange to green
    if number < 2/6:
        return (255 * (1 - (number) * 3), 255, 0)
    # Green to cyan
    elif number < 3/6:
        return (0, 255, 255 * (number-2/6) * 6)
    # Cyan to blue
    elif number < 4/6:
        return (0, 255 * (1 - (number-3/6) * 6), 255)
    # Blue to purple
    elif number < 5/6:
        return (255 * (number-4/6), 0, 255)
    # Purple to red
    else:
        return (255, 0, 255 * (1 - (number-5/6) * 6))
