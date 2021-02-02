from pygame.sprite import Sprite
import pygame


# class Button(Sprite):
#
#     def __init__(self, screen, width, height, inactive_color, active_color):
#         super().__init__()
#
#         self.width = width
#         self.height = height
#         self.inactive_color = inactive_color
#         self.active_color = active_color
#         self.screen = screen
#
#     def draw(self, x, y, msg, action=None):
#         mouse = pygame.mouse.get_pos()
#         click = pygame.mouse.get_pressed()
#
#         if x < mouse[0] < x + self.width:
#             if y < mouse[1] < y + self.height:
#                 pygame.draw.rect(self.screen, self.active_color, x, y, self.width, self.rect)
#
#                 if click[0] == 1 and action is not None:
#                     action()
#
#         else:
#             pygame.draw.rect(self.screen, self.inactive_color, x, y, self.width, self.rect)



class Button(Sprite):

    def __init__(self, settings, screen, msg, button_colour):

        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = settings

        # Настройки

        self.width = settings.button_width
        self.height = settings.button_height

        self.button_color = button_colour
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
