import pygame


class Duck:
    JUMP_HEIGHT = 150
    JUMP_SPEED = 50

    def __init__(self, x, y):
        self.animation_state = 1  # Track which frame of the run animation should be displayed next
        self.state1 = pygame.image.load('duck1.png')
        self.state2 = pygame.image.load('duck2.png')
        self.state3 = pygame.image.load('duck3.png')
        self.defaultx = x
        self.defaulty = y
        self.x = x
        self.y = y
        self.jumping = False

    def jump(self):
        """
        Make the duck jump. You can jump indefinitely.
        """
        self.jumping = True
        self.animation_state = 3

    def end_jump(self):
        self.jumping = False
        self.animation_state = 1

    def draw(self, screen):
        """
        Draws the duck onto the screen
        :param screen: The screen on which to draw the duck
        """
        if self.jumping:
            if self.y > self.defaulty - Duck.JUMP_HEIGHT:
                self.y = self.y - Duck.JUMP_SPEED

        if self.y < self.defaulty and not self.jumping:
            self.y = self.y + Duck.JUMP_SPEED

        if self.animation_state == 3:
            screen.blit(self.state3, (self.x, self.y))
        elif self.animation_state == 1:
            screen.blit(self.state1, (self.x, self.y))
            self.animation_state = 2
        else:
            screen.blit(self.state2, (self.x, self.y))
            self.animation_state = 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.state1.get_width(), self.state1.get_height())
