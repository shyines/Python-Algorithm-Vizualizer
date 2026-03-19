from AbstractAlg import SortingAlgorithm
import pygame

class BubbleSort(SortingAlgorithm):


    def sort(self, draw_information, lst):
        n = len(lst)
        
        # Traverse through all array elements
        for i in range(n):
            swapped = False

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                self.draw(draw_information, lst, {j: draw_information.green, j + 1: draw_information.red})
                yield True
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swapped = True
                    self.draw(draw_information, lst, {j: draw_information.red, j + 1: draw_information.green})
                    yield True
            if (swapped == False):
                break
