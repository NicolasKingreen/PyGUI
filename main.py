import pygame
from pygame.locals import *

from window import Window
from engine import Engine
from game_state import MenuGameState


class Application:

    def __init__(self):
        self.window = Window("Test GUI")
        self.engine = Engine(self.window)

        self.menu_state = MenuGameState(self.engine)
        self.engine.set_active_state(self.menu_state)

        self.engine.run()


if __name__ == "__main__":
    Application()
