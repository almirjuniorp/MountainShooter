import pygame

from code.Const import WIN_WIDTH, WIN_EIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_EIGHT))

    def run (self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



