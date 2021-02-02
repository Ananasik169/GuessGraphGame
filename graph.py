import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pygame

class Graph():

    def __init__(self, x, y, z, k, a, b, screen):

        self.x = x
        self.y = y
        self.z = z
        self.k = k
        self.a = a
        self.b = b
        self.screen = screen

    def draw_graph(self):

        fig, (ax1, ax2, ax3) = plt.subplots(
            nrows=1, ncols=3,
            figsize=(8, 4)
        )

        ax1.plot(self.x, self.y)
        ax1.spines['left'].set_position('center')
        ax1.spines['bottom'].set_position('center')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)

        ax2.plot(self.z, self.k)
        ax2.spines['left'].set_position('center')
        ax2.spines['bottom'].set_position('center')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)

        ax3.plot(self.a, self.b)
        ax3.spines['left'].set_position('center')
        ax3.spines['bottom'].set_position('center')
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)

        # Добавление графика fig на холст
        canvas = agg.FigureCanvasAgg(fig)



        # Отрисовка холста
        canvas.draw()

        # Рендер
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        self.screen.blit(surf, (0, 0))
