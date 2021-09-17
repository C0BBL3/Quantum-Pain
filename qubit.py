import math

class Qubit:
    def __init__(self):
        self.value = None
        self.entangled_pains = []

    def observe(self, probability_values): # Larry
        self.probability_for_0 = sum([math.abs(value) ^ 2 for value in probability_values])
        self.probability_for_1 = 1.0 - self.probability_for_0

    def __getitem__(self, value)
    
    