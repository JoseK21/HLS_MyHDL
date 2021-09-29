from myhdl import block, Signal, intbv, always, always_comb

@block
def ran_block(dout, din, addr, we, clock, depth=128):
    """  Ram model """

    mem = [Signal(intbv(0)[8:]) for i in range(depth)]

    @always(clock.posedge)
    def write():
        if we:
            mem[addr].next = din

    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read