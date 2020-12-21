import pygame
import pygame_gui

import litevision.res.languages as lang
from pygame_gui.elements import UIDropDownMenu, UIButton, UILabel, UIWindow
from litevision.res.glob import *
from litevision.lib.database import *


class SettingsWindow(UIWindow):
    """
    Bu tüm ayarların yapıldığı pencere olucak...
    Tüm ayarlar derken takım numarasının girildiği, led renklerinin değiştirildiği,
    kullanılan kameranın değiştirildiği(?) yer..
    
    :param rect: koordinat ve ekran büyüklüğü
    :param manager: ui yöneticisi muhtemelen tüm arayüzün yöneticisi olucak burdaki
    """
    def __init__(self, rect, manager):
        super().__init__(rect,
                         manager,
                         lang.strings['settings_window'],
                         'SettingsWindow',
                         '#settings_window',
                         resizable=True)
        self.manager = manager
        self.settings = read_json()

        self.special_flags = self.settings['screen_mode']
        self.any_settings_changed = False
        self.setting_changed = {
            'res': False,  # resolution of screen
            'fll': False,  # screen made fullscreen
            'scr': False,  # screen mode changed (other than fullscreen)
            'lng': False,  # language changed
            'yrs': False  # year changed 
        }

        # resolution ↓↓
        resol_label_rect = pygame.Rect(
            (12, 32), ((len(lang.strings['resolution_label']) * 10) - 36, 19))
        self.resol_label = UILabel(resol_label_rect,
                                   lang.strings['resolution_label'],
                                   self.manager, self, self, '#res_menu_label')
        resol_drop_down_rect = pygame.Rect((12, 56), (94, 24))
        resol_drop_down_rect.topleft = resol_label_rect.bottomleft
        self.res_selections = [
            "600x500", "800x600", "900x650", "1000x700", "1200x700", "1240x740"
        ]
        current_res = self.settings["resolution"]
        self.resol_drop_down = UIDropDownMenu(
            self.res_selections,
            f"{current_res['width']}x{current_res['height']}",
            resol_drop_down_rect, self.manager, self, self, '#resolution_menu')

        # screen mode ↓↓
        scr_mode_label_rect = pygame.Rect(
            (200, 32),
            ((len(lang.strings['screen_mode_label']) * 10) - 19, 19))
        self.scr_mode_label = UILabel(scr_mode_label_rect,
                                      lang.strings['screen_mode_label'],
                                      self.manager, self, self,
                                      '#screen_mode_label')
        scr_mode_menu_rect = pygame.Rect((200, 56), (106, 24))
        scr_mode_menu_rect.topleft = scr_mode_label_rect.bottomleft
        self.scr_mode_selections = lang.strings['screen_mode_list']
        current_screen_mode = self.settings['screen_mode']
        if self.settings['screen_mode'] == "windowed" and self.settings[
                'language'] == "turkce":
            current_screen_mode = self.scr_mode_selections[0]
        elif self.settings['screen_mode'] == "borderless" and self.settings[
                'language'] == "turkce":
            current_screen_mode = self.scr_mode_selections[1]
        elif self.settings['screen_mode'] == "fullscreen" and self.settings[
                'language'] == "turkce":
            current_screen_mode = self.scr_mode_selections[2]
        self.scr_mode_menu = UIDropDownMenu(self.scr_mode_selections,
                                            current_screen_mode,
                                            scr_mode_menu_rect, self.manager,
                                            self, self, '#screen_menu')

        # sene seçme ↓↓
        year_label_rect = pygame.Rect(
            (12, 132), ((len(lang.strings['year_label']) * 10) - 19, 19))
        self.year_label = UILabel(year_label_rect, lang.strings['year_label'],
                                  self.manager, self, self, '#year_menu_label')
        year_drop_down_rect = pygame.Rect((12, 156), (84, 24))
        year_drop_down_rect.topleft = year_label_rect.bottomleft
        self.year_selections = ['2018', '2019', '2020']
        self.year_drop_down_menu = UIDropDownMenu(self.year_selections,
                                                  self.settings["year"],
                                                  year_drop_down_rect,
                                                  self.manager,
                                                  self,
                                                  self,
                                                  object_id='#year_menu')
        # dil seçme ↓↓
        lang_label_rect = pygame.Rect(
            (200, 132), ((len(lang.strings['language_label']) * 10) - 24, 19))
        self.lang_label = UILabel(lang_label_rect,
                                  lang.strings['language_label'], self.manager,
                                  self, self, '#lang_menu_label')
        lang_drop_down_rect = pygame.Rect((200, 156), (84, 24))
        lang_drop_down_rect.topleft = lang_label_rect.bottomleft
        self.lang_drop_down = UIDropDownMenu(GUI_LANGUAGES,
                                             self.settings["language"],
                                             lang_drop_down_rect, self.manager,
                                             self, self, '#lang_menu')

        # keep changes? ↓↓
        save_button_x_size = ((len(lang.strings['keep_changes']) * 10) - 18)
        save_button_rect = pygame.Rect((-16 - save_button_x_size, -16 - 24),
                                       (save_button_x_size, 24))
        self.save_button = UIButton(save_button_rect,
                                    lang.strings['keep_changes'],
                                    self.manager,
                                    self,
                                    'keep and apply all changes?',
                                    parent_element=self,
                                    object_id='#keep_changes',
                                    anchors=GUI_ANCHORS_BOTTOM_RIGHT)

    def process_event(self, event: pygame.event.Event) -> bool:
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.year_drop_down_menu):
            self.settings["year"] = event.text
            self.setting_changed['yrs'] = True
            self.any_settings_changed = True

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.lang_drop_down):
            self.settings["language"] = event.text
            self.setting_changed['lng'] = True
            self.any_settings_changed = True

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.resol_drop_down):
            resolution = self.make_res_tuple(event.text)
            self.settings["resolution"]['width'] = resolution[0]
            self.settings["resolution"]['height'] = resolution[1]
            self.setting_changed['res'] = True
            self.any_settings_changed = True

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.scr_mode_menu):
            new_scr_mode = SettingsWindow.change_scr_for_lang(
                self.settings['language'], "turkce", event)
            print(new_scr_mode)
            self.settings['screen_mode'] = new_scr_mode
            screen_mode = self.settings['screen_mode']
            if screen_mode == "borderless":
                if self.special_flags == pygame.FULLSCREEN:
                    self.special_flags = pygame.NOFRAME
                    self.setting_changed['fll'] = True
                    self.any_settings_changed = True
                elif self.special_flags != pygame.NOFRAME:
                    self.special_flags = pygame.NOFRAME
                    self.setting_changed['scr'] = True
                    self.any_settings_changed = True
            elif screen_mode == "windowed":
                if self.special_flags == pygame.FULLSCREEN:
                    self.special_flags = 0
                    self.setting_changed['fll'] = True
                    self.any_settings_changed = True
                elif self.special_flags != 0:
                    self.special_flags = 0
                    self.setting_changed['scr'] = True
                    self.any_settings_changed = True
            elif screen_mode == "fullscreen":
                if self.special_flags != pygame.FULLSCREEN:
                    self.special_flags = pygame.FULLSCREEN
                    self.setting_changed['fll'] = True
                    self.any_settings_changed = True

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#settings_window.#keep_changes'):
            if self.any_settings_changed == True:
                if self.setting_changed['res'] == True:
                    write_to(self.settings)
                    pygame.event.post(GUI_WINDOW_RESOLUTION_CHANGED)
                elif self.setting_changed['lng'] == True:
                    write_to(self.settings)
                    pygame.event.post(GUI_LANUAGE_CHANGED)
                elif self.setting_changed['yrs'] == True:
                    write_to(self.settings)
                elif self.setting_changed['fll'] == True:
                    write_to(self.settings)
                    pygame.event.post(GUI_TOGGLE_FULLSCREEN)
                elif self.setting_changed['scr'] == True:
                    if self.special_flags == 0:
                        write_to(self.settings)
                        POST_SPECIAL_FLAG_CHANGE(self.special_flags)
                    else:
                        write_to(self.settings)
                        POST_SPECIAL_FLAG_CHANGE(self.special_flags)
                lang.strings = lang.change_strings()
                saved_changes = False
                if self.setting_changed['res'] == True or self.setting_changed[
                        'scr'] == True:
                    saved_changes = True
                for key in self.setting_changed:
                    if self.setting_changed[key] == True:
                        self.setting_changed[key] = False
                self.any_settings_changed = False
                if saved_changes:
                    pygame.event.post(GUI_CHANGES_MADE_TO_SETTINGS)
            else:
                pass

    def update(self, time_delta):
        super().update(time_delta)

    def make_res_tuple(self, r_string):
        self.res_settings = self.settings['resolution']
        self.res_selections = [
            "600x500", "800x600", "900x650", "1000x700", "1200x700", "1240x740"
        ]
        if r_string == "600x500":
            self.res_settings['width'] = 600
            self.res_settings['height'] = 500
        elif r_string == "800x600":
            self.res_settings['width'] = 800
            self.res_settings['height'] = 600
        elif r_string == "900x650":
            self.res_settings['width'] = 900
            self.res_settings['height'] = 650
        elif r_string == "1000x700":
            self.res_settings['width'] = 1000
            self.res_settings['height'] = 700
        elif r_string == "1200x700":
            self.res_settings['width'] = 1200
            self.res_settings['height'] = 700
        elif r_string == "1240x740":
            self.res_settings['width'] = 1240
            self.res_settings['height'] = 740
        else:
            self.res_settings['width'] = 800
            self.res_settings['height'] = 600
        tuple_res = (self.res_settings['width'], self.res_settings['height'])
        return tuple_res

    @staticmethod
    def change_scr_for_lang(language_settings, language_name: str, event):
        new_data = event.text
        if language_settings == language_name:
            if event.text == lang.strings['screen_mode_list'][0]:
                new_data = "windowed"
            elif event.text == lang.strings['screen_mode_list'][1]:
                new_data = "borderless"
            elif event.text == lang.strings['screen_mode_list'][2]:
                new_data = "fullscreen"
        return new_data