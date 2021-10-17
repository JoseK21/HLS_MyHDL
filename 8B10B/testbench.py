import os
import random
import time

from myhdl import block, always, instance, Signal, ResetSignal, modbv, intbv, delay, StopSimulation

from newBit import newBit
from convert8b10b import convert8b10b
from convert10b import convert10b

from datetime import datetime

if os.path.exists("testbench.vcd"):
    os.remove("testbench.vcd")
    time.sleep(1)

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

    abcdei =  Signal(intbv(0)[6:0])
    fghj =  Signal(intbv(0)[4:0])

    inc_1 = newBit(clock, enable, reset, bit_in)
    # inc_1.convert(hdl='Verilog')

    inc_2 = convert8b10b(clock, bit_in, reset, HGF, EDCBA, bit_out)

    inc_3 = convert10b(clock, reset, HGF, EDCBA, fghj, abcdei)

    HALF_PERIOD = delay(5)

    @always(HALF_PERIOD)
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        for i in range(8):
            print(int(bit_in), end='')

            yield clock.negedge
        print('')
        print(bin(abcdei)[2:], bin(fghj)[2:])
        raise StopSimulation()

    # @instance
    # def monitor():
    #     print("Data In 8B: ", end='')
    #     while 1:
    #         yield clock.posedge
    #         print(int(bit_in), end='')

    return clockGen, stimulus, inc_1, inc_2, inc_3 #, monitor #, HGF, EDCBA

tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()

# tb.convert(hdl='Verilog')