import random
from myhdl import block, always_seq

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

@block
def newBit(count, enable, clock, reset):
    """ Incrementer with enable.

    count -- output
    enable -- control input, increment when 1
    clock -- clock input
    reset -- asynchronous reset input
    """
    
    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            count.next = randrange(2) # 1 or 0

    return seq