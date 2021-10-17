from myhdl import Signal, ResetSignal, modbv, always, block, delay, instance, StopSimulation

from inc import inc

@block
def convert_inc():
    """Convert inc block to Verilog or VHDL."""

    count = Signal(bool(0))
    enable = Signal(bool(0))
    clock  = Signal(bool(0))
    reset = ResetSignal(0, active=0, isasync=True)

    inc_1 = inc(count, enable, clock, reset)
    
    @always(delay(10))
    def clkgen():
        clock.next = not clock

    @instance
    def stimulus():
        for i in range(10):
            clock.next = not clock
            delay(10)
        raise StopSimulation()

    return inc_1, stimulus, clkgen

tb = convert_inc()
tb.config_sim(trace=True)
tb.run_sim()