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
        return ''.join(list(two_qubit_quantum_system(num_1[0], num_2[0])))
    else:
        if len(num_1) == len(num_2):
            result = []
            carry = [Qubit(probability_vector = [1,0]) for _ in range(len(num_1) + 1)]
            for i, (q_1, q_2) in enumerate(list(zip(num_1, num_2))[::-1]):
                sum_ = two_qubit_quantum_system(q_1, q_2, carry[i], carry[i+1])
                result.append(sum_[0])
                if i == 0:
                    first_carry = sum_[1]
                if sum_[1] == '1':
                    carry[i+1] = Qubit(probability_vector = [0,1])
                    result.append(sum_[1])
            result = [first_carry] + result
            return ''.join(result[::-1])
        else:
            return 'fuck you im not doing this now'

def two_qubit_quantum_system(num_1, num_2, c_in = Qubit(probability_vector = [1,0]), zero = Qubit(probability_vector = [1,0])): # recursive addition... yeah... recursive... addition... kill me now
    # This is the full adder algorithm by Prof Feyman
    probability_matrix_a_b_c_in_zero = generate_probability_matrix([num_1] + [num_2] + [c_in] + [Qubit(probability_vector = [1, 0])])
    new_probability_matrix = ccnot(probability_matrix_a_b_c_in_zero, swaps=[0,1,3]) # Each of the following operations returns a matrix with a probability for each possible outcome. 
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0,1])
    new_probability_matrix = ccnot(new_probability_matrix, swaps=[1,2,3])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[1,2])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0,1]) # optional
    observation = observe(new_probability_matrix) # Returns a list of bits
    return observation[3], observation[2]

def generate_probability_matrix(qubits): #Tensor Multiplication
    k = 2 ** len(qubits)
    matrix = {}
    for row_index in range(k):
        binary = list(format(row_index, "b"))
        binary = ''.join(['0' for _ in range(len(qubits) - len(binary))] + binary)
        probability = 1
        for qubit_index, qubit in enumerate(qubits):
            vector_index = int(binary[qubit_index])
            probability *= qubit.probability_vector[vector_index]
        matrix[binary] = probability
    return matrix

def ccnot(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '1' and bit_string[swaps[2]] == '0'): 
    #i, j, k = swaps # i | on, j | on, k | off
    return cnot(probability_matrix, swaps, check_if_swap)

def cnot(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '0'):
    #i, j = swaps # i | on, j | off
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    for x, bit_string in enumerate(probability_matrix.keys()):
        if check_if_swap(bit_string, swaps):
            conjugate = bit_string[:swaps[-1]] + '1' + bit_string[swaps[-1] + 1:]
            new_probability_matrix = swap_rows(new_probability_matrix, bit_string, conjugate)
    return new_probability_matrix

def swap_rows(probability_matrix, x, y):
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    new_probability_matrix[x] = probability_matrix[y]
    new_probability_matrix[y] = probability_matrix[x]
    return new_probability_matrix

def observe(probability_matrix):
    return choices(list(probability_matrix.keys()), list(probability_matrix.values()))[0]

def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0] + num_2[0] == 2:
            return ''.join(list(['1', '0']))
        elif num_1[0] + num_2[0] <= 1:
            return str(num_1[0] + num_2[0])
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
    return ''.join([str(bit) for bit in bit_string] + ['0' for _ in range(0, longer_list_len - len(bit_string))])


def check_if_list_is_mixed(num_list):
    qubit_count = [isinstance(num, Qubit) for num in num_list].count(True)
    bit_count = [isinstance(num, int) for num in num_list].count(True)
    if qubit_count > 0 and bit_count > 0:
        return False
    return True