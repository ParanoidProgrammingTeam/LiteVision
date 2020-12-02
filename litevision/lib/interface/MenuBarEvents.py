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

    def process_events(self, event):
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#rgb_button_items.#red'):
            self.litevison_settings["rgb"] = "red"
            write_to(self.litevison_settings, LITEVISION_SETTINGS_PATH)
            try:
                print("yay!")
                pygame.image.save(
                    pygame.image.load(
                        os.path.join('litevision', 'res', 'image_examples',
                                     'rgb_icon', 'red.png')).convert_alpha(),
                    os.path.join('litevision', 'res', 'image_examples',
                                 'rgb_icon', 'rgb.png'))
            except pygame.error:
                print("Failed..")
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS and
                event.ui_object_id == '#menu_bar.#rgb_button_items.#green'):
            self.litevison_settings["rgb"] = "green"
            write_to(self.litevison_settings, LITEVISION_SETTINGS_PATH)
            try:
                print("yay!")
                pygame.image.save(
                    pygame.image.load(
                        os.path.join('litevision', 'res', 'image_examples',
                                     'rgb_icon', 'green.png')).convert_alpha(),
                    os.path.join('litevision', 'res', 'image_examples',
                                 'rgb_icon', 'rgb.png'))
            except pygame.error:
                print("Failed..")
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#rgb_button_items.#blue'):
            self.litevison_settings["rgb"] = "blue"
            write_to(self.litevison_settings, LITEVISION_SETTINGS_PATH)
            try:
                print("yay!")
                pygame.image.save(
                    pygame.image.load(
                        os.path.join('litevision', 'res', 'image_examples',
                                     'rgb_icon', 'blue.png')).convert_alpha(),
                    os.path.join('litevision', 'res', 'image_examples',
                                 'rgb_icon', 'rgb.png'))
            except pygame.error:
                print("Failed..")