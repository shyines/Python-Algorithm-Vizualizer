import pygame

class DrawInformations:
    
    black = 0, 0, 0
    white = 255, 255, 255
    grey = 128, 128, 128
    green = 0, 255, 0
    red = 255, 0, 0
    blue = 0, 0, 255

    list_colors = [
        (128, 128, 128),
        (150, 150, 150),
        (200, 200, 200)
    ]

    PADDING = 100
    TOP_PADDING = 100



    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))

        self.set_list(lst)

    def set_list(self, lst):
        self.max_value = max(lst)
        self.min_value = min(lst)
        self.block_width = round((self.width - self.PADDING) / len(lst))
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_value - self.min_value))
        self.starting_x = self.PADDING//2