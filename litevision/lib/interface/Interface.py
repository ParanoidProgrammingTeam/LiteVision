import pygame
import pygame_gui

from litevision.res import glob


class GUInterface:
    """
    İsim değişebilir şimdilik koydum
    
    Burası işte genel olarak yani arayüzün çalışması için olan sınıf
    """
    def __init__(self):
        pygame.init()

        # ana pencere
        pygame.display.set_caption("LiteVision")
        self.window_dimensions = (800, 600)
        # ↓↓ daha ikon olmadığı için yorum satırları yapıyorum
        ## title_icon = pygame.image.load("") # path olmalı
        ## pygame.display.set_icon(title_icon)
        self.main_window = pygame.display.set_mode(self.window_dimensions)
        self.background = pygame.Surface(self.window_dimensions)
        self.background.fill(pygame.Color("#000000"))

        # manager
        ## theme_path = ""
        self.manager = pygame_gui.UIManager(self.window_dimensions)

        self.clock = pygame.time.Clock()
        self.is_running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

        self.manager.process_events(event)

    def run(self):
        # main loop
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0  # sets to 60 fps

            for event in pygame.event.get():
                self.on_event(event)

            self.manager.update(time_delta)

            self.main_window.blit(self.background, (0, 0))

            self.manager.draw_ui(self.main_window)

            pygame.display.update()