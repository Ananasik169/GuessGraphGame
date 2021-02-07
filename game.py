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

    #x1,y1





    # Creating graph objects




    scoreboard = Scoreboard(settings, screen, stats)

    pygame.display.set_caption("Graph")
    pygame.display.set_icon(pygame.image.load("stocks.bmp"))

    # Menu buttons
    start_button = Button(settings, screen, stats, scoreboard, (400, 250), 'Start', (0, 100, 0), callback=start_game)
    exit_button = Button(settings, screen, stats, scoreboard, (400, 350), 'Exit', (100, 0, 0),  callback=exit_game)

    # Game buttons

    # level1 game elements

    # buttons
    skip_button1 = Button(settings, screen, stats, scoreboard, (400, 550), 'Skip', (0, 0, 100), callback=skip_game)

    answer_button1 = Button(settings, screen, stats, scoreboard, (200, 500), 'Answer 1', (0, 0, 50),
                            callback=wrong_button_l1)
    answer_button2 = Button(settings, screen, stats, scoreboard, (400, 500), 'Answer 2', (0, 0, 50),
                            callback=correct_button_l1)
    answer_button3 = Button(settings, screen, stats, scoreboard, (600, 500), 'Answer 3', (0, 0, 50),
                            callback=wrong_button_l1)
    # data
    x1 = np.linspace(-2, 2, 100)
    y1 = (x1 ** 3)

    z1 = np.around(np.arange(-10, 10, 1), decimals=4)
    k1 = (z1 ** 2)

    a1 = np.around(np.arange(-10, 10, 1), decimals=4)
    b1 = a1

    #graph
    graphs1 = Graph(x1, y1, z1, k1, a1, b1, screen)

    # level2_game_elements

    # buttons
    skip_button2 = Button(settings, screen, stats, scoreboard, (400, 550), 'Skip', (0, 0, 100), callback=skip_game)

    answer_button4 = Button(settings, screen, stats, scoreboard, (200, 500), 'Answer 1', (0, 0, 50),
                            callback=correct_button_l2)
    answer_button5 = Button(settings, screen, stats, scoreboard, (400, 500), 'Answer 2', (0, 0, 50),
                            callback=wrong_button_l2)
    answer_button6 = Button(settings, screen, stats, scoreboard, (600, 500), 'Answer 3', (0, 0, 50),
                            callback=wrong_button_l2)
    # data
    x2 = np.around(np.arange(-10, 10, 1), decimals=4)
    y2 = np.sin(x2)

    z2 = np.around(np.arange(-10, 10, 1), decimals=4)
    k2 = np.exp(z2)

    a2 = np.around(np.arange(-10, 10, 1), decimals=4)
    b2 = np.cos(a2)

    #graphs
    graphs2 = Graph(x2, y2, z2, k2, a2, b2, screen)

    # level3_game_elements

    #buttons
    skip_button3 = Button(settings, screen, stats, scoreboard, (400, 550), 'Skip', (0, 0, 100), callback=skip_game)

    answer_button7 = Button(settings, screen, stats, scoreboard, (200, 500), 'Answer 1', (0, 0, 50),
                            callback=wrong_button_l3)
    answer_button8 = Button(settings, screen, stats, scoreboard, (400, 500), 'Answer 2', (0, 0, 50),
                            callback=wrong_button_l3)
    answer_button9 = Button(settings, screen, stats, scoreboard, (600, 500), 'Answer 3', (0, 0, 50),
                            callback=correct_button_l3)
    # data

    x3 = np.around(np.arange(-10, 10, 1), decimals=4)
    y3 = np.log(x3)

    z3 = np.around(np.arange(-10, 10, 1), decimals=4)
    k3 = np.sqrt(z3)

    a3 = np.around(np.arange(-10, 10, 1), decimals=4)
    b3 = np.cbrt(a3)

    # graphs
    graphs3 = Graph(x3, y3, z3, k3, a3, b3, screen)


    menu_buttons = Group(start_button, exit_button)

    game_buttons1 = Group(answer_button1, answer_button2, answer_button3, skip_button1)
    game_buttons2 = Group(answer_button4, answer_button5, answer_button6, skip_button2)
    game_buttons3 = Group(answer_button7, answer_button8, answer_button9, skip_button3)

    while True:
        update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons1, game_buttons2, game_buttons3, graphs1, graphs2, graphs3)

        # if stats.game_active:

        # draw_graphs
        # if stats.game_active:
        # for button in game_buttons1:
        # button.draw_button()
        check_events(settings, screen, stats, menu_buttons, game_buttons1, scoreboard)


run_game()
