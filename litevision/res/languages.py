from litevision.lib.database import *

all_settings = read_json()
language_setting = all_settings["language"]
global strings
strings = {}


def change_strings():
    all_settings = read_json()
    language_setting = all_settings["language"]
    strings = {}
    if language_setting == "turkce":
        strings = {
            'settings_window': 'Ayarlar',
            'year_label': 'Yıl Seçiniz:',
            'language_label': 'Dil Seçiniz:'
        }
    if language_setting == "english":
        strings = {
            'settings_window': 'Settings',
            'year_label': 'Change Year:',
            'language_label': 'Change Language:'
        }
    return strings


if language_setting == "turkce":
    strings = {
        'settings_window': 'Ayarlar',
        'year_label': 'Yıl Seçiniz:',
        'language_label': 'Dil Seçiniz:'
    }
if language_setting == "english":
    strings = {
        'settings_window': 'Settings',
        'year_label': 'Change Year:',
        'language_label': 'Change Language:'
    }