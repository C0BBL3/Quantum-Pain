from qubit import Qubit
import math
from random import choices
from gates import cnot, ccnot, generate_probability_matrix, check_if_list_is_mixed

def factor(number):
    try:
        if isinstance(number, list):
            if not check_if_list_is_mixed(number):
                raise Exception('Mixed Qubit and Bit string')
            else:
                if isinstance(number[0], Qubit):
                    return quantum(number)
                else:
                    return binary(number)
        else:
            return number.value
        raise Exception('Mixed Qubit and Bit string')
    except Exception as exc:
        print(exc)
        exit()

#def quantum(number):

#def binary(number):