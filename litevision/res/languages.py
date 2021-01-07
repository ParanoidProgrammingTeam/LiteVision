"""
This file is for the languages that the ui will use.

If you want to add strings for a language that isn't here first add the name of the language to GUI_LANGUAGES
in glob.py -it doesn't matter if the letters are big or small as it will always be written in small to the json file, the way
it is written in that list is only for how it will be seen in the settings window-

Then, under line 14 add an elif statement in the middle of the already existing if-else statement. Here the string value
that it should compare 'language_setting' to is the all lowercase of what the string name is in GUI_LANGUAGES

In the elif statement make a dict with the same keys as the dicts that exist but, write the values as they are in the language you are adding

Finally, copy the elif statement you wrote and paste to the change_strings function as and IF statement.

strings = a dict containing all the strings in the gui

change_strings = a func to change the strings dict used especially when a language change is detected
"""
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
        'screen_mode_list': ["Çerçeveli", "Çerçevesiz"],
        'keep_changes': 'Değişiklikleri Kaydet?',
        'error': 'Hata',
        'keep_changes_hover': 'tüm değişiklikleri kaydet ve uygula?',
        'html_message_error_01':
        '<b>lütfen öncelikle ana ekrandaki tam ekran butonunu kullanarak<br>tam ekrandan çıkınız, daha sonra ekran modu değiştirebilirsiniz.</b>',
        'dismiss': 'Tamam',
        'dismiss_tip': 'Mesajı kapatmak için tıklayınız.',
        'min': 'Minimum',
        'max': 'Maksimum',
        'cancel': 'İptal'
    }
else:
    strings = {
        'settings_window': 'Settings',
        'year_label': 'Change Year:',
        'language_label': 'Change Language:',
        'resolution_label': 'Screen Resolution:',
        'screen_mode_label': 'Window Mode:',
        'screen_mode_list': ["Windowed", "Borderless"],
        'keep_changes': 'Keep Changes?',
        'error': 'Error',
        'keep_changes_hover': 'keep and apply all changes?',
        'html_message_error_01':
        '<b>please first use the fullscreen toggle to exit fullscreen<br>and then change the screen mode.</b>',
        'dismiss': 'Dismiss',
        'dismiss_tip': 'Click to get rid of this message.',
        'min': 'Minimum',
        'max': 'Maximum',
        'cancel': 'Cancel'
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
            'screen_mode_list': ["Çerçeveli", "Çerçevesiz"],
            'keep_changes': 'Değişiklikleri Kaydet?',
            'error': 'Hata',
            'keep_changes_hover': 'tüm değişiklikleri kaydet ve uygula?',
            'html_message_error_01':
            '<b>lütfen öncelikle ana ekrandaki tam ekran butonunu kullanarak<br>tam ekrandan çıkınız, daha sonra ekran modu değiştirebilirsiniz.</b>',
            'dismiss': 'Tamam',
            'dismiss_tip': 'Mesajı kapatmak için tıklayınız.',
            'min': 'Minimum',
            'max': 'Maksimum',
            'cancel': 'İptal'
        }
    if language_setting == "english":
        strings = {
            'settings_window': 'Settings',
            'year_label': 'Change Year:',
            'language_label': 'Change Language:',
            'resolution_label': 'Screen Resolution:',
            'screen_mode_label': 'Window Mode:',
            'screen_mode_list': ["Windowed", "Borderless"],
            'keep_changes': 'Keep Changes?',
            'error': 'Error',
            'keep_changes_hover': 'keep and apply all changes?',
            'html_message_error_01':
            '<b>please first use the fullscreen toggle to exit fullscreen<br>and then change the screen mode.</b>',
            'dismiss': 'Dismiss',
            'dismiss_tip': 'Click to get rid of this message.',
            'min': 'Minimum',
            'max': 'Maximum',
            'cancel': 'Cancel'
        }
    return strings