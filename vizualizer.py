# Example file showing a basic pygame "game loop"
import pygame
import random

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


def generate_list(max_value, min_value, no_elements):
    lst = []
    for _ in range(no_elements):
        random_value = random.randint(min_value, max_value)
        lst.append(random_value)
    return lst



def draw(draw_information, lst, d = {}):
    draw_information.window.fill(draw_information.white)
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



def bubble_sort(draw_information, lst):
    n = len(lst)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            draw(draw_information, lst, {j: draw_information.green, j + 1: draw_information.red})
            yield True
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
                draw(draw_information, lst, {j: draw_information.red, j + 1: draw_information.green})
                yield True
        if (swapped == False):
            break


pygame.init()
clock = pygame.time.Clock()
running = True

lst = generate_list(100, 1, 100)
draw_information = DrawInformations(1280, 720, lst)

sorting_alg = bubble_sort(draw_information, lst)
sorting = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorting = not sorting   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                next(sorting_alg)   
    
    if(sorting):
        next(sorting_alg)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()