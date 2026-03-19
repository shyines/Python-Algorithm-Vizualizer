# Example file showing a basic pygame "game loop"
import pygame
import random
import drawInformation
from bubblesort import BubbleSort
from insertionSort import InsertionSort
from selectionSort import SelectionSort

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

def generate_list(max_value, min_value, no_elements):
    lst = []
    for _ in range(no_elements):
        random_value = random.randint(min_value, max_value)
        lst.append(random_value)
    return lst

pygame.init()
clock = pygame.time.Clock()
running = True

sorting_algs = {
    "bubble sort": BubbleSort(),
    "inserton sort" : InsertionSort(),
    "selection sort" : SelectionSort()
}


name_of_alg = "bubble sort"
sorting_alg = sorting_algs[name_of_alg]
lst = generate_list(100, 1, 100)
draw_information = drawInformation.DrawInformations(SCREEN_WIDTH, SCREEN_HEIGHT, lst)
active_alg = sorting_alg.sort(draw_information, lst)

def change_algorithm(lst, alg_name):
    lst = original_lst
    current_alg_name = "inserton sort"
    sorting_alg = sorting_algs[current_alg_name]
    active_alg = sorting_alg.sort(draw_information, lst)
    return active_alg

original_lst = lst
sorting = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorting = not sorting   
            if event.key == pygame.K_n:
                next(active_alg)   
            if event.key == pygame.K_b:
                active_alg = change_algorithm(lst, "bubble sort")
                print("algorithm changed: bubble sort")
            elif event.key == pygame.K_i:
                active_alg = change_algorithm(lst, "insertion sort")
                print("algorithm changed: insertion sort")
            elif event.key == pygame.K_s:
                active_alg = change_algorithm(lst, "selection sort")
                print("algorithm changed: selection sort")
    
    if(sorting):
        next(active_alg)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()