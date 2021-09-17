from addition import add
from bit import Bit
from qubit import Qubit

num_1 = [Bit(1), Bit(1), Bit(0), Bit(1)]
num_2 = [Bit(1), Bit(0), Bit(0)]
sum_ = add(num_1, num_2)

print(sum_)