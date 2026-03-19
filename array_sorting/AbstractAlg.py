from abc import ABC, abstractmethod
from typing import List, Any
import random
import pygame

class SortingAlgorithm(ABC):

    def draw(self, draw_information, lst, d = {}):
        draw_information.window.fill(draw_information.white)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Stop execution: SPACE, Next Step: n", True, draw_information.black)
        textpos = text.get_rect(centerx=draw_information.width / 2, y=10)
        draw_information.window.blit(text, textpos)


        for i, value in enumerate(lst):
            x = draw_information.starting_x + i * draw_information.block_width
            y = draw_information.height - (value - draw_information.min_value) * draw_information.block_height

            rect = pygame.Rect(x, y, draw_information.block_width, draw_information.block_height * (value - draw_information.min_value + draw_information.max_value))
            if i in d:
                color = d[i]
                pygame.draw.rect(draw_information.window, color, rect)
            else:
                pygame.draw.rect(draw_information.window, draw_information.list_colors[i % 3], rect)

                

        pygame.display.update()

    @abstractmethod
    def sort(self, draw_information, lst, d = {}):
        """
        Executes the sorting algorithm on the provided data.
        """
        pass