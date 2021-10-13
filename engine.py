import pygame
from pygame.locals import *

from game_state import GameState


class Engine:

    MAX_FPS = 60

    def __init__(self, window):
        self.window = window
        self.surface = self.window.get_surface()
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.active_game_state = GameState(self)

    def set_active_state(self, game_state):
        self.active_game_state = game_state

    def run(self):
        self.is_running = True
        while self.is_running:

            ticks_from_start = pygame.time.get_ticks()
            frame_time_ms = self.clock.tick(Engine.MAX_FPS)
            frame_time_s = frame_time_ms / 1000.
            print(f"Ticks: {ticks_from_start}, Frame time (ms): {frame_time_ms}")

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()
                self.active_game_state.handle_event(event)

            self.active_game_state.update(frame_time_s)
            self.active_game_state.draw(self.surface)
            pygame.display.update()

    def stop(self):
        self.is_running = False
        pygame.quit()
        exit()
