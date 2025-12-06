import random
import numpy as np

from numpy.matlib import zeros


class Board:
    def __init__(self, rows:int=10, cols:int=10):
        self.mines_array = np.zeros((cols, rows))
        self.width = cols
        self.height = rows

    def fill_mines_array(self):
        randomines: int = 0
        for i in range(self.width):
            for j in range(self.height):
                if random.random() < 0.33:
                    randomines = 1
                self.mines_array[i, j] = randomines
                randomines = 0
        print(self.mines_array)

    def mark_cell(self):
        ...

    def compute_numbers(self):
        ...



class Cell:
    def __int__(self):
        self.siblings = []
        self.value = 0 # -1

    def compute_number(self):
        count = 0
        for sibling in self.siblings:
            if sibling.isMine():
                count +=1

        self.value = count

    def isMine(self):
        return self.value == -1


