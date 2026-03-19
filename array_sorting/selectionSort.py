from AbstractAlg import SortingAlgorithm
import pygame

class SelectionSort(SortingAlgorithm):

    def sort(self, draw_information, lst, d = {}):
        size = len(lst)
        for ind in range(size - 1):
            min_index = ind

            for j in range(ind + 1, size):
                if lst[j] < lst[min_index]:
                    min_index = j
            self.draw(draw_information, lst, {min_index: draw_information.green, ind: draw_information.red})
            yield True
            lst[ind], lst[min_index] = lst[min_index], lst[ind]
            self.draw(draw_information, lst, {min_index: draw_information.red, ind: draw_information.green})
            yield True