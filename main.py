import pygame
from pygame.locals import *

from window import Window
from gui import Button


class Application:

    MAX_FPS = 120

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = Window()

        self.start_button = Button("Start", (40, 160), (200, 50))
        self.options_button = Button("Options", (40, 200), (200, 50))
        self.exit_button = Button("Exit", (40, 240), (200, 50))
        self.exit_button.set_on_click_function(self.stop)

        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(Application.MAX_FPS)
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.stop()

            self.start_button.update()
            self.options_button.update()
            self.exit_button.update()

            render_surface = self.window.surface
            render_surface.fill('#90E0F3')
            self.start_button.draw(render_surface)
            self.options_button.draw(render_surface)
            self.exit_button.draw(render_surface)
            pygame.display.update()

    def stop(self):
        self.is_running = False
        pygame.quit()
        exit()


if __name__ == "__main__":
    Application().run()
