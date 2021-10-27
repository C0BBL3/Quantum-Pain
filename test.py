from addition import add
from qubit import Qubit
import math

#answers are in binary, so 10 = [1, 0] = 2

print('0+0=0')
print(add([0], [0])) # 1+0=1
print(add([Qubit(probability_vector = [1,0])], [Qubit(probability_vector = [1,0])])) # 1+0=1

print('1+0=1')
print(add([0], [1])) # 1+0=1
print(add([Qubit(probability_vector = [1,0])], [Qubit(probability_vector = [0,1])])) # 1+0=1

print('0+1=1')
print(add([1], [0])) # 0+1=1
print(add([Qubit(probability_vector = [0,1])], [Qubit(probability_vector = [1,0])])) # 0+1=1

print('1+1=10')
print(add([1], [1])) # 1+1=10
print(add([Qubit(probability_vector = [0,1])], [Qubit(probability_vector = [0,1])])) # 1+1=10

#print('2+1=11')
#print(add([1,0], [1,0])) # 2+1=11
#print(add([Qubit(probability_vector = [0,1]), Qubit(probability_vector = [1,0])], [Qubit(probability_vector = [0,1])])) # 2+1=11

print('2+2=100')
print(add([1,0], [1,0])) # 2+2=100
print(add([Qubit(probability_vector = [0,1]), Qubit(probability_vector = [1,0])], [Qubit(probability_vector = [0,1]), Qubit(probability_vector = [1,0])])) # 2+2=100