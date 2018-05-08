import pygame
import random

def drawBoard(vehicles, size):

    # initialise image
    image = pygame.Surface((size * 50, size * 50))
    image.fill((127, 127, 127))
    huemap = readBoard(vehicles)

    # draw all cars
    for i in range(len(vehicles)):
        vehicle = vehicles[i]
        rect = []
        if vehicle.orientation == 'H':
            rect = [vehicle.xBegin * 50 + 5, vehicle.yBegin * 50 + 5, 50 * vehicle.length - 10, 40]
        elif vehicle.orientation == 'V':
            rect = [vehicle.xBegin * 50 + 5, vehicle.yBegin * 50 + 5, 40, 50 * vehicle.length - 10]
        image.fill(huemap[vehicle.name], rect)

    # save image
    pygame.image.save(image, "drawing.jpeg")

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
    huemap['X'] = ((255,0,0))
    return huemap
