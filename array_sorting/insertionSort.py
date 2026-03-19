from AbstractAlg import SortingAlgorithm
import pygame

class InsertionSort(SortingAlgorithm):

    def sort(self, draw_information, lst, d = {}):
        for i in range(1, len(lst)):
            self.draw(draw_information= draw_information, lst= lst, d = {i: draw_information.black})
            key = lst[i]
            j = i - 1
            yield True
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            while j >= 0 and key < lst[j]:        
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
            self.draw(draw_information= draw_information, lst= lst, d = {j + 1: draw_information.blue})
            yield True

