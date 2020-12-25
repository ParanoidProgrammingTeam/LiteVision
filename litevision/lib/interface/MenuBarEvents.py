import os
import pygame
import pygame_gui

from litevision.res.glob import *
from litevision.lib.database import *


class HandlerForMenuBarEvents:
    def __init__(self, window_surface, ui_manager):
        self.window_surface = window_surface
        self.ui_manager = ui_manager

        self.stream_started = False
        self.processing = False

        self.rgb_picker = None

        # bunu kullanır mıyız emin değilim direkt eventle de halledebilirz sanırım ama yeniden açıldığında
        # son bırakıldığı halde olması için diye düşündüm
        self.litevison_settings = read_json(LITEVISION_SETTINGS_PATH)
        self.theme_file = read_json(THEME_FILE)

    def process_events(self, event, menu_bar, stream):
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
                and event.ui_object_id == '#menu_bar.#rgb_button'):
            self.rgb_dict = self.litevison_settings["color"]["rgb"]
            rgb_tuple = (int(self.rgb_dict["r"]), int(self.rgb_dict["g"]),
                         int(self.rgb_dict["b"]))
            self.rgb_color = pygame.Color(rgb_tuple)
            self.hsv_color = self.rgb_color.hsva
            if self.rgb_picker == None:
                # open color picker or post event to open it
                self.rgb_picker = pygame_gui.windows.UIColourPickerDialog(
                    rect=pygame.Rect((100, 200), (390, 390)),
                    manager=self.ui_manager,
                    initial_colour=self.rgb_color)
            else:
                # close
                self.rgb_picker.kill()
                self.rgb_picker = None

        if (event.type == pygame.USEREVENT and event.user_type
                == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED):
            self.rgb_color = event.colour
            self.rgb_dict = {
                'r': str(self.rgb_color.r),
                'g': str(self.rgb_color.g),
                'b': str(self.rgb_color.b)
            }
            self.hsv_color = self.rgb_color.hsva
            self.hsv_dict = {
                'h': str(self.hsv_color[0]),
                's': str(self.hsv_color[1]),
                'v': str(self.hsv_color[2]),
                'a': str(self.hsv_color[3])
            }
            color_dict = {'rgb': self.rgb_dict, 'hsva': self.hsv_dict}
            self.litevison_settings["color"] = color_dict
            write_to(self.litevison_settings, LITEVISION_SETTINGS_PATH)
            self.rgb_picker = None

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#start_processing'):
            if self.processing == False and self.stream_started:
                self.processing = True
            else:
                self.processing = False