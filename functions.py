import pygame
import sys
from pygame.locals import *
from button import Button
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def show_menu():
   menu_bckgr = pygame.image.load('fon.jpg')

   show = True
   while show:
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()

      pygame.blit(menu_bckgr, (0, 0))


def update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons, graphs):
    background_image = pygame.image.load("fon.jpg").convert()
    screen.blit(background_image, [0, 0])


    if not stats.game_active:


        menu_buttons['start_button'].draw_button()
        #menu_buttons['exit_button'].draw_button()

        pygame.display.flip()
        return

    graphs.draw_graph()
    for button in game_buttons.values():
        button.draw_button()
    #game_buttons['answer_button1'].draw_button()


    scoreboard.show_score()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def check_events(settings,screen,stats, menu_buttons, scoreboard):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard)


def create_game_buttons(settingas, screen, game_buttons):
    # button1 = Button(settings, screen, '', width, height, button_colour)
    pass

def check_play_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard):

    button_clicked = menu_buttons['start_button'].rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

def check_exit_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard):

    button_clicked = menu_buttons['exit_button'].rect.collidepoint(mouse_x, mouse_y)

    if button_clicked:
        sys.exit()

def check_answers_button(settings, screen, stats, game_buttons, mouse_x, mouse_y, scoreboard):

    button1_clicked = game_buttons['answer_button1'].rect.collidepoint(mouse_x, mouse_y)
    button2_clicked = game_buttons['answer_button2'].rect.collidepoint(mouse_x, mouse_y)
    button3_clicked = game_buttons['answer_button3'].rect.collidepoint(mouse_x, mouse_y)

    if button1_clicked:
        print('True')
    elif button2_clicked:
        print('False')
    elif button3_clicked:
        print('False')