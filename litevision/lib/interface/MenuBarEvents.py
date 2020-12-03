import os
import pygame
import pygame_gui

from litevision.res.glob import *


class HandlerForMenuBarEvents:
    def __init__(self, window_surface, ui_manager):
        self.window_surface = window_surface
        self.ui_manager = ui_manager

        # bunu kullanır mıyız emin değilim direkt eventle de halledebilirz sanırım ama yeniden açıldığında
        # son bırakıldığı halde olması için diye düşündüm
        self.litevison_settings = read_json(LITEVISION_SETTINGS_PATH)
        self.theme_file = read_json(THEME_FILE)

        self.red_button = "litevision\\res\\image_examples\\rgb_icon\\red.png"
        self.green_button = "litevision\\res\\image_examples\\rgb_icon\\green.png"
        self.blue_button = "litevision\\res\\image_examples\\rgb_icon\\blue.png"

    def process_events(self, event, menu_bar):
        pass