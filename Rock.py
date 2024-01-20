import pygame
import random


class Rock:
    ROCK_IMAGES = [pygame.image.load('rock1.png'), pygame.image.load('rock2.png'), pygame.image.load('rock3.png')]
    ROCK_SPEED = 40
    PEA_IMAGE = pygame.image.load('peas.png')

    def __init__(self, x, y, is_peas):
        self.image = Rock.ROCK_IMAGES[random.randint(0, 2)]
        self.is_peas = is_peas
        if is_peas:
            self.image = Rock.PEA_IMAGE
        # set x and y so that the x, y given in the parameters is the bottom left corner
        self.x = x
        self.y = y - self.image.get_height()
        self.exists = True

    def draw(self, screen):
        """
        Draw the rock on the screen. Do not do anything if the rock is not on the screen.
        :param screen: The screen to draw on
        """
        self.x = self.x - Rock.ROCK_SPEED
        if self.x < 0:
            self.exists = False
            return
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, rect):
        return pygame.Rect(self.x + 20, self.y + 20,
                           self.image.get_width() - 20, self.image.get_height() - 20).colliderect(rect)


