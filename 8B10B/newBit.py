import random
from myhdl import block, always_seq

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

@block
def newBit(clock, enable, reset, bit_in):  
    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            bit_in.next = randrange(2) # 1 or 0

    return seq