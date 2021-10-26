from addition import add
from qubit import Qubit
import math

#answers are in binary, so 10 = [1, 0] = 2

print(add([0], [1])) # 1+0=1

print(add([Qubit(probability_vector = [1,0]), [Qubit(probability_vector = [0,1])])]) # 1

print(add([1], [1])) # 1+1=2

print(add([Qubit(probability_vector = [1,0]), [Qubit(probability_vector = [1,0])])]) # 10

print(add([1], [1,1])) # 1+3=4

print(add([Qubit(probability_vector = [1,0]), [Qubit(probability_vector = [1,0])])]) # 100