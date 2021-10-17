import random
from myhdl import block, always, instance, Signal, \
    ResetSignal, modbv, intbv, delay, StopSimulation

from newBit import newBit

from datetime import datetime

random.seed(datetime.now().second)
randrange = random.randrange

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

DATA_IN_BITS = 8

@block
def testbench():
    count = Signal(bool(0))
    enable = Signal(bool(0))
    clock  = Signal(bool(0))
    reset = ResetSignal(0, active=0, isasync=True)

    inc_1 = newBit(count, enable, clock, reset)

    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        reset.next = INACTIVE_HIGH
        yield clock.negedge
        # reset.next = INACTIVE_HIGH
        for i in range(8):
            enable.next = 1
            print(int(count), end='')
            yield clock.negedge
        raise StopSimulation()

    # @instance
    # def monitor():
    #     print("enable  count")
    #     yield reset.posedge
    #     while 1:
    #         yield clock.posedge
    #         yield delay(1)
    #         print("   %s      %s" % (int(enable), count))

    return clockGen, stimulus, inc_1 #, monitor

tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()