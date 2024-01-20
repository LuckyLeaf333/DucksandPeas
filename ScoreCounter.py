import pygame


class ScoreCounter:
    FONT_SIZE = 30
    FONT = pygame.font.SysFont("comicsansms", FONT_SIZE)
    COLOR = (128, 64, 0)
    BG_COLOR = (255, 246, 182)

    def __init__(self, x, y):
        self.score = 10
        self.x = x
        self.y = y
        self.text = ScoreCounter.FONT.render("Peas: " + str(self.score), True, ScoreCounter.COLOR)

    def change_score(self, num):
        self.score = self.score + num

    def draw(self, screen):
        self.text = ScoreCounter.FONT.render("Peas: " + str(self.score), True, ScoreCounter.COLOR)
        screen.blit(self.text, (self.x, self.y))
