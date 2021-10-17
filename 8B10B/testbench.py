import os
import random

from myhdl import block, always, instance, Signal, ResetSignal, modbv, intbv, delay, StopSimulation

from newBit import newBit
from convert8b10b import convert8b10b
from datetime import datetime

if os.path.exists("testbench.vcd"):
  os.remove("testbench.vcd")

random.seed(datetime.now().second)
randrange = random.randrange

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

DATA_IN_BITS = 8

@block
def testbench():
    bit_in = Signal(bool(randrange(2)))
    bit_out = Signal(bool(0))

    enable = Signal(bool(1))
    clock  = Signal(bool(0))
    reset = ResetSignal(1, active=0, isasync=True)

    # din = intbv(input, min=0, max=256)
    # dout = intbv(0, min=0, max=1025)

    # disarity = Signal(intbv(0)[1:0])

    # _HGF = int(din[8:5])
    # _EDCBA = int(din[5:0])

    HGF = Signal(intbv(0)[3:0])
    EDCBA = Signal(intbv(0)[5:0])

    abcdei = intbv(0)[6:0]
    fghj = intbv(0)[4:0]

    inc_1 = newBit(clock, enable, reset, bit_in)

    inc_2 = convert8b10b(clock, bit_in, reset, HGF, EDCBA, bit_out)

    HALF_PERIOD = delay(5)

    @always(HALF_PERIOD)
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        for i in range(8):
            yield clock.negedge
        raise StopSimulation()

    @instance
    def monitor():
        print("Data In 8B: ", end='')
        while 1:
            yield clock.posedge
            print(int(bit_in), end='')

    return clockGen, stimulus, monitor, inc_1, inc_2, #, HGF, EDCBA

tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()