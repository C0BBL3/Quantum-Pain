import math
from random import choices
import numpy as np

class Qubit:
    def __init__(self, probability_vector = list([1 / math.sqrt(2), 1 / math.sqrt(2)])):
        self.value = None
        self.entangled_pains = []
        self.probability_vector = probability_vector

    def __getitem__(self, value): # observe
        choice = choices([0, 1], weights = [100.0 * self.probability_for_0, 100.0 * self.probability_for_1])
        return choice