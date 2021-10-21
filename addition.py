from qubit import Qubit
import numpy as np
import math
from random import choices


def add(num_1, num_2): # `num_1` and `num_2` are an array of `Qubits` or `Bits` but not both in the same list
    try:
        if isinstance(num_1, list) and isinstance(num_2, list):
            if not check_if_list_is_mixed(num_1) and not check_if_list_is_mixed(num_2):
                raise Exception('Mixed Qubit and Bit string')
            else:
                if isinstance(num_1[0], Qubit) and isinstance(num_2[0], Qubit):
                    return quantum(num_1, num_2)
                else:
                    return binary(num_1, num_2)
        elif not isinstance(list, num_1) and not isinstance(list, num_2):
            return num_1 + num_2
        raise ValueError('Please give the function two numbers of the same type. Either both lists of Qubits/Bits or both floats/ints.')
    except ValueError as va:
        print(va)
        exit()

def quantum(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        return two_qubit_quantum_system(num_1, num_2)
    else:
        #ahhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        return 'fuck you im not doing this now'


def two_qubit_quantum_system(num_1, num_2, c_in = Qubit()): # recursive addition... yeah... recursive... addition... kill me now
    # This is the full adder algorithm by Prof Feyman
    num_1[0].name = ' a '
    num_2[0].name = ' b '
    c_in.name = ' c in '
    probability_matrix_a_b_c_in_zero, bit_strings = generate_probability_matrix(num_1 + num_2 + [c_in] + [Qubit(probability_vector = [math.sqrt(0.99),math.sqrt(0.01)], name = 'zero')])
    new_probability_matrix = ccnot(probability_matrix_a_b_c_in_zero, bit_strings, swaps=[0,1,3]) # Each of the following operations returns a matrix with a probability for each possible outcome. 
    new_probability_matrix = cnot(new_probability_matrix, bit_strings, swaps=[0,1])
    new_probability_matrix = ccnot(new_probability_matrix, bit_strings, swaps=[1,2,3])
    new_probability_matrix = cnot(new_probability_matrix, bit_strings, swaps=[1,2])
    new_probability_matrix = cnot(new_probability_matrix, bit_strings, swaps=[0,1]) # optional
    observation = observe(new_probability_matrix, bit_strings) # Returns a list of bits
    if observation[2] == 0:
        return str(observation[3])
    else:
        return str(observation[2]) + str(observation[3])

def generate_probability_matrix(qubits): #Tensor Multiplication
    k = 2 ** len(qubits)
    matrix = []
    bit_strings = []
    for row_index in range(k):
        binary = list(format(row_index, "b"))
        binary = ['0' for _ in range(len(qubits) - len(binary))] + binary
        bit_strings.append([int(value) for value in binary])
        temp = 1
        for qubit_index, qubit in enumerate(qubits):
            vector_index = int(binary[qubit_index])
            temp *= qubit.probability_vector[vector_index]
        matrix.append(temp)
    return matrix, bit_strings

def ccnot(probability_matrix, bit_strings, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == 1 and bit_string[swaps[1]] == 1 and bit_string[swaps[2]] == 0): 
    #i, j, k = swaps # i | on, j | on, k | off
    return cnot(probability_matrix, bit_strings, swaps, check_if_swap)

def cnot(probability_matrix, bit_strings, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == 1 and bit_string[swaps[1]] == 0):
    #i, j = swaps # i | on, j | off
    new_probability_matrix = [probability for probability in probability_matrix]
    for x, bit_string in enumerate(bit_strings):
        temp = [bit for bit in bit_string]
        if check_if_swap(bit_string, swaps):
            conjugate = bit_string[:swaps[-1]] + [1] + bit_string[swaps[-1] + 1:]
            y = bit_strings.index(conjugate)
            new_probability_matrix = swap_rows(new_probability_matrix, x, y)
    return new_probability_matrix

def swap_rows(probability_matrix, x, y):
    new_probability_matrix = [probability for probability in probability_matrix]
    new_probability_matrix[x] = probability_matrix[y]
    new_probability_matrix[y] = probability_matrix[x]
    return new_probability_matrix

def observe(probability_matrix, bit_strings):
    return choices(bit_strings, [probability * 100.0 for probability in probability_matrix])[0]

def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0] + num_2[0] > 1:
            return [1, 0]
        else:
            return [num_1[0] + num_2[0]]
    longer_list_len = max(len(num_1), len(num_2))
    bit_string = []
    carry = 0
    for index in range(longer_list_len - 1, -1, -1):
        temp = carry
        temp += 1 if num_1[index] == 1 else 0
        temp += 1 if num_2[index] == 1 else 0
        bit_string = [(1 if temp % 2 == 1 else 0)] + bit_string
    
        carry = 0 if temp < 2 else 1
    
    if carry != 0:
        bit_string = [1] + bit_string  

    return bit_string + [0 for _ in range(0, len(longer_list_len) - len(bit_string))]


def check_if_list_is_mixed(num_list):
    qubit_count = [isinstance(num, Qubit) for num in num_list].count(True)
    bit_count = [isinstance(num, int) for num in num_list].count(True)
    if qubit_count > 0 and bit_count > 0:
        return False
    return True