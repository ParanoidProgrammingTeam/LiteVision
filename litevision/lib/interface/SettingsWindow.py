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

        # sene seçme ↓↓
        year_label_rect = pygame.Rect(
            (12, 132), ((len(lang.strings['year_label']) * 10) - 19, 19))
        self.year_label = UILabel(year_label_rect, lang.strings['year_label'],
                                  self.manager, self, self, '#year_menu_label')
        year_drop_down_rect = pygame.Rect((12, 156), (84, 24))
        year_drop_down_rect.center = (year_label_rect.center[0],
                                      year_label_rect.center[1] + 19)
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
            (200, 132), ((len(lang.strings['language_label']) * 10) - 19, 19))
        self.lang_label = UILabel(lang_label_rect,
                                  lang.strings['language_label'], self.manager,
                                  self, self, '#lang_menu_label')
        lang_drop_down_rect = pygame.Rect((200, 156), (84, 24))
        lang_drop_down_rect.center = (lang_label_rect.center[0],
                                      lang_label_rect.center[1] + 19)
        self.lang_drop_down = UIDropDownMenu(GUI_LANGUAGES,
                                             self.settings["language"],
                                             lang_drop_down_rect, self.manager,
                                             self, self, '#lang_menu')

    def process_event(self, event: pygame.event.Event) -> bool:
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.year_drop_down_menu):
            self.settings["year"] = event.text
            write_to(self.settings)
            lang.strings = lang.change_strings()
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.lang_drop_down):
            self.settings["language"] = event.text
            write_to(self.settings)
            lang.strings = lang.change_strings()

    def update(self, time_delta):
        super().update(time_delta)