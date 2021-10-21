from bit import Bit
from qubit import Qubit
import numpy as np
import math


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

def quantum(num_1, num_2): # recursive addition... yeah... recursive... addition... kill me now
    probability_matrix_a_b_c_in_zero = generate_probability_matrix(num_1 + num_2 + c_in + Qubit(probability_vector = [1,0]))
    
    return 

def generate_probability_matrix(qubits): #Tensor Multiplication
    if len(qubits) == 1:
        return qubits[0].probability_vector
    matrix = []
    qubit_1 = qubits[0]
    qubit_2 = qubits[1]
    for probability in qubit_2.probability_vector:
        matrix.append([probability * probability_2 for probability_2 in qubit_1])
    if len(qubits[:2]) > 0:
        new_qubit = Qubit(probability_vector = matrix)
        return generate_probability_matrix([new_qubit] + qubits[:2])
    return matrix

def two_qubits(probability_matrix): 
    zero = Qubit(probability_vector = [1, 0]) # A.K.A. c_out
    # Quantum Full Adder by Prof Feyman go brrrrrr (I met him before and hes a dope af dood)
    ccnot 

    sum_out = None

    return 

def cnot(probability_matrix, i, j):


def ccnot(probability_matrix, i, j, k):
    k = math.log(len(probability_matrix)) / math.log(2)

    

def cnot(probability_matrix):
    return np.array([[probability_matrix[0]], [probability_matrix[1]], [probability_matrix[3]], [probability_matrix[2]]])

def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0].value + num_2[0].value > 1:
            return [Bit(1), Bit(0)]
        else:
            return [Bit(num_1[0].value + num_2[0].value)]
    longer_list_len = max(len(num_1), len(num_2))
    result = []
    carry = 0
    for index in range(longer_list_len - 1, -1, -1):
        temp = carry
        temp += 1 if num_1[index] == 1 else 0
        temp += 1 if num_2[index] == 1 else 0
        result = [(Bit(1) if temp % 2 == 1 else Bit(0))] + result
    
        carry = 0 if temp < 2 else 1
    
    if carry != 0:
        result = [Bit(1)] + result  

    return result + [0 for _ in range(0, len(longer_list_len) - len(result))]


def check_if_list_is_mixed(num_list):
    qubit_count = [isinstance(num, Qubit) for num in num_list].count(True)
    bit_count = [isinstance(num, Bit) for num in num_list].count(True)
    if qubit_count > 0 and bit_count > 0:
        return True
    return False