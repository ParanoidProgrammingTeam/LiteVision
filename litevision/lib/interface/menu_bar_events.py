from litevision.lib.database import *
from litevision.res.glob import *
import pygame_gui
import pygame
import os



class HandlerForMenuBarEvents:
    def __init__(self, window_surface, ui_manager):
        self.window_surface = window_surface
        self.ui_manager = ui_manager

        self.stream_started = False
        self.processing = False

        self.min_rgb_picker = None
        self.max_rgb_picker = None

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
            self.min_rgb_dict = self.litevison_settings["min_color"]["rgb"]
            min_rgb_tuple = (int(self.min_rgb_dict["r"]),
                             int(self.min_rgb_dict["g"]),
                             int(self.min_rgb_dict["b"]))
            self.min_rgb_color = pygame.Color(min_rgb_tuple)
            self.min_hsv_color = self.min_rgb_color.hsva
            self.max_rgb_dict = self.litevison_settings["max_color"]["rgb"]
            max_rgb_tuple = (int(self.max_rgb_dict["r"]),
                             int(self.max_rgb_dict["g"]),
                             int(self.max_rgb_dict["b"]))
            self.max_rgb_color = pygame.Color(max_rgb_tuple)
            self.max_hsv_color = self.max_rgb_color.hsva
            if self.min_rgb_picker == None:
                # open color picker or post event to open it
                self.min_rgb_picker = pygame_gui.windows.UIColourPickerDialog(
                    rect=pygame.Rect((64, 200), (390, 390)),
                    manager=self.ui_manager,
                    window_title='Minimum',
                    initial_colour=self.min_rgb_color)
                self.max_rgb_picker = pygame_gui.windows.UIColourPickerDialog(
                    rect=pygame.Rect((424, 200), (390, 390)),
                    manager=self.ui_manager,
                    window_title='Maximum',
                    initial_colour=self.max_rgb_color)
            else:
                # close
                self.min_rgb_picker.kill()
                self.min_rgb_picker = None
                self.max_rgb_picker.kill()
                self.max_rgb_picker = None

        if (event.type == pygame.USEREVENT and event.user_type
                == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED):
            min_color_dict = self.litevison_settings["min_color"]
            max_color_dict = self.litevison_settings["max_color"]
            if event.ui_element == self.min_rgb_picker:
                self.min_rgb_color = event.colour
                self.min_rgb_dict = {
                    'r': str(self.min_rgb_color.r),
                    'g': str(self.min_rgb_color.g),
                    'b': str(self.min_rgb_color.b)
                }
                self.min_hsv_color = self.min_rgb_color.hsva
                self.min_hsv_dict = {
                    'h': str(self.min_hsv_color[0]),
                    's': str(self.min_hsv_color[1]),
                    'v': str(self.min_hsv_color[2]),
                    'a': str(self.min_hsv_color[3])
                }
                min_color_dict = {
                    'rgb': self.min_rgb_dict,
                    'hsva': self.min_hsv_dict
                }
                self.min_rgb_picker = None
            if event.ui_element == self.max_rgb_picker:
                self.max_rgb_color = event.colour
                self.max_rgb_dict = {
                    'r': str(self.max_rgb_color.r),
                    'g': str(self.max_rgb_color.g),
                    'b': str(self.max_rgb_color.b)
                }
                self.max_hsv_color = self.max_rgb_color.hsva
                self.max_hsv_dict = {
                    'h': str(self.max_hsv_color[0]),
                    's': str(self.max_hsv_color[1]),
                    'v': str(self.max_hsv_color[2]),
                    'a': str(self.max_hsv_color[3])
                }
                max_color_dict = {
                    'rgb': self.max_rgb_dict,
                    'hsva': self.max_hsv_dict
                }
                self.max_rgb_picker = None
            self.litevison_settings["min_color"] = min_color_dict
            self.litevison_settings["max_color"] = max_color_dict
            write_to(self.litevison_settings, LITEVISION_SETTINGS_PATH)

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_object_id == '#menu_bar.#start_processing'):
            if self.processing == False and self.stream_started:
                self.processing = True
            else:
                self.processing = False