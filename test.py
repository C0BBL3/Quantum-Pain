from addition import add
from addition import generate_quantum_system
from qubit import Qubit

#answers are in binary, so 10  =  [1, 0]  =  10

print('\n0 + 0 = 0') # 0 + 0 = 0
print('Conventional:', add([0], [0])) # 0 + 0 = 0
print('Quantum:', add(generate_quantum_system('0'), generate_quantum_system('0'))) # 0 + 0 = 0

print('\n0 + 1 = 1') # 0 + 1 = 0
print('Conventional:', add([0], [1])) # 0 + 1 = 1
print('Quantum:', add(generate_quantum_system('0'), generate_quantum_system('1'))) # 0 + 1 = 1

print('\n1 + 0 = 1') # 0 + 1 = 1
print('Conventional:', add([1], [0])) # 0 + 1 = 1
print('Quantum:', add(generate_quantum_system('1'), generate_quantum_system('0'))) # 0 + 1 = 1

print('\n1 + 1 = 2 = 10') # 1 + 1 = 2
print('Conventional:', add([1], [1])) # 1 + 1 = 10
print('Quantum:', add(generate_quantum_system('1'), generate_quantum_system('1'))) # 1 + 1 = 10

print('\n2 + 1 = 3 = 11') # 2 + 1 = 3
print('Conventional:', add([1,0], [1])) # 10 + 1 = 11
print('Quantum:', add(generate_quantum_system('10'), generate_quantum_system('1'))) # 10 + 1 = 11

print('\n2 + 2 = 4 = 100') # 2 + 2 = 4
print('Conventional:', add([1,0], [1,0])) # 10 + 10 = 100
print('Quantum:', add(generate_quantum_system('10'), generate_quantum_system('10'))) # 10 + 10 = 100

print('\n6 + 4 = 10 = 1010') # 6 + 4 = 10
print('Conventional:', add([1,1,0], [1,0,0])) # 110 + 100 = 1010
print('Quantum:', add(generate_quantum_system('110'), generate_quantum_system('100'))) # 110 + 100 = 1010

print('\n6 + 12 = 18 = 10010') 
print('Conventional:', add([1,1,0], [1,1,0,0])) # 110 + 1100 = 10010
print('Quantum:', add(generate_quantum_system('110'), generate_quantum_system('1100'))) # 110 + 1100 = 10010

print('\n35 + 23 = 58 = 111010')
print('Conventional:', add([1,0,0,0,1,1], [1,0,1,1,1])) # 100011 + 10111 = 111010
print('Quantum:', add(generate_quantum_system('100011'), generate_quantum_system('10111'))) # 100011 + 10111 = 111010

print('\n1234 + 4321 = 5555 = 1010110110011')
print('Conventional:', add([1,0,0,1,1,0,1,0,0,1,0], [1,0,0,0,0,1,1,1,0,0,0,0,1])) # 100011 + 10111 = 1010110110011
print('Quantum:', add(generate_quantum_system('10011010010'), generate_quantum_system('1000011100001'))) # 100011 + 10111 = 1010110110011