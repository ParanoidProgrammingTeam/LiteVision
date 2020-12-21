import os
import pygame
import pygame_gui

from litevision.res.glob import *
from litevision.lib.database import *
from litevision.lib import vision


class HandlerForMenuBarEvents:
    def __init__(self, window_surface, ui_manager):
        self.window_surface = window_surface
        self.ui_manager = ui_manager

        self.stream_started = False

        # bunu kullanır mıyız emin değilim direkt eventle de halledebilirz sanırım ama yeniden açıldığında
        # son bırakıldığı halde olması için diye düşündüm
        self.litevison_settings = read_json(LITEVISION_SETTINGS_PATH)
        self.theme_file = read_json(THEME_FILE)

    def process_events(self, event, menu_bar):
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#start_pause'):
            if self.stream_started == False:
                sp_icon = pygame.image.load(
                    os.path.join('litevision', 'res', 'image_examples',
                                 'start_icon', 'pause.png')).convert_alpha()
                self.stream_started = True
                event.ui_element.set_image(sp_icon)
                pygame.event.post(GUI_STREAM_WINDOW_START)
            else:
                sp_icon = pygame.image.load(
                    os.path.join('litevision', 'res', 'image_examples',
                                 'start_icon', 'start.png')).convert_alpha()
                self.stream_started = False
                event.ui_element.set_image(sp_icon)
                pygame.event.post(GUI_STREAM_WINDOW_PAUSE)
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#start_processing'):
            pass