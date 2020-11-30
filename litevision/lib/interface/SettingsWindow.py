import pygame
import pygame_gui

from pygame_gui.elements import UIDropDownMenu, UIButton, UILabel, UIWindow
from litevision.res.glob import *


class SettingsWindow(UIWindow):
    """
    Bu tüm ayarların yapıldığı pencere olucak...
    Tüm ayarlar derken takım numarasının girildiği, led renklerinin değiştirildiği,
    kullanılan kameranın değiştirildiği(?) yer..
    
    :param rect: koordinat ve ekran büyüklüğü
    :param manager: ui yöneticisi muhtemelen tüm arayüzün yöneticisi olucak burdaki
    :param team_number: Takım Numarası (init içinde olduğu için default giricez mantıken objeyi yaparken
    sonradan penceredeki bi yazı kutusuyla değiştirilebilir yaparız)
    """
    def __init__(self, rect, manager, team_number):
        super().__init__(rect,
                         manager,
                         'Settings',
                         'SettingsWindow',
                         '#settings_window',
                         resizable=True)
        self.manager = manager
        self.team_number = team_number
        self.settings = read_json()
        # şöyle bi şi düşünüyorum şuan ayarlar ekranında butonlar olucak takım numarası değiştirin, vs. yazıcak butonlarda
        # bunlara basınca ayarlar içinde yeni bi pencere açılıcak içinde yazı yazma kutusu olan ordan yeni numara girilicek gibi
        # ve bunu tüm ayarlar için yapalım gibi düşündüm güzel olur mu idk ama olur gibi geldi
        year_label_rect = pygame.Rect((12, 132), (105, 19))
        self.year_label = UILabel(year_label_rect, 'Yıl Seçiniz: ',
                                  self.manager, self, self, '#year_menu_label')
        year_drop_down_rect = pygame.Rect((12, 156), (84, 24))
        self.year_selections = ['2018', '2019', '2020']
        self.year_drop_down_menu = UIDropDownMenu(self.year_selections,
                                                  self.settings["year"],
                                                  year_drop_down_rect,
                                                  self.manager,
                                                  self,
                                                  self,
                                                  object_id='#year_menu')

    def process_event(self, event: pygame.event.Event) -> bool:
        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == self.year_drop_down_menu):
            self.settings["year"] = event.text
            write_to(self.settings)

    def update(self, time_delta):
        super().update(time_delta)