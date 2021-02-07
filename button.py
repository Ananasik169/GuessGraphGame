from pygame.sprite import Sprite
import pygame


class Button(Sprite):

    def __init__(self, settings, screen, stats, sb, pos, msg, button_colour, callback):

        super().__init__()
        # Callback - функция при нажатии кнопки
        self.callback = callback
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pos = pos
        self.stats = stats

        self.settings = settings

        # Настройки

        self.width = settings.button_width
        self.height = settings.button_height

        self.button_color = button_colour
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.scoreboard = sb

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # self.rect.center = self.screen_rect.center
        self.rect.center = self.pos

        self.callback = callback
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def handle_event(self, event):
        """Обработка событий, передаваемых в цикле обработки событий"""
        # Если событие нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если нажата левая кнопка мыши
            if event.button == 1:
                # Проверка наличия коллизии кординатов нажатия мыши и кнопки
                if self.rect.collidepoint(event.pos):
                    # Изменение изображения на кнопке
                    self.image = self.settings.button_down_image
                    self.callback(self.stats, self.settings, self.scoreboard)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.image = self.msg_image
                if self.rect.collidepoint(event.pos):
                    print('Button pressed.')
                    # Вызов функции переданной при инциализации класса
                    # (при создании объекта)

    def die(self):
        self.kill()
