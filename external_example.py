import pygame


# Simple state
class State:
    def __init__(self, engine):
        self.engine = engine

    def on_draw(self, surface):
        pass

    def on_event(self, event):
        pass

    def on_update(self, delta, ticks):
        pass


# Simple display and state manager
class DisplayEngine:
    def __init__(self, caption, width, height, flags=0):
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.delta = 0
        self.fps = 60

        self.state = State(self)
        self.on_quit = self.quit

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def size(self):
        return self.rect.size

    def main_loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_quit()
                else:
                    self.state.on_event(event)

            ticks = pygame.time.get_ticks()
            self.state.on_draw(self.surface)
            self.state.on_update(self.delta, ticks)
            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)

    def quit(self):
        self.running = False


class Player:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = image.get_rect(center=position)
        self.center = pygame.Vector2(self.rect.center)
        self.speed = speed
        self.vector = pygame.Vector2()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, delta):
        self.center += self.vector * delta * self.speed
        self.rect.center = self.center


class ExampleState(State):
    def __init__(self, engine):
        State.__init__(self, engine)
        self.moving = None
        player_image = self.create_player_image()
        self.player = Player(player_image, self.engine.rect.center, 0.1)

    def create_player_image(self):
        surface = pygame.Surface((32, 32))
        surface.fill(pygame.Color("dodgerblue"))
        return surface

    def on_draw(self, surface):
        surface.fill(pygame.Color("black"))
        self.player.draw(surface)

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:
                self.moving = pygame.Vector2(event.pos)
                self.player.vector = (self.moving - self.player.center).normalize()

    def on_update(self, delta, ticks):
        if self.moving:
            self.player.update(delta)

            if self.player.center.x - 1 < self.moving.x < self.player.center.x + 1:
                if self.player.center.y - 1 < self.moving.y < self.player.center.y + 1:
                    self.moving = None


def main():
    pygame.init()
    engine = DisplayEngine("Example", 800, 600)
    state = ExampleState(engine)
    engine.state = state
    engine.main_loop()


main()