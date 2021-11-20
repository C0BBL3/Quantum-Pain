from qubit import Qubit
import math
from random import choices
from gates import cnot, ccnot, generate_probability_matrix, check_if_list_is_mixed

def subtract(num_1, num_2):
    try:
        if isinstance(num_1, list) and isinstance(num_2, list):
            if not check_if_list_is_mixed(num_1) and not check_if_list_is_mixed(num_2):
                raise Exception('Mixed Qubit and Bit string')
            else:
                if isinstance(num_1[0], Qubit) and isinstance(num_2[0], Qubit):
                    print('no')
                    exit()
                    #return quantum(num_1, num_2)
                else:
                    return binary(num_1, num_2)
        elif not isinstance(list, num_1) and not isinstance(list, num_2):
            return num_1 + num_2
        raise ValueError('Please give the function two numbers of the same type. Either both lists of Qubits/Bits or both floats/ints.')
    except ValueError as va:
        print(va)
        exit()

#def quantum(qs_1, qs_2):

def two_qubits(q_1, q_2, b_in = Qubit(probability_vector = [1,0]), zero = Qubit(probability_vector = [1,0])):
    # This is the full subtractor algorithm by ME!
    probability_matrix_x_y_b_in_zero_zero_zero = generate_probability_matrix([q_1] + [q_2] + [b_in] + [zero])
    new_probability_matrix = _not(probability_matrix_x_y_b_in_zero, swaps=[0]) # Each of the following operations returns a matrix with a probability for each possible outcome. 
    new_probability_matrix = _and(new_probability_matrix, swaps=[0, 1])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0, 1])
    new_probability_matrix = _not(new_probability_matrix, swaps=[1])
    new_probability_matrix = _and(new_probability_matrix, swaps=[1, 2])
    new_probability_matrix = _and(new_probability_matrix, swaps=[1, 3])
    new_probability_matrix = cnot(new_probability_matrix, swaps=[0, 1]) # optional
    observation = observe(new_probability_matrix) # Returns a list of bits
    return observation[2], observation[3] # difference, borrow

def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0] - num_2[0] >= 0:
            return str(num_1[0] - num_2[0])
        if num_1[0] - num_2[0] < 0:
            return '0b1' # -1
    longer_list_len = max(len(num_1), len(num_2))
    if len(num_1) > len(num_2):
        num_2 = [0 for _ in range(longer_list_len - len(num_2))] + num_2
    if len(num_2) > len(num_1):
        num_1 = [0 for _ in range(longer_list_len - len(num_1))] + num_1
    bit_string = []
    borrow = 0
    for index in range(longer_list_len - 1, -1, -1):
        temp = borrow
        temp += 1 if num_1[index] == 1 else 0
        temp -= 1 if num_2[index] == 1 else 0
        bit_string = [(1 if temp % 2 == 1 else 0)] + bit_string
        borrow = 0 if temp < 2 else 1
    if borrow != 0:
        bit_string = [1] + bit_string  
    return ''.join([str(bit) for bit in bit_string] + ['0' for _ in range(longer_list_len - len(bit_string))])