import random
from myhdl import block, always_seq, Signal, modbv, delay, always, intbv

from datetime import datetime

# random.seed(datetime.now().second)
# randrange = random.randrange

random.seed(5)
randrange = random.randrange

base2_3 = [4, 2, 1]
base2_5 = [16, 8, 4, 2, 1]
_3B4BEncodingValues = [4, 9, 5, 3, 2, 10, 6, 1]
_5B6BEncodingValues = [39, 29, 45, 49, 53, 41, 25, 56, 57, 37, 21, 52, 13, 44, 28, 23, 27, 35, 19, 50, 11, 42, 26, 58, 51, 38, 22, 54, 14, 46, 30, 43]


@block
def newBit(data, clock, enable, reset, bit_in):
    counter = Signal(modbv(7, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            bit_in.next = data[counter + 1: counter] # 1 or 0
        counter.next = counter - 1

    return seq #, getRandom

@block
def convert10b(clock, reset, HGF, EDCBA, fghj, abcdei):
    i = Signal(modbv(0, min=0, max=8))

    mem3_4 = [intbv(4), intbv(9), intbv(5), intbv(3), intbv(2), intbv(10), intbv(6), intbv(1)]
    mem5_6 = [Signal(intbv(i)[5:]) for i in _5B6BEncodingValues]


    @always_seq(clock.negedge, reset=reset)
    def seq():
        if(i == 2): # 3er item
            if(HGF == 0):
                fghj.next = 4
            elif(HGF == 1):
                fghj.next = 9
            elif(HGF == 2):
                fghj.next = 5
            elif(HGF == 3):
                fghj.next = 3
            elif(HGF == 4):
                fghj.next = 2
            elif(HGF == 5):
                fghj.next = 10
            elif(HGF == 6):
                fghj.next = 6
            elif(HGF == 7):
                fghj.next = 1              
        if(i == 7): # 8to item
            # print('--------iiiiiiiii-----------', _5B6BEncodingValues[int(EDCBA)])
            if(EDCBA == 0):
                abcdei.next = 39
            elif(EDCBA == 1):
                abcdei.next = 29
            elif(EDCBA == 2):
                abcdei.next = 45
            elif(EDCBA == 3):
                abcdei.next = 49
            elif(EDCBA == 4):
                abcdei.next = 53
            elif(EDCBA == 5):
                abcdei.next = 41
            elif(EDCBA == 6):
                abcdei.next = 25
            elif(EDCBA == 7):
                abcdei.next = 56
            elif(EDCBA == 8):
                abcdei.next = 57
            elif(EDCBA == 9):
                abcdei.next = 37
            elif(EDCBA == 10):
                abcdei.next = 21
            elif(EDCBA == 11):
                abcdei.next = 52
            elif(EDCBA == 12):
                abcdei.next = 13
            elif(EDCBA == 13):
                abcdei.next = 44
            elif(EDCBA == 14):
                abcdei.next = 28
            elif(EDCBA == 15):
                abcdei.next = 23
            elif(EDCBA == 16):
                abcdei.next = 27
            elif(EDCBA == 17):
                abcdei.next = 35
            elif(EDCBA == 18):
                abcdei.next = 19
            elif(EDCBA == 19):
                abcdei.next = 50
            elif(EDCBA == 20):
                abcdei.next = 11
            elif(EDCBA == 21):
                abcdei.next = 42
            elif(EDCBA == 22):
                abcdei.next = 26
            elif(EDCBA == 23):
                abcdei.next = 58
            elif(EDCBA == 24):
                abcdei.next = 51
            elif(EDCBA == 25):
                abcdei.next = 38
            elif(EDCBA == 26):
                abcdei.next = 22
            elif(EDCBA == 27):
                abcdei.next = 54
            elif(EDCBA == 28):
                abcdei.next = 14
            elif(EDCBA == 29):
                abcdei.next = 46
            elif(EDCBA == 30):
                abcdei.next = 30
            elif(EDCBA == 31):
                abcdei.next = 43

        i.next = i + 1

    return seq

@block
def convert8b10b(clock, bit_in, reset, HGF, EDCBA):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if(i < 3):
            if(bit_in):
                if(i == 0):
                    HGF.next = HGF + 4
                elif(i == 1):
                    HGF.next = HGF + 2 
                elif(i == 2):
                    HGF.next = HGF + 1 
        else:
            if(bit_in):
                if(i == 3):
                    EDCBA.next = EDCBA + 16 
                elif(i == 4):
                    EDCBA.next = EDCBA + 8 
                elif(i == 5):
                    EDCBA.next = EDCBA + 4
                elif(i == 6):
                    EDCBA.next = EDCBA + 2 
                elif(i == 7):
                    EDCBA.next = EDCBA + 1
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