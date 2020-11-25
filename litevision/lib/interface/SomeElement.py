import pygame
import pygame_gui

from pygame_gui.core import UIElement
from litevision.res.glob import *


class SomeElement(UIElement):
    """
    I will change the name when I know what this is for
    """
    def __init__(self):
        pass

    def process_event(self, event: pygame.event.Event) -> bool:
        pass

    def update(self, time_delta):
        pass