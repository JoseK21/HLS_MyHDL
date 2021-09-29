from myhdl import Signal, intbv

from RAM import ran_block

def convert_ram(hdl):
    clock  = Signal(bool(0))
    we  = Signal(bool(0))
    din = Signal(intbv(0)[8:])
    dout = Signal(intbv(0)[8:])
    addr = Signal(intbv(0)[7:])

    inst = ran_block(dout, din, addr, we, clock)
    inst.convert(hdl=hdl)

# convert_ram(hdl='Verilog')
convert_ram(hdl='VHDL')