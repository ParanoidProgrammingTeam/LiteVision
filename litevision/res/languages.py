from litevision.lib.database import *

all_settings = read_json()
language_setting = all_settings["language"]
global strings
if language_setting == "turkce":
    strings = {
        'settings_window': 'Ayarlar',
        'year_label': 'Yıl Seçiniz:',
        'language_label': 'Dil Seçiniz:',
        'resolution_label': 'Ekran Çözünürlüğü:',
        'screen_mode_label': 'Pencere Ayarı:',
        'screen_mode_list': ["çerçeveli", "çerçevesiz", "tam ekran"]
    }
else:
    strings = {
        'settings_window': 'Settings',
        'year_label': 'Change Year:',
        'language_label': 'Change Language:',
        'resolution_label': 'Screen Resolution:',
        'screen_mode_label': 'Window Mode:',
        'screen_mode_list': ["windowed", "borderless", "fullscreen"]
    }


def change_strings():
    all_settings = read_json()
    language_setting = all_settings["language"]
    strings = {}
    if language_setting == "turkce":
        strings = {
            'settings_window': 'Ayarlar',
            'year_label': 'Yıl Seçiniz:',
            'language_label': 'Dil Seçiniz:',
            'resolution_label': 'Ekran Çözünürlüğü:',
            'screen_mode_label': 'Pencere Ayarı:',
            'screen_mode_list': ["çerçeveli", "çerçevesiz", "tam ekran"]
        }
    if language_setting == "english":
        strings = {
            'settings_window': 'Settings',
            'year_label': 'Change Year:',
            'language_label': 'Change Language:',
            'resolution_label': 'Screen Resolution:',
            'screen_mode_label': 'Window Mode:',
            'screen_mode_list': ["windowed", "borderless", "fullscreen"]
        }
    return strings