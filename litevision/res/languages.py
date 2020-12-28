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
        'screen_mode_list': ["çerçeveli", "çerçevesiz"],
        'keep_changes': 'değişiklikleri kaydet?',
        'error': 'Hata',
        'keep_changes_hover': 'tüm değişiklikleri kaydet ve uygula?',
        'html_message_error_01':
        '<b>lütfen öncelikle ana ekrandaki tam ekran butonunu kullanarak<br>tam ekrandan çıkınız, daha sonra ekran modu değiştirebilirsiniz.</b>',
        'dismiss': 'Tamam',
        'dismiss_tip': 'Mesajı kapatmak için tıklayınız.'
    }
else:
    strings = {
        'settings_window': 'Settings',
        'year_label': 'Change Year:',
        'language_label': 'Change Language:',
        'resolution_label': 'Screen Resolution:',
        'screen_mode_label': 'Window Mode:',
        'screen_mode_list': ["windowed", "borderless"],
        'keep_changes': 'keep changes?',
        'error': 'Error',
        'keep_changes_hover': 'keep and apply all changes?',
        'html_message_error_01':
        '<b>please first use the fullscreen toggle to exit fullscreen<br>and then change the screen mode.</b>',
        'dismiss': 'Dismiss',
        'dismiss_tip': 'Click to get rid of this message.'
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
            'screen_mode_list': ["çerçeveli", "çerçevesiz"],
            'keep_changes': 'değişiklikleri kaydet?',
            'error': 'Hata',
            'keep_changes_hover': 'tüm değişiklikleri kaydet ve uygula?',
            'html_message_error_01':
            '<b>lütfen öncelikle ana ekrandaki tam ekran butonunu kullanarak<br>tam ekrandan çıkınız, daha sonra ekran modu değiştirebilirsiniz.</b>',
            'dismiss': 'Tamam',
            'dismiss_tip': 'Mesajı kapatmak için tıklayınız.'
        }
    if language_setting == "english":
        strings = {
            'settings_window': 'Settings',
            'year_label': 'Change Year:',
            'language_label': 'Change Language:',
            'resolution_label': 'Screen Resolution:',
            'screen_mode_label': 'Window Mode:',
            'screen_mode_list': ["windowed", "borderless"],
            'keep_changes': 'keep changes?',
            'error': 'Error',
            'keep_changes_hover': 'keep and apply all changes?',
            'html_message_error_01':
            '<b>please first use the fullscreen toggle to exit fullscreen<br>and then change the screen mode.</b>',
            'dismiss': 'Dismiss',
            'dismiss_tip': 'Click to get rid of this message.'
        }
    return strings