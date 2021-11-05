from qubit import Qubit
import math
from random import choices
from gates import cnot, ccnot, generate_probability_matrix, check_if_list_is_mixed

def division(num_1, num_2):
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

#def quantum(number):

#def binary(number):