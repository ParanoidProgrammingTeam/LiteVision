import pygame
import pygame_gui

from pygame_gui.elements import UIWindow
from litevision.res.glob import *


class StreamWindow(UIWindow):
    """
    Kameradakilerin yansıtıldığı ekran bu sınıfın objesi olucak.
    
    :param rect: koordinat ve ekran büyüklüğü
    :param manager: ui yöneticisi, muhtemelen tüm arayüzün yöneticisi neyse o olucak burdaki
    """
    def __init__(self, rect):
        pass