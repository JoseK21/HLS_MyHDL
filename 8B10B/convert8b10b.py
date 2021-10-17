import random
from myhdl import block, always_seq, Signal, modbv

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

base2 = [1, 2, 4, 8, 16, 32]


@block
def convert8b10b(clock, bit_in, reset, HGF, EDCBA, bit_out):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if(i < 3):
            if(bit_in):
                HGF.next = HGF + base2[i]
            # bit_out.next = bit_in
        else:
            if(bit_in):
                EDCBA.next = EDCBA + base2[i - 3]
            # bit_out.next = bit_in
        if(i >= 8):
            i.next = 0

        # print(int(i), end='')
        i.next = i + 1

    return seq