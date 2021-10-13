from gui import Button


class GameState:

    def __init__(self, engine):
        self.engine = engine

    def handle_event(self, event):
        pass

    def update(self, frame_time_s):
        pass

    def draw(self, surface):
        pass


class MenuState(GameState):

    def __init__(self, engine):
        GameState.__init__(self, engine)
        self.start_button = Button("Start", (40, 160), (200, 50))
        self.options_button = Button("Options", (40, 200), (200, 50))
        self.exit_button = Button("Exit", (40, 240), (200, 50))
        self.exit_button.set_on_click_function(self.engine.stop)

    def handle_event(self, event):
        pass

    def update(self, frame_time_s):
        self.start_button.update()
        self.options_button.update()
        self.exit_button.update()

    def draw(self, surface):
        surface.fill('#90E0F3')
        self.start_button.draw(surface)
        self.options_button.draw(surface)
        self.exit_button.draw(surface)
