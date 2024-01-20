import pygame


class Timer:
    FONT_SIZE = 30
    FONT = pygame.font.SysFont("comicsansms", FONT_SIZE)
    COLOR = (128, 64, 0)
    BG_COLOR = (255, 246, 182)

    def __init__(self, x, y):
        self.time_left = 60
        self.x = x
        self.y = y
        self.text = Timer.FONT.render(str(self.time_left) + " seconds remaining", True, Timer.COLOR)
        self.time = pygame.time.get_ticks()

    def update_time(self):
        if pygame.time.get_ticks() - self.time >= 1000:
            self.time_left = self.time_left - 1
            self.time = pygame.time.get_ticks()

    def draw(self, screen):
        self.update_time()
        self.text = Timer.FONT.render(str(self.time_left) + " seconds remaining", True, Timer.COLOR)
        screen.blit(self.text, (self.x, self.y))
