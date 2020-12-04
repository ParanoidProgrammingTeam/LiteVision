"""
Bütün repoda kullanılabilicek değişkenler falan filan 'glob' işte niye açıklama yapıyom pdfksğdpfkpsdlfk     
"""
from typing import Union
from pygame.event import Event
import json
import pygame

# buraya event yazarız..?
GUI_STREAM_WINDOW_START: Union[Event,
                               None] = Event(pygame.USEREVENT,
                                             {'user_type': 'stream_started'})
GUI_STREAM_WINDOW_PAUSE: Union[Event,
                               None] = Event(pygame.USEREVENT,
                                             {'user_type': 'stream_paused'})

# pygame gui elemanları için anchorları tek tek yazmak üşendirici olur gibi geldi direkt buraya değişkenlere
# yazıcam çok daha rahat olur bence müq
GUI_ANCHORS_BOTTOM_LEFT = {
    'left': 'left',
    'right': 'left',
    'top': 'bottom',
    'bottom': 'bottom'
}
GUI_ANCHORS_TOP_RIGHT = {
    'left': 'right',
    'right': 'right',
    'top': 'top',
    'bottom': 'top'
}
GUI_ANCHORS_BOTTOM_RIGHT = {
    'left': 'right',
    'right': 'right',
    'top': 'bottom',
    'bottom': 'bottom'
}
# top left zaten default diye eklemedim

APP_SETTINGS_PATH = "litevision\\res\\settings.json"
LITEVISION_SETTINGS_PATH = "litevision\\res\\litevision.json"
THEME_FILE = "litevision\\res\\theme.json"

MENU_BAR_DATA_DICT = {
    '#icon': {
        'display_name': '',
        'items': {}
    },
    '#empty_1': {
        'display_name': '',
        'items': {}
    },
    '#empty_2': {
        'display_name': '',
        'items': {}
    },
    '#networking': {
        'display_name': ' ',
        'items': {}
    },
    '#start_pause': {
        'display_name': ' ',
        'items': {}
    },
    '#cam_change': {
        'display_name': ' ',
        'items': {}
    },
    '#rgb_button': {
        'display_name': ' ',
        'items': {}
    }
}

GUI_OFFSET_VALUE = 5
GUI_LANGUAGES = ['turkce', 'english']

__all__ = [
    'GUI_STREAM_WINDOW_START', 'GUI_STREAM_WINDOW_PAUSE',
    'GUI_ANCHORS_BOTTOM_LEFT', 'GUI_ANCHORS_BOTTOM_RIGHT',
    'GUI_ANCHORS_TOP_RIGHT', 'APP_SETTINGS_PATH', 'LITEVISION_SETTINGS_PATH',
    'THEME_FILE', 'MENU_BAR_DATA_DICT', 'GUI_OFFSET_VALUE', 'GUI_LANGUAGES'
]
# çünkü from glob import * kullanların typing.Union gibi modülleri importlamasını istemiyorum pdflkgjğdfpk
# yeni global değişken yazınca bu listenin içine '' içinde yazın import * diyince importlanıcak şeyler listesi