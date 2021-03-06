"""
~~~~~~~~~~~~~~~~~~~~~~~~~TODO~~~~~~~~~~~~~~~~~~~~~~~~~~
- I just started I don't even know lol
- Settings Window [~74%]
- Stream Window [~90%]
- This Class [~67%]
- Menu Bar or Side Menu Bar [~56%]
- a lot more
- |DONE|MAKE A KEEP CHANGES BUTTON TO SETTINGS WINDOW SO ITS NOT SO MIND KILLING SPDKJFDPFKJ
- |should be done|rgb picker thingy pdfksdlfkpşlf
- team number selection
- update the auto-relaunch mechanizm and make it better dfgkpdlfkgpdlfk (if you can lol)
- and just deal with the fullscreen shite already [~80%]
- further expand the theme.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~NOTES~~~~~~~~~~~~~~~~~~~~~~~~~
- the fullscreen is still kinda buggy... it seems nice but if you double click to fastly i think it can swap the icons idk its weird
- the auto-relaunch is even wierder tbh, it crashes after a few times but i have no idea why, it changes for some reason i think
according to the changes made like 3 times if you change the screen mode 5 times if you change resolution or sth idk its very weird
FİXED! - (- if you select the already selected option on any of the settings options and press keep changes it closes the program thinking a change was
made but when it can't find ant keeps it closed. doing something like that would be idiotic but, i guess i still should try to fix it.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import os
import pygame
import pygame_gui
from pygame_gui.elements.ui_button import UIButton

from litevision.lib.interface.menu_bar import MenuBar
from litevision.lib.interface.menu_bar_events import HandlerForMenuBarEvents
from litevision.lib.interface.window_settings import SettingsWindow
from litevision.lib.interface.window_stream import StreamWindow

import litevision.lib.database as database
from litevision.lib import vision
from litevision.res.glob import *


class GUInterface:
    """
    İsim değişebilir şimdilik koydum
    
    Burası işte genel olarak yani arayüzün çalışması için olan sınıf
    """
    def __init__(self):
        pygame.init()

        # ana pencere
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("LiteVision")

        settings = database.read_json()
        resolution = settings['resolution']
        self.resolution = (int(resolution['width']), int(resolution['height']))
        self.window_dimensions = (self.resolution)

        settings['in_fullscreen'] = "false"
        database.write_to(settings)

        title_icon = pygame.image.load(
            os.path.join('litevision', 'res', 'image_examples', 'icon32x.png'))
        pygame.display.set_icon(title_icon)

        # şuanki ekran modunu şaapıyo
        flags = settings['screen_mode']
        if flags != "fullscreen":
            if flags == "borderless":
                self.special_flags = pygame.NOFRAME
            elif flags == "windowed":
                self.special_flags = 0

        self.main_window = pygame.display.set_mode(self.window_dimensions,
                                                   self.special_flags)
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.fill(pygame.Color("#2F4F4F"))

        # manager
        theme_path = THEME_FILE
        self.manager = pygame_gui.UIManager(self.window_dimensions, theme_path)

        # attributes / ui elements
        ## buttons
        ### settings button
        self.settings_button_rect = pygame.Rect((5, -48 - GUI_OFFSET_VALUE),
                                                (48, 48))
        self.settings_button = UIButton(self.settings_button_rect,
                                        '',
                                        self.manager,
                                        object_id='#settings_button',
                                        anchors=GUI_ANCHORS_BOTTOM_LEFT)
        ### close window button
        self.close_button = None
        if self.special_flags != 0:
            self.close_button_rect = pygame.Rect((-36, 0), (36, 16))
            self.close_button = UIButton(self.close_button_rect,
                                         '╳',
                                         self.manager,
                                         object_id='#close_ui_button',
                                         anchors=GUI_ANCHORS_TOP_RIGHT)
        ### minimize window button
        self.min_button = None
        if self.special_flags != 0:
            self.min_button_rect = pygame.Rect((-72, 0), (36, 16))
            self.min_button = UIButton(self.min_button_rect,
                                       '−',
                                       self.manager,
                                       object_id='#min_ui_button',
                                       anchors=GUI_ANCHORS_TOP_RIGHT)
        ### fullscreen button
        self.fullscreen_button_rect = pygame.Rect(
            (-40 - 3 - GUI_OFFSET_VALUE, -40 - 3 - GUI_OFFSET_VALUE), (40, 40))
        self.fullscreen_button = UIButton(self.fullscreen_button_rect,
                                          '',
                                          self.manager,
                                          object_id='#fullscreen',
                                          anchors=GUI_ANCHORS_BOTTOM_RIGHT)
        #### for some reason fullscreen only works when resolution is 800x600 ??? idk why
        self.unfull_button = UIButton(self.fullscreen_button_rect,
                                      '',
                                      self.manager,
                                      object_id='#unfull',
                                      anchors=GUI_ANCHORS_BOTTOM_RIGHT,
                                      visible=0)

        ## windows
        ### settings window
        self.settings_window = None

        ### stream window
        size_tuple = ((GUI_OFFSET_VALUE + (self.resolution[0] / 5),
                       GUI_OFFSET_VALUE + (self.resolution[1] / 11)),
                      (((self.resolution[0] / 3) * 2,
                        (self.resolution[1] / 3) * 2)))
        stream_window_rect = pygame.Rect(size_tuple)
        self.stream_surf = pygame.Surface(size_tuple[1])
        self.stream_window = StreamWindow(stream_window_rect, self.stream_surf,
                                          self.manager)

        ## other
        ### menubar
        self.menu_bar = MenuBar(pygame.Rect(
            (0, 0), (58, self.window_dimensions[1] -
                     self.settings_button_rect.height - GUI_OFFSET_VALUE)),
                                self.manager,
                                object_id='#menu_bar')
        ### menubar event handler
        self.menu_events = HandlerForMenuBarEvents(self.main_window,
                                                   self.manager)

        self.clock = pygame.time.Clock()
        self.is_running = True

    def on_event(self, event):
        # eventleri açıklamicam biraz karışık görünebilir ama max bu kadar düzenli yapabiliyom lsdkfjpedkfjg
        if event.type == pygame.QUIT:
            self.is_running = False

        self.menu_events.process_events(event, self.menu_bar,
                                        self.stream_window)

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#close_ui_button'):
            self.is_running = False

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#min_ui_button'):
            pygame.display.iconify()  # iconify = minimize

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#settings_button'):
            if self.settings_window == None:
                settings_rect = pygame.Rect((0, 0), (400, 400))
                settings_rect.bottomleft = self.settings_button.rect.topright
                self.settings_window = SettingsWindow(settings_rect,
                                                      self.manager,
                                                      self.main_window)
            else:
                self.settings_window.kill()
                self.settings_window = None

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and self.settings_window is not None and event.ui_element
                == self.settings_window.close_window_button) or (
                    event.type == pygame.USEREVENT
                    and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                    and self.settings_window is not None
                    and self.settings_window.warning_screen is not None
                    and event.ui_element
                    == self.settings_window.warning_screen.dismiss_button):
            self.settings_window.kill()
            self.settings_window = None

        if (event.type == pygame.USEREVENT
                and event.user_type == 'language_changed'
                and self.settings_window is not None):
            print("language change detected")
            self.settings_window.kill()
            self.settings_window = None
            if self.settings_window == None:
                settings_rect = pygame.Rect((0, 0), (400, 400))
                settings_rect.bottomleft = self.settings_button.rect.topright
                self.settings_window = SettingsWindow(settings_rect,
                                                      self.manager,
                                                      self.main_window)

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_element == self.fullscreen_button) or (
                    event.type == pygame.USEREVENT
                    and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                    and event.ui_element == self.unfull_button):
            if event.ui_element == self.fullscreen_button:
                self.fullscreen_button.visible = 0
                self.unfull_button.visible = 1
            else:
                self.fullscreen_button.visible = 1
                self.unfull_button.visible = 0
            pygame.display.toggle_fullscreen()
            # pygame2'yle gelmiş olması lazım yukarıdaki fonksiyonun tam ekran değilse yapar tam ekransa çıkarır
            self.settings = database.read_json()
            if self.settings['in_fullscreen'] == 'false':
                self.settings['in_fullscreen'] = 'true'
                database.write_to(self.settings)
            else:
                self.settings['in_fullscreen'] = 'false'
                database.write_to(self.settings)

        if (event.type == pygame.USEREVENT
                and event.user_type == 'changes_made'):
            self.is_running = False

        self.manager.process_events(event)

    def kill(self):
        """
        bu sınıf hariç bi yerden pygame.quit diyebilmek için fonksiyon içindeki hali
        direkt [obj].quit() deniliyo muydu bilmiyom o yüzden böyle yaptım
        """
        pygame.quit()

    def run(self):
        # main loop
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0
            # sets to 60 fps and i <b>think<\b> returns time between ticks

            for event in pygame.event.get():
                self.on_event(event)

            # camera footage
            if self.menu_events.stream_started == True:
                # processing
                if self.menu_events.processing:
                    frame, _ = vision.process_18()
                else:
                    frame = vision.show_cam()
                screen = pygame.Surface([frame.shape[0], frame.shape[1]])
                pygame.surfarray.blit_array(screen, frame)
                screen = pygame.transform.scale(
                    screen, (self.stream_window.rect.width,
                             self.stream_window.rect.height))
                self.stream_window.set_image(screen)

            self.manager.update(time_delta)

            self.main_window.blit(self.background, (0, 0))

            self.manager.draw_ui(self.main_window)

            pygame.display.update()