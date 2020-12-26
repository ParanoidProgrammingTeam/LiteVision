from typing import Union, Tuple, Dict
import os

import pygame_gui
import pygame

from pygame_gui.core.drawable_shapes.rect_drawable_shape import RectDrawableShape
from pygame_gui.core.interfaces import IContainerLikeInterface
from pygame_gui.core import UIElement, UIContainer

from pygame_gui.elements import UIButton, UISelectionList, UIImage
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
            if menu_key == '#icon':
                icon_surf = pygame.image.load(
                    os.path.join('litevision', 'res', 'image_examples',
                                 'icon.png')).convert_alpha()
                self.icon = UIImage(
                    pygame.Rect(
                        (0 + GUI_OFFSET_VALUE +
                         ((48 - 32) // 2), current_y_pos + GUI_OFFSET_VALUE),
                        (32, 32)), icon_surf, self.ui_manager,
                    self.menu_bar_container, self, menu_key)
                current_y_pos += (48 + GUI_OFFSET_VALUE)
                continue

            elif menu_key == '#empty_1' or menu_key == '#empty_2':
                empty_surf = pygame.Surface((48, 48),
                                            pygame.SRCALPHA,
                                            masks=pygame.Color('#2F4F4F'))
                UIImage(
                    pygame.Rect((0 + GUI_OFFSET_VALUE, current_y_pos),
                                (48, 48)), empty_surf, self.ui_manager,
                    self.menu_bar_container, self, menu_key)
                current_y_pos += (48 + GUI_OFFSET_VALUE)
                continue

            elif menu_key == '#start_pause':
                sp_surf = pygame.Surface((48, 48),
                                         pygame.SRCALPHA,
                                         masks=pygame.Color('#2F4F4F'))
                sp_icon = pygame.image.load(
                    os.path.join('litevision', 'res', 'image_examples',
                                 'start_icon', 'start.png')).convert_alpha()
                sp_surf.blit(sp_icon, (0, 0))
                self.start_button = UIImage(
                    pygame.Rect((0 + GUI_OFFSET_VALUE, current_y_pos),
                                (48, 48)), sp_surf, self.ui_manager,
                    self.menu_bar_container, self, '#start_pause')

                current_y_pos += (48 + GUI_OFFSET_VALUE)
                continue

            elif menu_key == '#rgb_button':
                rgb_surf = pygame.Surface((48, 48),
                                          pygame.SRCALPHA,
                                          masks=pygame.Color('#2F4F4F'))
                rgb_icon = pygame.image.load(
                    os.path.join('litevision', 'res', 'image_examples',
                                 'rgb.png')).convert_alpha()
                rgb_surf.blit(rgb_icon, (0, 0))
                self.rgb_button = UIImage(
                    pygame.Rect((0 + GUI_OFFSET_VALUE, current_y_pos),
                                (48, 48)), rgb_surf, self.ui_manager,
                    self.menu_bar_container, self, '#rgb_button')

                current_y_pos += (48 + GUI_OFFSET_VALUE)
                continue

            UIButton(pygame.Rect((0 + GUI_OFFSET_VALUE, current_y_pos),
                                 (48, 48)),
                     menu_item['display_name'],
                     self.ui_manager,
                     self.menu_bar_container,
                     object_id=menu_key,
                     parent_element=self)
            current_y_pos += (48 + GUI_OFFSET_VALUE)

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

        if event.ui_object_id != '#menu_bar.#start_processing':
            menu_key = event.ui_object_id.split('.')[-1]
            menu_size = ((len(self.menu_data[menu_key]['items']) * 20) + 3)
            item_data = [(item_data['display_name'], item_key)
                         for item_key, item_data in self.menu_data[menu_key]
                         ['items'].items()]

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

    def process_event(self, event: pygame.event.Event
                      ):  # -> bool # pylinter desteklemiyor düzeltirsin burayı
        consumed_event = False
        if (self is not None and event.type == pygame.MOUSEBUTTONDOWN
                and event.button in [pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT]):
            scaled_mouse_pos = (int(event.pos[0] *
                                    self.ui_manager.mouse_pos_scale_factor[0]),
                                int(event.pos[1] *
                                    self.ui_manager.mouse_pos_scale_factor[1]))
            if self.hover_point(scaled_mouse_pos[0], scaled_mouse_pos[1]):
                consumed_event = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            scaled_mouse_pos = self.start_button.ui_manager.calculate_scaled_mouse_position(
                event.pos)
            x = scaled_mouse_pos[0]
            y = scaled_mouse_pos[1]

            if self.start_button.hover_point(x, y):
                event_data = {
                    'user_type': pygame_gui.UI_BUTTON_START_PRESS,
                    'ui_element': self.start_button,
                    'ui_object_id': self.start_button.most_specific_combined_id
                }
                pygame.event.post(
                    pygame.event.Event(pygame.USEREVENT, event_data))

            elif self.rgb_button.hover_point(x, y):
                event_data = {
                    'user_type': pygame_gui.UI_BUTTON_START_PRESS,
                    'ui_element': self.rgb_button,
                    'ui_object_id': self.rgb_button.most_specific_combined_id
                }
                pygame.event.post(
                    pygame.event.Event(pygame.USEREVENT, event_data))

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
                and event.ui_element in self.menu_bar_container.elements
                and event.ui_object_id != '#menu_bar.#start_pause'
                and event.ui_object_id != '#menu_bar.#rgb_button'):

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