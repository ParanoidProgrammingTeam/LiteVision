"""
Bütün repoda kullanılabilicek değişkenler falan filan 'glob' işte niye açıklama yapıyom pdfksğdpfkpsdlfk     
"""
from typing import Union
from pygame.event import Event

# buraya event yazarız..?
GUI_BUTTON_PRESSED = None  # type: Union[Event, None]
# gibi.. ya da direkt event'i yazmak daha mantıklı olabilir boş değişkene göre bilmiyom lfjğsdfokğsdprfk

__all__ = ['GUI_BUTTON_PRESSED']
# çünkü from glob import * kullanların typing.Union gibi modülleri importlamasını istemiyorum pdflkgjğdfpk
# yeni global değişken yazınca bu listenin içine '' içinde yazın import * diyince importlanıcak şeyler listesi