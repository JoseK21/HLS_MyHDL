import os
import random
import time

from myhdl import block, always, instance, Signal, ResetSignal, modbv, intbv, delay, StopSimulation

from help import convert8b10b, newBit, convert10b, getDisparity

from datetime import datetime

FILES = ['testbench.vcd', 'convert8b10b.v', 'convert10b.v', 'newBit.v', 'tb_newBit.v']

for f in FILES:
    if os.path.exists(f):
        os.remove(f)

time.sleep(1)

random.seed(datetime.now().second)
randrange = random.randrange

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

DATA_IN_BITS = 8

CICLO_RELOJ = 10

@block
def testbench(hdl):
    bit_in = Signal(bool(0))

    enable = Signal(bool(1))
    clock  = Signal(bool(0))
    reset = ResetSignal(1, active=0, isasync=True)
    # disparity = Signal(intbv(0)[2:0])
    disparity = Signal(intbv(0, min=-7, max=7))

    # -----------------------
    data = intbv(1)
    # -----------------------

    HGF = Signal(intbv(0)[3:0])
    EDCBA = Signal(intbv(0)[5:0])

    abcdei =  Signal(intbv(0)[6:0])
    fghj =  Signal(intbv(0)[4:0])

    inc_1 = newBit(data, clock, enable, reset, bit_in)

    inc_2 = convert8b10b(clock, bit_in, reset, HGF, EDCBA)

    inc_3 = convert10b(clock, reset, HGF, EDCBA, fghj, abcdei)

    inc_1.convert(hdl=hdl)
    inc_2.convert(hdl=hdl)
    inc_3.convert(hdl=hdl)

    # inc_4 = getDisparity(clock, reset, fghj, abcdei, disparity)

    @always(delay(CICLO_RELOJ)) # 10ns 
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        print('\nInput: ', end='')

        for i in range(10):
            if(i > 0):
                print(int(bit_in), end='')
            if(i == 3):
                print(' ', end='')

            yield clock.negedge # negedge } posedge
        # yield delay(10)
        print('\nOutput: ', end='')

        print(format(int(abcdei), '06b'), format(int(fghj), '04b'))
        print('Disparity: ', int(disparity))
        raise StopSimulation()

    return clockGen, stimulus, inc_1, inc_2, inc_3 #, inc_4

tb = testbench(hdl='Verilog')
tb.config_sim(trace=True)
tb.run_sim()
