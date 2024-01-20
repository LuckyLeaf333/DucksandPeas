import pygame

pygame.font.init()


class Button:
    FONT_SIZE = 30
    FONT = pygame.font.SysFont("comicsansms", FONT_SIZE)
    MARGIN = 3
    BORDER_WIDTH = 3
    COLOR = (128, 64, 0)
    BG_COLOR = (255, 246, 182)

    def __init__(self, x, y, label):
        """
        Creates a button object with the given label, resized to default button height
        :param x: int, the top left x-coordinate of the button
        :param y: int, the top left y-coordinate of the button
        :param label: String label on the button
        """
        self.x = x
        self.y = y
        self.label = label
        self.text = Button.FONT.render(label, True, Button.COLOR)
        border_x = x - Button.MARGIN
        border_y = y - Button.MARGIN
        border_width = self.text.get_width() + 2 * Button.MARGIN
        border_height = self.text.get_height() + 2 * Button.MARGIN
        self.border = pygame.Rect(border_x, border_y, border_width, border_height)
        self.clickable = True

    def draw(self, screen):
        """
        Draws the button onto the screen, but does not update the screen
        :param screen: The screen on which to draw the button
        """
        pygame.draw.rect(screen, Button.BG_COLOR, pygame.Rect(self.border.x + Button.MARGIN,
                                                              self.border.y + Button.MARGIN, self.text.get_width(),
                                                              self.text.get_height()))
        pygame.draw.rect(screen, Button.COLOR, self.border, Button.BORDER_WIDTH, Button.BORDER_WIDTH)
        screen.blit(self.text, (self.x, self.y))

    def is_pressed(self):
        """
        Checks if the button is clicked.
        :return: True if the button is clicked and is clickable. False otherwise.
        """
        if self.clickable:
            mouse_pos = pygame.mouse.get_pos()
            if self.border.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.clickable = False
                    print(self.label)
                    return True
        return False

    def set_inactive(self):
        self.clickable = False

    def set_active(self):
        self.clickable = True