import pygame
import sys
from pygame.locals import *
from button import Button
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def update_screen(settings, screen, stats, menu_buttons, scoreboard, game_buttons1, game_buttons2, game_buttons3, graphs1, graphs2, graphs3):
    background_image = pygame.image.load("fon.jpg").convert()
    screen.blit(background_image, [0, 0])


    if not stats.game_active:
        for menu_button in menu_buttons:
            menu_button.draw_button()
        #menu_buttons['start_button'].draw_button()
        #menu_buttons['exit_button'].draw_button()

        pygame.display.flip()
        return

    if stats.level1:
        graphs1.draw_graph()

        for game_button1 in game_buttons1:
            game_button1.draw_button()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('level1', True, (250, 250, 50), (50, 50, 250))
        textRect = text.get_rect()
        textRect.center = (400, 400)
        screen.blit(text, textRect)
        pygame.display.flip()

    if stats.level2:
        graphs2.draw_graph()

        for game_button2 in game_buttons2:
            game_button2.draw_button()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('level2', True, (250, 250, 50), (50, 50, 250))
        textRect = text.get_rect()
        textRect.center = (400, 400)
        screen.blit(text, textRect)

        # graphs1.kill()

        for game_button1 in game_buttons1:
            game_button1.kill()

    if stats.level3:
        graphs3.draw_graph()

        for game_button3 in game_buttons3:
            game_button3.draw_button()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('level3', True, (250, 250, 50), (50, 50, 250))
        textRect = text.get_rect()
        textRect.center = (400, 400)
        screen.blit(text, textRect)

        for game_button2 in game_buttons2:
            game_button2.kill()

        # graphs2.kill()


    # Отрисовка графиков

    # graphs.draw_graph()
    # graphs1.draw_graph()
    #graphs2.draw_graph()


    scoreboard.show_score()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def check_events(settings, screen, stats, menu_buttons, game_buttons1, game_buttons2, game_buttons3, scoreboard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not stats.game_active:
            for menu_button in menu_buttons:
                menu_button.handle_event(event)
            return

        if stats.level1 and stats.game_active:
            for game_button in game_buttons1:
                game_button.handle_event(event)
            return

        if stats.level2 and stats.game_active:
            for game_button in game_buttons2:
                game_button.handle_event(event)

        if stats.level3:
            for game_button in game_buttons3:
                game_button.handle_event(event)



def start_game(stats, settings, scoreboard):
    stats.reset_stats()
    stats.game_active = True
    stats.level1 = True

def exit_game(stats, settings, scoreboard):
    sys.exit()


# Correct Buttons
def correct_button_l1(stats, settings, scoreboard):
    stats.score += settings.correct_points
    scoreboard.prep_score()

    stats.level1 = False
    stats.level2 = True

    settings.true_sound.play()

def correct_button_l2(stats, settings, scoreboard):
    stats.score += settings.correct_points
    scoreboard.prep_score()

    stats.level2 = False
    stats.level3 = True

    settings.true_sound.play()

def correct_button_l3(stats, settings, scoreboard):
    stats.score += settings.correct_points
    scoreboard.prep_score()

    settings.true_sound.play()


# Wrong Buttons
def wrong_button_l1(stats, settings, scoreboard):
    stats.level1 = False
    stats.level2 = True

    settings.false_sound.play()

def wrong_button_l2(stats, settings, scoreboard):
    stats.level2 = False
    stats.level3 = True

    settings.false_sound.play()

def wrong_button_l3(stats, settings, scoreboard):
    settings.false_sound.play()

def skip_game(stats, settings, scoreboard):
    if stats.level1:
        stats.level1 = False
        stats.level2 = True
    elif stats.level2:
        stats.level2 = False
        stats.level3 = True
