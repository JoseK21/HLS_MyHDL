import random
from myhdl import block, always_seq, Signal, modbv

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

base2_3 = [4, 2, 1]
base2_5 = [16, 8, 4, 2, 1]

# _3B4BEncodingValues = ['0100', '1001', '0101', '0011', '0010', '1010', '0110', '0001']
_3B4BEncodingValues = [4, 9, 5, 3, 2, 10, 6, 1]

# _5B6BEncodingValues = ['100111', '011101', '101101', '110001', '110101', '101001', '011001', '111000', '111001', '100101', '010101', '110100', '001101', '101100', '011100', '010111', '011011', '100011', '010011', '110010', '001011', '101010', '011010', '111010', '110011', '100110', '010110', '110110', '001110', '101110', '011110', '101011']
_5B6BEncodingValues = [39, 29, 45, 49, 53, 41, 25, 56, 57, 37, 21, 52, 13, 44, 28, 23, 27, 35, 19, 50, 11, 42, 26, 58, 51, 38, 22, 54, 14, 46, 30, 43]

@block
def convert10b(clock, reset, HGF, EDCBA, fghj, abcdei):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if(i == 2):
            fghj.next = _3B4BEncodingValues[int(HGF)]
        if(i == 7):
            abcdei.next =_5B6BEncodingValues[int(EDCBA)]

        i.next = i + 1

    return seq