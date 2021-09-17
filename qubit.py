import math
from random import choices
import Bit
import numpy as np

class Qubit:
    def __init__(self):
        self.value = None
        self.entangled_pains = []
        # Initial Values (subject to change)
        self.probability_vector = np.array([(1 / (math.sqrt(2))), (1 / (math.sqrt(2)))])
        self.update_probabilities()

    #def observe(self, probability_values): # Larry
        

    def update_probabilities(self):
        self.probability_for_0 = sum([math.abs(value) ^ 2 for value in self.probability_vector]) 
        self.probability_for_1 = 1.0 - self.probability_for_0

    def __getitem__(self, value):
        choice = choices([Bit(0), Bit(1)], [self.probability_for_0, self.probability_for_1])
        return choice
    
    