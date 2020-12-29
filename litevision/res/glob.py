"""
Bütün repoda kullanılabilicek değişkenler falan filan 'glob' işte niye açıklama yapıyom pdfksğdpfkpsdlfk     
"""
from typing import Union
import os
import pygame
from pygame.event import Event

# buraya event yazarız..?
GUI_STREAM_WINDOW_START: Union[Event,
                               None] = Event(pygame.USEREVENT,
                                             {'user_type': 'stream_started'})
GUI_STREAM_WINDOW_PAUSE: Union[Event,
                               None] = Event(pygame.USEREVENT,
                                             {'user_type': 'stream_paused'})
GUI_WINDOW_RESOLUTION_CHANGED: Union[Event, None] = Event(
    pygame.USEREVENT, {'user_type': 'resolution_changed'})
GUI_TOGGLE_FULLSCREEN: Union[Event,
                             None] = Event(pygame.USEREVENT,
                                           {'user_type': 'fullscreen_toggled'})
GUI_LANUAGE_CHANGED: Union[Event,
                           None] = Event(pygame.USEREVENT,
                                         {'user_type': 'language_changed'})
GUI_CHANGES_MADE_TO_SETTINGS: Union[Event, None] = Event(
    pygame.USEREVENT, {'user_type': 'changes_made'})


def POST_SPECIAL_FLAG_CHANGE(text):
    GUI_SCREEN_SPECIAL_FLAGS_CHANGED: Union[Event, None] = Event(
        pygame.USEREVENT, {
            'user_type': 'screen_flag_changed',
            'text': text
        })
    pygame.event.post(GUI_SCREEN_SPECIAL_FLAGS_CHANGED)


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

# paths
APP_SETTINGS_PATH = os.path.join('litevision', 'res', 'settings.json')
LITEVISION_SETTINGS_PATH = os.path.join('litevision', 'res', 'litevision.json')
THEME_FILE = os.path.join('litevision', 'res', 'theme.json')
# i used os.path.join for it to be the most cross-platform as possible

MENU_BAR_DATA_DICT = {
    '#icon': {
        'display_name': '',
        'items': {}
    },
    '#empty_1': {
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
    '#start_processing': {
        'display_name': 'sp',
        'items': {}
    },
    '#cam_change': {
        'display_name': ' ',
        'items': {}
    },
    '#rgb_button': {
        'display_name': ' ',
        'items': {}
    },
    '#empty_2': {
        'display_name': '',
        'items': {}
    }
}

GUI_OFFSET_VALUE = 5
GUI_LANGUAGES = ['Turkce', 'English']

__all__ = [
    'GUI_STREAM_WINDOW_START', 'GUI_STREAM_WINDOW_PAUSE',
    'GUI_ANCHORS_BOTTOM_LEFT', 'GUI_ANCHORS_BOTTOM_RIGHT',
    'GUI_ANCHORS_TOP_RIGHT', 'APP_SETTINGS_PATH', 'LITEVISION_SETTINGS_PATH',
    'THEME_FILE', 'MENU_BAR_DATA_DICT', 'GUI_OFFSET_VALUE', 'GUI_LANGUAGES',
    'GUI_WINDOW_RESOLUTION_CHANGED', 'GUI_TOGGLE_FULLSCREEN',
    'POST_SPECIAL_FLAG_CHANGE', 'GUI_LANUAGE_CHANGED',
    'GUI_CHANGES_MADE_TO_SETTINGS'
]
# çünkü from glob import * kullanların typing.Union gibi modülleri importlamasını istemiyorum pdflkgjğdfpk
# yeni global değişken yazınca bu listenin içine '' içinde yazın import * diyince importlanıcak şeyler listesi