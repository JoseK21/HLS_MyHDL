import os
import time

from myhdl import block, always, instance, Signal, ResetSignal, intbv, delay, StopSimulation

from help import parseBits, newBit, convertion

FILES = ['testbench.vcd', 'parseBits.v', 'convertion.v', 'newBit.v', 'tb_newBit.v']

for f in FILES:
    if os.path.exists(f):
        os.remove(f)

time.sleep(1)

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

DATA_IN_BITS = 8

CICLO_RELOJ = 10

@block
def testbench(hdl):
    # -----------------------
    data = intbv(255)
    # -----------------------
    # 10111001  ': 100 111011

    bit_in = Signal(bool(0))
    clock  = Signal(bool(0))
    reset = ResetSignal(1, active=0, isasync=True)

    HGF = Signal(intbv(0)[3:0])
    EDCBA = Signal(intbv(0)[5:0])

    fghj =  Signal(intbv(0)[4:0])
    abcdei =  Signal(intbv(0)[6:0])

    inc_1 = newBit(data, clock, reset, bit_in)
    inc_2 = parseBits(clock, bit_in, reset, HGF, EDCBA)
    inc_3 = convertion(clock, reset, HGF, EDCBA, fghj, abcdei)
    
    inc_1.convert(hdl=hdl)
    inc_2.convert(hdl=hdl)
    inc_3.convert(hdl=hdl)

    @always(delay(CICLO_RELOJ)) # 10ns 
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        print('\nInput: ', end='')

        for i in range(9):
            if(i > 0):
                print(int(bit_in), end='')
            if(i == 3):
                print(' ', end='')

            yield clock.negedge
        print('\nOutput: ', format(int(abcdei), '06b'), format(int(fghj), '04b'))
        reset.next = 0
        raise StopSimulation()

    return clockGen, stimulus, inc_1, inc_2, inc_3

tb = testbench(hdl='Verilog') # VHDL OR Verilog
tb.config_sim(trace=True)
tb.run_sim()
