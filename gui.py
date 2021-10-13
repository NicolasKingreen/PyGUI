import pygame


pygame.font.init()
FONT32 = pygame.font.SysFont(None, 32)
FONT48 = pygame.font.SysFont(None, 48)


class Button:

    def __init__(self, text, position, size):

        # text
        self.text_color = "#FFFFFF"
        self.text_surface = FONT32.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(topleft=position)

        hovered_text_position = position[0] - 4, position[1] - 4
        self.hovered_text_surface = FONT48.render(text, True, self.text_color)
        self.hovered_text_rect = self.hovered_text_surface.get_rect(topleft=hovered_text_position)

        # text shadow
        self.text_shadow_color = "#B8B3E9"
        self.shadow_offset = (2, 2)
        text_shadow_position = position[0] + self.shadow_offset[0], position[1] + self.shadow_offset[1]
        self.text_shadow_surface = FONT32.render(text, True, self.text_shadow_color)
        self.text_shadow_rect = self.text_shadow_surface.get_rect(topleft=text_shadow_position)
        hovered_text_shadow_position = hovered_text_position[0] + self.shadow_offset[0], hovered_text_position[1] + self.shadow_offset[1]
        self.hovered_text_shadow_surface = FONT48.render(text, True, self.text_shadow_color)
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

