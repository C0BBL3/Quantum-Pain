import math
from random import choices
import numpy as np

class Qubit:
    def __init__(self, probability_vector = list([1 / math.sqrt(2), 1 / math.sqrt(2)]), name = ''):
        self.name = ' ' + name + ' '
        self.value = None
        self.entangled_pains = []
        # Initial Values (subject to change)
        self.probability_vector = probability_vector
        #self.update_probabilities()

    #def observe(self, probability_values): # Larry
        
    def update_probabilities(self):
        print(self.probability_vector)
        self.probability_for_0 = self.probability_vector[0] ** 2
        self.probability_for_1 = self.probability_vector[1] ** 2

    def __getitem__(self, value): # observe
        choice = choices([Bit(0), Bit(1)], weights = [100.0 * self.probability_for_0, 100.0 * self.probability_for_1])
        return choice