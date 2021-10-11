import pygame
from pygame.locals import *


pygame.font.init()
FONT = pygame.font.SysFont(None, 32)
FONT2 = pygame.font.SysFont(None, 48)


class Button:

    def __init__(self, text, position, size):

        # text
        self.text_color = "#FFFFFF"
        self.text_surface = FONT.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(topleft=position)

        hovered_text_position = position[0] - 4, position[1] - 4
        self.hovered_text_surface = FONT2.render(text, True, self.text_color)
        self.hovered_text_rect = self.hovered_text_surface.get_rect(topleft=hovered_text_position)

        # text shadow
        self.text_shadow_color = "#B8B3E9"
        self.shadow_offset = (2, 2)
        text_shadow_position = position[0] + self.shadow_offset[0], position[1] + self.shadow_offset[1]
        self.text_shadow_surface = FONT.render(text, True, self.text_shadow_color)
        self.text_shadow_rect = self.text_shadow_surface.get_rect(topleft=text_shadow_position)
        hovered_text_shadow_position = hovered_text_position[0] + self.shadow_offset[0], hovered_text_position[1] + self.shadow_offset[1]
        self.hovered_text_shadow_surface = FONT2.render(text, True, self.text_shadow_color)
        self.hovered_text_shadow_rect = self.hovered_text_shadow_surface.get_rect(topleft=hovered_text_shadow_position)

        # core attributes
        self.is_hovered = False
        self.is_pressed = False
        self._on_click_function = None

    def update(self):
        self.on_hover()
        self.on_click()

    def on_hover(self):
        mouse_position = pygame.mouse.get_pos()
        if not self.is_hovered:
            if self.text_rect.collidepoint(mouse_position):
                if not self.is_hovered:
                    self.is_hovered = True
            else:
                self.is_hovered = False
        else:
            if self.hovered_text_shadow_rect.collidepoint(mouse_position):
                if not self.is_hovered:
                    self.is_hovered = True
            else:
                self.is_hovered = False

    def on_click(self):
        mouse_position = pygame.mouse.get_pos()
        if self.hovered_text_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            if not self.is_pressed:
                self.is_pressed = True
                if self._on_click_function:
                    self._on_click_function()
        else:
            self.is_pressed = False

    def set_on_click_function(self, function):
        self._on_click_function = function

    def draw(self, surface):
        if not self.is_hovered:
            surface.blit(self.text_shadow_surface, self.text_shadow_rect)
            surface.blit(self.text_surface, self.text_rect)
        else:
            surface.blit(self.hovered_text_shadow_surface, self.hovered_text_shadow_rect)
            surface.blit(self.hovered_text_surface, self.hovered_text_rect)


class Window:

    WIDTH, HEIGHT = DIMENSIONS = (640, 360)

    def __init__(self):
        pygame.display.set_caption("GUI Test")
        self.surface = pygame.display.set_mode(Window.DIMENSIONS)


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
