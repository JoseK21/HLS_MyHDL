import random
from myhdl import StopSimulation, block, enum, always, instance, Signal, intbv, delay
from mux import mux

random.seed(5)
randrange = random.randrange

t_state = enum('0', '1')

@block
def test_mux():

    a = Signal(intbv(4))
    b = Signal(intbv(6))
    z = Signal(intbv(0))
    sel = Signal(intbv(0))

    clk = Signal(bool(0))

    mux_1 = mux(z, a, b, sel)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        for i in range(10):
            sel.next = randrange(2)
            delay(10)
        raise StopSimulation()

    return mux_1, clkgen, stimulus


    # @instance
    # def stimulus():
    #     print("z a b sel")
    #     for i in range(12):
    #         sel.next = randrange(2)
    #         yield delay(10)
    #         print("%s %s %s %s" % (z, a, b, sel))
    #     raise StopSimulation()

    # return mux_1, stimulus, clkgen

tb = test_mux()
tb.config_sim(trace=True)
tb.run_sim()