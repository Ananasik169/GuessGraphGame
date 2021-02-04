import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group
# import numpy
import matplotlib
import numpy as np
from functions import *
# from button import Button_start
from button import Button
from settings import Settings
from stats import GameStats
from scoreboard import Scoreboard
from graph import Graph

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


def run_game():
    pygame.init()

    # Запускает matlotlib во встроенном режиме
    matplotlib.use("Agg")

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen_rect = screen.get_rect()
    stats = GameStats(settings)

    # Generating Data
    np.seterr(divide='ignore', invalid='ignore')

    # Данные для графиков

    x = np.linspace(-2, 2, 100)
    y = (x ** 3)

    x1 = np.around(np.arange(-10, 10, 1), decimals=4)
    y1 = np.sin(x1)

    x2 = np.around(np.arange(-10, 10, 1), decimals=4)
    y2 = np.log(x2)

    z = np.around(np.arange(-10, 10, 1), decimals=4)
    k = (z ** 2)

    z1 = np.around(np.arange(-10, 10, 1), decimals=4)
    k1 = np.exp(z1)

    z2 = np.around(np.arange(-10, 10, 1), decimals=4)
    k2 = np.sqrt(z2)

    a = np.around(np.arange(-10, 10, 1), decimals=4)
    b = a

    a1 = np.around(np.arange(-10, 10, 1), decimals=4)
    b1 = np.cos(a1)

    a2 = np.around(np.arange(-10, 10, 1), decimals=4)
    b2 = np.cbrt(a2)

    # Creating graph objects

    graphs = Graph(x, y, z, k, a, b, screen)
    graphs1 = Graph(x1, y1, z1, k1, a1, b1, screen)
    graphs2 = Graph(x2, y2, z2, k2, a2, b2, screen)

    scoreboard = Scoreboard(settings, screen, stats)

    pygame.display.set_caption("Graphics")
    pygame.display.set_icon(pygame.image.load("stocks.bmp"))

    # Menu buttons
    start_button = Button(settings, screen, stats, scoreboard, (400, 250), 'Start', (0, 100, 0), callback=start_game)
    exit_button = Button(settings, screen, stats, scoreboard, (400, 350), 'Exit', (0, 100, 0),  callback=exit_game)

    # Game buttons
    answer_button1 = Button(settings, screen, stats, scoreboard, (200, 500), 'Answer 1', (0, 0, 50),
                            callback=wrong_button)
    answer_button2 = Button(settings, screen, stats, scoreboard, (400, 500), 'Answer 2', (0, 0, 50),
                            callback=correct_button)
    answer_button3 = Button(settings, screen, stats, scoreboard, (600, 500), 'Answer 3', (0, 0, 50),
                            callback=wrong_button)
    skip_button = Button(settings, screen, stats, scoreboard, (400, 550), 'Skip', (0, 0, 100), callback=exit_game)

    menu_buttons = Group(start_button, exit_button)
    game_buttons = Group(answer_button1, answer_button2, answer_button3, skip_button)

    while True:
        update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons, graphs, graphs1, graphs2)

        # if stats.game_active:

        # draw_graphs
        # if stats.game_active:
        # for button in game_buttons:
        # button.draw_button()
        check_events(settings, screen, stats, menu_buttons, game_buttons, scoreboard)


run_game()
