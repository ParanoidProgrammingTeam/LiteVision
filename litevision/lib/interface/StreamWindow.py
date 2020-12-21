import pygame
import pygame_gui

from pygame_gui.elements import UIImage
from litevision.lib import vision
from litevision.res.glob import *


class StreamWindow(UIImage):
    """
    Kameradakilerin yansıtıldığı ekran bu sınıfın objesi olucak.
    
    :param rect: koordinat ve ekran büyüklüğü
    :param manager: ui yöneticisi, muhtemelen tüm arayüzün yöneticisi neyse o olucak burdaki
    """
    def __init__(self, rect, stream_surface, manager):
        super().__init__(rect,
                         stream_surface,
                         manager,
                         object_id='#stream_window')