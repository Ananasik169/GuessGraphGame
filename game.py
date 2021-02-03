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

   # x, y
   x = np.linspace(-2, 2, 100)
   y = (x ** 3)

   x1 = np.around(np.arange(0, 10, 1), decimals=4)
   y1 = np.sin(x1)

   x2 = np.around(np.arange(-10, 10, 1), decimals=4)
   y2 = np.cbrt(x2)

   # z, k
   z = np.around(np.arange(-10, 10, 1), decimals=4)
   k = (z**2)

   z1 = np.around(np.arange(0, 10, 1), decimals=4)
   k1 = np.sqrt(z1)

   z2 = np.around(np.arange(-10, 10, 1), decimals=4)
   k2 = np.cos(z2)

   #a, b
   a = np.around(np.arange(-10, 10, 1), decimals=4)
   b = a

   a1 = np.around(np.arange(-10, 10, 1), decimals=4)
   b1 = np.exp(a1)

   a2 = np.around(np.arange(-10, 10, 1), decimals=4)
   b2 = np.log(a2)

   # Creating graph objects

   graph1 = Graph(x, y, z, k, a, b, screen)
   graph2 = Graph(x1, y1, z1, k1, a1, b1, screen)
   graph3 = Graph(x2, y2, z2, k2, a2, b2, screen)

   scoreboard = Scoreboard(settings, screen, stats)

   pygame.display.set_caption("Graphics")
   pygame.display.set_icon(pygame.image.load("stocks.bmp"))


   start_button = Button(settings, screen, stats, scoreboard, (400, 200), 'Start', (0, 100, 0), callback=start_game)

   # All game buttons
   exit_button = Button(settings, screen, stats, scoreboard, (400, 400), 'Exit', (100, 0, 0), callback=exit_game)

   #skip_button = Button(settings, screen, 'Skip', (0, 0, 100))


   # Answer buttons
   answer_button1 = Button(settings, screen, stats, scoreboard, (200, 500), 'Answer 1', (0, 0, 250), callback=wrong_button)
   answer_button2 = Button(settings, screen, stats, scoreboard, (400, 500), 'Answer 2', (0, 0, 250), callback=correct_button)
   answer_button3 = Button(settings, screen, stats, scoreboard, (600, 500), 'Answer 3', (0, 0, 250), callback=wrong_button)

   #menu_buttons = {'exit_button': exit_button, 'start_button': start_button}
   #game_buttons = {'answer_button1': answer_button1, 'answer_button2': answer_button2, 'answer_button3': answer_button3}

   menu_buttons = Group(exit_button, start_button)
   game_buttons = Group(answer_button1, answer_button2, answer_button3)



   while True:
      update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons, graph1, graph2, graph3)

      #if stats.game_active:

      #draw_graphs
      #if stats.game_active:
         #for button in game_buttons:
            #button.draw_button()
      check_events(settings, screen, stats, menu_buttons, game_buttons, scoreboard)

run_game()
