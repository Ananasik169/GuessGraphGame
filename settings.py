import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.correct_points = 50

        self.button_height = 30
        self.button_width = 100

        #self.menu_button_height = 30
        #self.menu_button_width = 100

        # Звуки
        true_sound = pygame.mixer.Sound('malenkaya-pobeda-4567.ogg')
        false_sound = pygame.mixer.Sound('zvuk-eta-dver-zablokirovana-4491.ogg')
