from qubit import Qubit

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

def _not(probability_matrix, swaps):
    #i =  i | on -> i | off
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    for x, bit_string in enumerate(probability_matrix.keys()):
        conjugate = ''
        for index, bit in enumerate(bit_string):
            if index in swaps:
                conjugate += '1' if bit == '0' else '0'
            else:
                conjugate += bit
        new_probability_matrix = swap_rows(new_probability_matrix, bit_string, conjugate)
    return new_probability_matrix

def cnot(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '0'):
    #i, j = swaps # i | on and j | off
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    for x, bit_string in enumerate(probability_matrix.keys()):
        if check_if_swap(bit_string, swaps):
            conjugate = bit_string[:swaps[-1]] + '1' + bit_string[swaps[-1] + 1:]
            new_probability_matrix = swap_rows(new_probability_matrix, bit_string, conjugate)
    return new_probability_matrix

def ccnot(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '1' and bit_string[swaps[2]] == '0'): 
    #i, j, k = swaps # i | on and j | on and k | off
    return cnot(probability_matrix, swaps, check_if_swap)

def buffer(probability_matrix, swaps):
    #i = i | on -> i | off -> i | on
    new_probability_matrix = _not(probability_matrix, swaps, check_if_swap)
    return _not(new_probability_matrix, swaps)

def _and(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '1'):
    #i, j, k = swaps # i | on and j | on
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    for x, bit_string in enumerate(probability_matrix.keys()):
        if check_if_swap(bit_string, swaps):
            conjugate = ''
            for index, bit in enumerate(bit_string):
                if index in swaps:
                    conjugate += '1' if bit == '0' else '0'
                else:
                    conjugate += bit
            new_probability_matrix = swap_rows(new_probability_matrix, bit_string, conjugate)
    return new_probability_matrix

def _or(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: bit_string[swaps[0]] == '1' or bit_string[swaps[1]] == '1'):
    #i, j = swaps # i | on or j | on
    return _and(probability_matrix, swaps, check_if_swap)

def nand(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: not (bit_string[swaps[0]] == '1' and bit_string[swaps[1]] == '1')):
    #i, j = swaps # not i | on and j | on
    return _and(probability_matrix, swaps, check_if_swap)

def _nor(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: not(bit_string[swaps[0]] == '1' or bit_string[swaps[1]] == '1')):
    #i, j = swaps # not i | on or j | on
    return _and(probability_matrix, swaps, check_if_swap)

def xor(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: (bit_string[swaps[0]] != bit_string[swaps[1]])):
    #i, j = swaps # i | on or j | on while not (i | on and j | on or i | off and i | off)
    return _or(probability_matrix, swaps, check_if_swap)

def xnor(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: (bit_string[swaps[0]] == bit_string[swaps[1]])):
    #i, j = swaps # i | off and j | off or i | on and i | on 
    return _or(probability_matrix, swaps, check_if_swap)

def xand(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: (bit_string[swaps[0]] == bit_string[swaps[1]])):
    #i, j = swaps # i | off and j | off or i | on and i | on 
    return xnor(probability_matrix, swaps,)

def xnand(probability_matrix, swaps, check_if_swap = lambda bit_string, swaps: (bit_string[swaps[0]] != bit_string[swaps[1]])):
    #i, j = swaps # i | on or j | on while not (i | on and j | on or i | off and i | off)
    return xor(probability_matrix, swaps)

def swap_rows(probability_matrix, x, y):
    new_probability_matrix = {bit_string: probability for bit_string, probability in probability_matrix.items()}
    new_probability_matrix[x] = probability_matrix[y]
    new_probability_matrix[y] = probability_matrix[x]
    return new_probability_matrix

def check_if_list_is_mixed(num_list):
    qubit_count = [isinstance(num, Qubit) for num in num_list].count(True)
    bit_count = [isinstance(num, int) for num in num_list].count(True)
    if qubit_count > 0 and bit_count > 0:
        return False
    return True