import pygame
import sys
from pygame.locals import *
from button import Button
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons, graphs):
    background_image = pygame.image.load("fon.jpg").convert()
    screen.blit(background_image, [0, 0])

    if not stats.game_active:
        for menu_button in menu_buttons:
            menu_button.draw_button()
        #menu_buttons['start_button'].draw_button()
        #menu_buttons['exit_button'].draw_button()

        pygame.display.flip()
        return

    graphs.draw_graph()
    for game_button in game_buttons:
        game_button.draw_button()


    scoreboard.show_score()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def check_events(settings, screen, stats, menu_buttons, game_buttons, scoreboard):

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         mouse_x, mouse_y = pygame.mouse.get_pos()
    #         check_play_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        for menu_button in menu_buttons:
            menu_button.handle_event(event)

        for game_button in game_buttons:
            game_button.handle_event(event)


def create_game_buttons():
    # button1 = Button(settings, screen, '', width, height, button_colour)
    pass

def start_game(stats):
    stats.reset_stats()
    stats.game_active = True


def exit_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard):

    button_clicked = menu_buttons['exit_button'].rect.collidepoint(mouse_x, mouse_y)

    if button_clicked:
        sys.exit()

def skip_button(settings, screen, stats, menu_buttons, mouse_x, mouse_y, scoreboard):
    pass
