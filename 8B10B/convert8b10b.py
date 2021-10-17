import random
from myhdl import block, always_seq, Signal, modbv

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

base2_3 = [4, 2, 1]
base2_5 = [16, 8, 4, 2, 1]

@block
def convert8b10b(clock, bit_in, reset, HGF, EDCBA, bit_out):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
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