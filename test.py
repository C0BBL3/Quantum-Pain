from addition import add
from qubit import Qubit
import math

print(add([0], [1])[0]) # 1

print(add([Qubit(probability_vector = [math.sqrt(0.99), math.sqrt(0.01)])], [Qubit(probability_vector = [math.sqrt(0.01), math.sqrt(0.99)])])) # 1