from pygame_gui.elements import UIImage
from litevision.res.glob import *


class StreamWindow(UIImage):
    """
    Kameradakilerin yansıtıldığı ekran bu sınıfın objesi olucak.
    
    Bu sınıfa çok gerek yoktu aslında ama yaptım öyle attribute ekleyebilirdim ama başka yerlerde yönetilen bi uiimage oldu baya neyse
    
    :param rect: koordinat ve ekran büyüklüğü
    :param stream_surface: pygame surface işte
    :param manager: ui yöneticisi, muhtemelen tüm arayüzün yöneticisi neyse o olucak burdaki
    """
    def __init__(self, rect, stream_surface, manager):
        super().__init__(rect,
                         stream_surface,
                         manager,
                         object_id='#stream_window')