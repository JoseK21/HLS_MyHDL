import random
from myhdl import block, always_seq, Signal, modbv, delay

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

base2_3 = [4, 2, 1]
base2_5 = [16, 8, 4, 2, 1]
_3B4BEncodingValues = [4, 9, 5, 3, 2, 10, 6, 1]
_5B6BEncodingValues = [39, 29, 45, 49, 53, 41, 25, 56, 57, 37, 21, 52, 13, 44, 28, 23, 27, 35, 19, 50, 11, 42, 26, 58, 51, 38, 22, 54, 14, 46, 30, 43]


CODE_INPUT = [1,1,1,0,1,1,0,1]

@block
def newBit(clock, enable, reset, bit_in):
    counter = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            print('>>>>', bool(CODE_INPUT[int(counter)]))
            bit_in.next = bool(CODE_INPUT[int(counter)]) # 1 or 0
        counter.next = counter + 1
    return seq

@block
def convert10b(clock, reset, HGF, EDCBA, fghj, abcdei):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.negedge, reset=reset)
    def seq():
        if(i == 2): # 3er item
            fghj.next = _3B4BEncodingValues[int(HGF)] # int(HGF) = 6 (110) ----> 7 (111)
        if(i == 7): # 8to item
            # print('--------iiiiiiiii-----------', _5B6BEncodingValues[int(EDCBA)])
            abcdei.next =_5B6BEncodingValues[int(EDCBA)]

        i.next = i + 1

    return seq

@block
def convert8b10b(clock, bit_in, reset, HGF, EDCBA, bit_out):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        delay(1)
        
        if(i < 3):
            if(bit_in):
                HGF.next = HGF + base2_3[i]
        else:
            if(bit_in):
                EDCBA.next = EDCBA + base2_5[i - 3]
        if(i >= 8):
            i.next = 0
        i.next = i + 1

    return seq

@block
def getDisparity(clock, reset, fghj, abcdei, disparity):
    a = Signal(modbv(0, min=0, max=8))
    c0 = Signal(modbv(0, min=0, max=8))
    c1 = Signal(modbv(0, min=0, max=8))  

    @always_seq(clock.negedge, reset=reset)
    def seq():
        if(a == 7):
            # for a in range(10):
            print('\n>>>>>>>>', abcdei, fghj)
        # if(a < 4):
        #     if(fghj[a+1:a]):
        #         c1.next = c1 + 1
        #     else:
        #         c0.next = c0 - 1
        # else:
        #     if(abcdei[a-4+1:a-4]):
        #         c1.next = c1 + 1
        #     else:
        #         c0.next = c0 - 1

        a.next = a + 1
        # print('\n0s ~ ', int(c0))
        # print('\n1s ~ ', int(c1))


    return seq