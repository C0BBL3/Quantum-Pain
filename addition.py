from qubit import Qubit
import math
from random import choices
from gates import cnot, ccnot, generate_probability_matrix, check_if_list_is_mixed

def generate_quantum_system(bit_string):
    quantum_system = []
    for bit in bit_string:
        if bit == '0' or bit == 0:
            quantum_system.append(Qubit(probability_vector = [1,0]))
        if bit == '1' or bit == 1:
            quantum_system.append(Qubit(probability_vector = [0,1]))
    return quantum_system

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

def quantum(qs_1, qs_2):
    if len(qs_1) == 0 and len(qs_2) == 0:
        return '0'
    elif len(qs_1) == 1 and len(qs_2) == 1:
        sum_ = two_qubits(qs_1[0], qs_2[0])
        if sum_[1] == '0':
            return sum_[0]
        else:
            return ''.join(sum_[::-1])
    else:
        if len(qs_1) > len(qs_2):
            qs_2 = generate_quantum_system(''.join(['0' for _ in range(len(qs_1) - len(qs_2))])) + qs_2
        elif len(qs_2) > len(qs_1):
            qs_1 = generate_quantum_system(''.join(['0' for _ in range(len(qs_2) - len(qs_1))])) + qs_1
        result = []
        carry = [Qubit(probability_vector = [1,0]) for _ in range(len(qs_1) + 1)]
        for i, (q_1, q_2) in enumerate(list(zip(qs_1, qs_2))[::-1]):
            sum_ = two_qubits(q_1, q_2, carry[i], carry[i+1])
            result.append(sum_[0])
            if sum_[1] == '1':
                carry[i+1] = Qubit(probability_vector = [0,1])
        if sum_[1] == '1':
            result.append(sum_[1])
        return ''.join(result[::-1])

def two_qubits(q_1, q_2, c_in = Qubit(probability_vector = [1,0]), zero = Qubit(probability_vector = [1,0])): 
    # This is the full adder algorithm by Prof Feyman
    probability_matrix_a_b_c_in_zero = generate_probability_matrix([q_1] + [q_2] + [c_in] + [zero])
    new_probability_matrix = ccnot(probability_matrix_a_b_c_in_zero, swaps=[0,1,3]) # Each of the following operations returns a matrix with a probability for each possible outcome. 
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0,1])
    new_probability_matrix = ccnot(new_probability_matrix, swaps=[1,2,3])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[1,2])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0,1]) # optional
    observation = observe(new_probability_matrix) # Returns a list of bits
    return observation[2], observation[3] # sum, carry

def observe(probability_matrix):
    return choices(list(probability_matrix.keys()), list(probability_matrix.values()))[0]

def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0] + num_2[0] == 2:
            return ''.join(list(['1', '0']))
        elif num_1[0] + num_2[0] <= 1:
            return str(num_1[0] + num_2[0])
    longer_list_len = max(len(num_1), len(num_2))
    if len(num_1) > len(num_2):
        num_2 = [0 for _ in range(longer_list_len - len(num_2))] + num_2
    if len(num_2) > len(num_1):
        num_1 = [0 for _ in range(longer_list_len - len(num_1))] + num_1
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
    return ''.join([str(bit) for bit in bit_string] + ['0' for _ in range(longer_list_len - len(bit_string))])
