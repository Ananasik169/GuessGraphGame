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

   z = np.around(np.arange(-10, 10, 1), decimals=4)
   k = (z**2)

   a = np.around(np.arange(-10, 10, 1), decimals=4)
   b = a

   # Creating graph objects

   graphs = Graph(x, y, z, k, a, b, screen)

   scoreboard = Scoreboard(settings, screen, stats)

   pygame.display.set_caption("Graphics")
   pygame.display.set_icon(pygame.image.load("stocks.bmp"))


   start_button = Button(settings, screen, stats, (200, 200), 'Start', (0, 100, 0), callback=start_game)
   #start_button = Button(settings, screen, (200, 200), 'Start', (0, 100, 0), callback=lambda: start_game(stats))
   #def __init__(self, settings, screen, stats, pos, msg, button_colour, callback)
   # All game buttons
   #exit_button = Button(settings, screen, 'Exit', (100, 0, 0), callback=create_game_buttons())

   #skip_button = Button(settings, screen, 'Skip', (0, 0, 100))


   # Answer buttons
   answer_button1 = Button(settings, screen, stats, (200, 200) , 'Answer 1', (0, 0, 50), callback=start_game)
   answer_button2 = Button(settings, screen, stats, (200, 200) ,'Answer 2', (0, 0, 50), callback=start_game)
   answer_button3 = Button(settings, screen, stats, (200, 200) ,'Answer 3', (0, 0, 50), callback=start_game)

   #menu_buttons = {'exit_button': exit_button, 'start_button': start_button}
   #game_buttons = {'answer_button1': answer_button1, 'answer_button2': answer_button2, 'answer_button3': answer_button3}

   #menu_buttons = Group(exit_button, start_button)
   menu_buttons = Group(start_button)
   game_buttons = Group(answer_button1, answer_button2, answer_button3)



   while True:
      update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons, graphs)

      #if stats.game_active:

      #draw_graphs
      #if stats.game_active:
         #for button in game_buttons:
            #button.draw_button()
      check_events(settings, screen, stats, menu_buttons, game_buttons, scoreboard)

run_game()
