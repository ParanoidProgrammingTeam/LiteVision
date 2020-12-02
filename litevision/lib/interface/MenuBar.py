from typing import Union, Tuple, Dict

import pygame
import pygame_gui

from pygame_gui.core import UIElement, UIContainer
from pygame_gui.core.drawable_shapes.rect_drawable_shape import RectDrawableShape
from pygame_gui.core.interfaces import IContainerLikeInterface

from pygame_gui.elements import UIButton, UISelectionList
from litevision.res.glob import *


class MenuBar(UIElement):
    """
    Menubar sınıfı. İçinde menuler ve alt menuler içeren ui elemanı
    
    :param rect: elemanın pygame.Rect'i
    :param manager: ui yöneticisi
    :param menu_bar_data: bardaki menulerin ve alt menülerin bulunduğu dict
    :param container: bu elemanın neyin içinde olduğu
    :param parent: bu objenin 'sahibi' olan eleman
    :param object_id: objeye atanacak id
    :param anchors: objenin rect koordinatının nereye göre olduğunu bildiren dict
    """
    def __init__(self,
                 rect: pygame.Rect,
                 manager,
                 container: Union[IContainerLikeInterface, None] = None,
                 parent: Union[UIElement, None] = None,
                 object_id: Union[str, None] = None,
                 anchors: Union[Dict[str, str], None] = None,
                 menu_bar_data: Dict[str,
                                     Dict[str,
                                          Union[Dict,
                                                str]]] = MENU_BAR_DATA_DICT):
        super().__init__(rect,
                         manager,
                         container,
                         starting_height=1,
                         layer_thickness=1,
                         anchors=anchors)
        self._create_valid_ids(container, parent, object_id, 'menu_bar')

        self.menu_data = menu_bar_data

        self.bg_color = None
        self.border_color = None
        self.shape_type = 'rectangle'

        self.rgb_tuple = None  # type: Union[Tuple[int, int, int], None]

        self.open_menu = None
        self._selected_menu = None

        self._close_opened_menu = False

        self.rebuild_from_changed_theme_data()

        self.container_rect = pygame.Rect(
            self.relative_rect.left + (self.shadow_width + self.border_width),
            self.relative_rect.top + (self.shadow_width + self.border_width),
            self.relative_rect.width - 2 *
            (self.shadow_width + self.border_width),
            self.relative_rect.height - 2 *
            (self.shadow_width + self.border_width))
        self.menu_bar_container = UIContainer(self.container_rect,
                                              manager,
                                              starting_height=1,
                                              parent_element=self,
                                              object_id='#menu_bar_container')

        # menü butonları için for loop
        current_y_pos = 0
        for menu_key, menu_item in self.menu_data.items():
            UIButton(pygame.Rect((0 + GUI_OFFSET_VALUE, current_y_pos),
                                 (48, 48)),
                     menu_item['display_name'],
                     self.ui_manager,
                     self.menu_bar_container,
                     object_id=menu_key,
                     parent_element=self)
            current_y_pos += 48

    def unfocus(self):
        if self.open_menu is not None:
            self.open_menu.kill()
            self.open_menu = None
        if self._selected_menu is not None:
            self._selected_menu.unselect()
            self._selected_menu = None

    def kill(self):
        self.menu_bar_container.kill()
        super().kill()

    def _open_menu(self, event):
        if self.open_menu is not None:
            self.open_menu.kill()
        menu_key = event.ui_object_id.split('.')[-1]
        menu_size = ((len(self.menu_data[menu_key]['items']) * 20) + 3)
        item_data = [(item_data['display_name'], item_key) for item_key,
                     item_data in self.menu_data[menu_key]['items'].items()]
        menu_rect = pygame.Rect((0, 0), (200, menu_size))
        menu_rect.topleft = event.ui_element.rect.topright
        top_ui_layer = self.ui_manager.get_sprite_group().get_top_layer()
        self.open_menu = UISelectionList(menu_rect,
                                         item_data,
                                         self.ui_manager,
                                         starting_height=top_ui_layer,
                                         parent_element=self,
                                         object_id=menu_key + '_items')
        self.ui_manager.set_focus_set(self)

    def rebuild_from_changed_theme_data(self):
        has_any_changed = False

        bg_color = self.ui_theme.get_colour_or_gradient(
            'normal_bg', self.combined_element_ids)
        if bg_color != self.bg_color:
            self.bg_color = bg_color
            has_any_changed = True

        border_color = self.ui_theme.get_colour_or_gradient(
            'normal_border', self.combined_element_ids)
        if border_color != self.border_color:
            self.border_color = border_color
            has_any_changed = True

        # misc
        shape_type_str = self.ui_theme.get_misc_data('shape',
                                                     self.combined_element_ids)
        if (shape_type_str is not None and shape_type_str in ['rectangle']
                and shape_type_str != self.shape_type):
            self.shape_type = shape_type_str
            has_any_changed = True

        if self._check_shape_theming_changed(defaults={
                'border_width': 1,
                'shadow_width': 0,
                'shape_corner_radius': 0
        }):
            has_any_changed = True

        if has_any_changed:
            self.rebuild()

    def rebuild(self):
        theming_parameters = {
            'normal_bg': self.bg_color,
            'normal_border': self.border_color,
            'border_width': self.border_width,
            'shadow_width': self.shadow_width
        }

        if self.shape_type == 'rectangle':
            self.drawable_shape = RectDrawableShape(self.rect,
                                                    theming_parameters,
                                                    ['normal'],
                                                    self.ui_manager)

        self.on_fresh_drawable_shape_ready()

    def process_event(self, event: pygame.event.Event) -> bool:
        consumed_event = False
        if (self is not None and event.type == pygame.MOUSEBUTTONDOWN
                and event.button in [pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT]):
            scaled_mouse_pos = (int(event.pos[0] *
                                    self.ui_manager.mouse_pos_scale_factor[0]),
                                int(event.pos[1] *
                                    self.ui_manager.mouse_pos_scale_factor[1]))
            if self.hover_point(scaled_mouse_pos[0], scaled_mouse_pos[1]):
                consumed_event = True

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED
                and event.ui_element in self.menu_bar_container.elements
                and self.open_menu != None):
            if self._selected_menu is not None:
                self._selected_menu.unselect()
            self._selected_menu = event.ui_element
            self._selected_menu.select()
            self._open_menu(event)

        if (event.type == pygame.USEREVENT
                and event.user_type == pygame_gui.UI_BUTTON_START_PRESS
                and event.ui_element in self.menu_bar_container.elements):
            if self._selected_menu is not None:
                self._selected_menu.unselect()
            self._selected_menu = event.ui_element
            self._selected_menu.select()
            self._open_menu(event)
        return consumed_event

    def update(self, time_delta):
        super().update(time_delta)
        if self.menu_bar_container.layer_thickness != self.layer_thickness:
            self.layer_thickness = self.menu_bar_container.layer_thickness