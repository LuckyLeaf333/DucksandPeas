import pygame


class Goose:
    SPEED = 50

    def __init__(self, x, y):
        self.animation_state = 1  # Track which frame of the run animation should be displayed next
        self.state1 = pygame.image.load('goose2.png')
        self.state2 = pygame.image.load('goose1.png')
        self.defaultx = x
        self.defaulty = y
        self.x = x
        self.y = y
        self.exists = False

    def set_exist(self):
        self.exists = True
        self.x = self.defaultx
        self.y = self.defaulty

    def set_nonexist(self):
        self.exists = False

    def draw(self, screen):
        """
        Draws the goose onto the screen if the goose exists
        :param screen: The screen on which to draw the duck
        """
        if not self.exists:
            return

        self.x = self.x - Goose.SPEED

        if self.x < 0:
            self.exists = False
            return

        if self.animation_state == 1:
            screen.blit(self.state1, (self.x, self.y))
            self.animation_state = 2
        else:
            screen.blit(self.state2, (self.x, self.y))
            self.animation_state = 1

    def check_collision(self, rect):
        if not self.exists:
            return False
        hitbox = pygame.Rect(self.x - 10, self.y, self.state1.get_width(), self.state1.get_height())
        return hitbox.colliderect(rect)
