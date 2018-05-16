import pygame
import random

# size constant
CAR_SIZE = 500

def drawBoard(vehicles, size, huemap, name):

    # initialise image
    image = pygame.Surface((size * 500, size * 500))
    image.fill((127, 127, 127))
    WHITE = (255,255,255)

    # draw all cars
    for i in range(len(vehicles)):
        vehicle = vehicles[i]
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

        if vehicle.name == 'X':
            # corners of goal car
            nw = [vehicle.xBegin * 500 + 50, vehicle.yBegin * 500 + 50]
            ne = [(vehicle.xBegin + vehicle.length) * 500 - 60, vehicle.yBegin * 500 + 50]
            sw = [vehicle.xBegin * 500 + 50, vehicle.yBegin * 500 + 430]
            se = [(vehicle.xBegin + vehicle.length) * 500 - 60, vehicle.yBegin * 500 + 430]

            # draw a cross
            pygame.draw.line(image, WHITE, nw, se, 20)
            pygame.draw.line(image, WHITE, ne, sw, 20)

    # save image
    pygame.image.save(image, name + ".png")


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
