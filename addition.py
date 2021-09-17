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
    if len(num_1) == 1 and len(num_2) == 1:
        return two_qubits(num_1[0], num_2[0])
    # A Density Matrix a day keeps Dr. Chapman away... yay
    

def two_qubits(is_entangled, qubit_1, qubit_2): # I think this is how it be
    if is_entangled:
        probability_vector = np.append(qubit_1.probability_vector, qubit_2.probability_vector, axis=0)
    else:
        probability_vector = np.array([value_1 * value_2 for value_2 in qubit_2.probability_vector for value_1 in qubit_1.probability_vector])
    qubits = [qubit_1, qubit_2]
    gap = 0
    for qubit in qubits:
        for i in range(0,2):
            gubit.probability_vector = np.array([[probability_vector[i][0]], [probability_vector[i + 1 + gap][0]]])
        gap = 1
    return qubits


def binary(num_1, num_2):
    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0].value + num_2[0].value > 1:
            return [Bit(1), Bit(0)]
        else:
            return [Bit(num_1[0].value + num_2[0].value)]
    longer_list_len = len(max(len(num_1), len(num_2)))
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