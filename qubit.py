import math
from random import choices
import Bit
import numpy as np

class Qubit:
    def __init__(self, probability_vector = [(1 / (math.sqrt(2))), (1 / (math.sqrt(2)))]):
        self.value = None
        self.entangled_pains = []
        # Initial Values (subject to change)
        self.probability_vector = np.array(probability_vector)
        self.update_probabilities()

    #def observe(self, probability_values): # Larry
        

    def update_probabilities(self):
        self.probability_for_0 = math.abs(self.probability_vector[0]) ^ 2
        self.probability_for_1 = math.abs(self.probability_vector[1]) ^ 2

    def __getitem__(self, value):
        choice = choices([Bit(0), Bit(1)], [self.probability_for_0, self.probability_for_1])
        return choice