import pygame
from pygame.locals import *

from game_state import GameState


class Engine:

    MAX_FPS = 120

    def __init__(self, window):
        self.surface = pygame.display.set_mode(window.size)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.game_state = GameState(self)

    def set_state(self, game_state):
        self.game_state = game_state

    def run(self):
        self.is_running = True
        while self.is_running:

            ticks = pygame.time.get_ticks()
            frame_time_ms = self.clock.tick(Engine.MAX_FPS)
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()
                self.game_state.handle_event(event)

            self.game_state.update(frame_time_s)
            self.game_state.draw(self.surface)
            pygame.display.update()

    def stop(self):
        self.is_running = False
        pygame.quit()
        exit()
