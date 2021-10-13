import pygame


class Window:

    WIDTH, HEIGHT = DIMENSIONS = (640, 360)

    def __init__(self, caption):
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode(Window.DIMENSIONS)
        self.rect = self.surface.get_rect()

    @property
    def size(self):
        return self.rect.size

    def get_surface(self):
        return self.surface