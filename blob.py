'''

this is a very simple animation to illustrate how to take
an object oriented approach to making an animation with
python and pygame

'''

import pygame
import time
import random

# initializes pygame so fonts can be easily accessible
pygame.init()

# the main purpose why i made this stupid animation... work with
# object oriented programming in a way that is easy to see
class Blob:

    def __init__(self, color, radius, xspeed, yspeed, x, y, name):
        self.color = color
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.x = x
        self.y = y
        self.name = name

    def drawBlob(self):
        # handles just putting the blob on the screen
        pygame.draw.circle(game_display, self.color, [self.x, self.y], self.radius)


    def checkBoundaries(self):
        # standard set of if statements to make sure the blob stays on the screen
        if self.x >= DISPLAY_WIDTH or self.x <= 0:
            self.xspeed = -self.xspeed

        if self.y >= DISPLAY_HEIGHT or self.y <= 0:
            self.yspeed = -self.yspeed

    def addName(self):
        # handles rendering the font for pygame and creating the text rectangles
        font = pygame.font.Font('freesansbold.ttf', 20)

        textSurf = font.render(self.name, True, colors['black'])
        textRect = textSurf.get_rect()

        textRect.center = (self.x, self.y)
        game_display.blit(textSurf, textRect)

# global initializing variables specific to the blobs
blobs = []
blobName = 1

# global varialbes specific to pygame
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
clock = pygame.time.Clock()
FPS = 60

# this is not how this should be done...
# in the future use associated lists if you want to be able to
# easily randomize colors
colors = {
'black' : (0,0,0),
'white' : (255, 255, 255),
'red' : (255, 0, 0),
'green' : (0, 255, 0),
'blue' : (0, 0, 255),
}

# creates screen for things to be drawn to
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('blob class testing')

# Generates the blobs
for i in range(6):
    # features of the blob are randomized
    radius = random.randint(5, 100)
    xspeed = random.randint(1, 10)
    yspeed = random.randint(1, 10)
    xloc = random.randint(1, DISPLAY_WIDTH)
    yloc = random.randint(1, DISPLAY_HEIGHT)

    addBlob = Blob(colors['red'], radius, xspeed, yspeed, xloc, yloc, 'blob' + str(blobName))

    # blobs are held in a list... note that since they are object
    # oriented none of the blobs relate to eachother...
    blobs.append(addBlob)

    blobName += 1


# main game loop... I honestly should probably just say while true... lol jk blobbing is sicc
blobbing = True
while blobbing:

    game_display.fill(colors['blue'])
    for blob in blobs:
        # calling methods for each blob
        blob.drawBlob()
        blob.addName()

        # moves blobs with their own relative speeds / checks if it is still on screen
        # note: each blob checks itself
        blob.x += blob.xspeed
        blob.y += blob.yspeed

        blob.checkBoundaries()

    # standard handling of events in pygame. allows a user to quit out of this
    # pos animation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
    clock.tick(FPS)

# handles if something caused the while loop to accidently fire as false
# note: this should never actually be called. it is simply a safety net
pygame.quit()
quit()
