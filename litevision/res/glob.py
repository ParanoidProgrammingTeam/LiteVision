"""
Bütün repoda kullanılabilicek değişkenler falan filan 'glob' işte niye açıklama yapıyom pdfksğdpfkpsdlfk     
"""
from typing import Union
from pygame.event import Event
import json

# buraya event yazarız..?
GUI_BUTTON_PRESSED = None  # type: Union[Event, None]
# gibi.. ya da direkt event'i yazmak daha mantıklı olabilir boş değişkene göre bilmiyom lfjğsdfokğsdprfk

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

APP_SETTINGS_PATH = "litevision\\res\\glob.json"


def read_json(path=APP_SETTINGS_PATH):
    with open(path) as file:
        read = json.load(file)
    return read


def write_to(obj, path=APP_SETTINGS_PATH):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file, indent=4)
    except:
        print("İşlem başarısız...")
        return False
    return True


__all__ = [
    'GUI_BUTTON_PRESSED', 'GUI_ANCHORS_BOTTOM_LEFT',
    'GUI_ANCHORS_BOTTOM_RIGHT', 'GUI_ANCHORS_TOP_RIGHT', 'APP_SETTINGS_PATH',
    'read_json', 'write_to'
]
# çünkü from glob import * kullanların typing.Union gibi modülleri importlamasını istemiyorum pdflkgjğdfpk
# yeni global değişken yazınca bu listenin içine '' içinde yazın import * diyince importlanıcak şeyler listesi