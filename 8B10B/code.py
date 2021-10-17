from myhdl import intbv
import random

random.seed(5)
randrange = random.randrange

_3B4BEncodingValues = ['0100', '1001', '0101', '0011', '0010', '1010', '0110', '0001']

_5B6BEncodingValues = ['100111', '011101', '101101', '110001', '110101', '101001', '011001', '111000', '111001', '100101', '010101', '110100', '001101', '101100', '011100', '010111', '011011', '100011', '010011', '110010', '001011', '101010', '011010', '111010', '110011', '100110', '010110', '110110', '001110', '101110', '011110', '101011']

input = 80  # 100 11100

def prints(din):
    _HGF = int(din[8:5])
    _EDCBA = int(din[5:0])
    _fghj = _3B4BEncodingValues[_HGF]
    _abcdei = _5B6BEncodingValues[_EDCBA]

    print('~~~~~~~~~~~~~~~~~~~~')
    print('Input Dec: ', input)
    print('Input: ', bin(din[8:5])[2:], bin(din[5:0])[2:])
    print('Output: ', _abcdei, _fghj)
    print('~~~~~~~~~~~~~~~~~~~~')

def main():
    din = intbv(input, min=0, max=256)
    
    prints(din)

if __name__ == '__main__' :
    main()