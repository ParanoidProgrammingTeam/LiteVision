"""
~~~~~~~~~~~~~~~~~~~~~~~~~TODO~~~~~~~~~~~~~~~~~~~~~~~~~~
- I just started I don't even know lol
- Settings Window [~20%]
- Stream Window [~0%]
- This Class [~15%]
- Menu Bar or Side Menu Bar [~10%]
- a lot more
- MAKE A KEEP CHANGES BUTTON TO SETTINGS WINDOW SO ITS NOT SO MIND KILLING SPDKJFDPFKJ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import os
import pygame
import pygame_gui
from pygame_gui.elements.ui_button import UIButton

import litevision.lib.database as database
from litevision.res.glob import *
from litevision.lib.interface import SettingsWindow, MenuBar, HandlerForMenuBarEvents


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

        title_icon = pygame.image.load(
            os.path.join('litevision', 'res', 'image_examples', 'icon32x.png'))
        pygame.display.set_icon(title_icon)

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
        theme_path = os.path.join('litevision', 'res', 'theme.json')
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

        ## windows
        ### settings window
        self.settings_window = None

        ### stream window
        #### self.stream_window = StreamWindow()

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
        if event.type == pygame.QUIT:
            self.is_running = False

        self.menu_events.process_events(event, self.menu_bar)

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#close_ui_button'):
            self.is_running = False

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#min_ui_button'):
            pygame.display.iconify()

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and event.ui_object_id == '#settings_button'):
            if self.settings_window == None:
                settings_rect = pygame.Rect((0, 0), (400, 400))
                settings_rect.bottomleft = self.settings_button.rect.topright
                self.settings_window = SettingsWindow(settings_rect,
                                                      self.manager)
            else:
                self.settings_window.kill()
                self.settings_window = None

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                and self.settings_window is not None and event.ui_element
                == self.settings_window.close_window_button):
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
                                                      self.manager)

        if (event.type == pygame.USEREVENT
                and event.user_type == 'fullscreen_toggled'):
            pygame.display.toggle_fullscreen()

        if (event.type == pygame.USEREVENT
                and event.user_type == 'changes_made'):
            self.is_running = False

        self.manager.process_events(event)

    def kill(self):
        print("going dark")
        pygame.quit()

    def run(self):
        # main loop
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0
            # sets to 60 fps and i <b>think<\b> returns time between ticks

            for event in pygame.event.get():
                self.on_event(event)

            self.manager.update(time_delta)

            self.main_window.blit(self.background, (0, 0))

            self.manager.draw_ui(self.main_window)

            pygame.display.update()