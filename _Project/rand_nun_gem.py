# single_port_ram.py
# result is same as "single_port_RAM.v" of the Verilog tutorial

from myhdl import *

@block
def single_port_ram(clk, we, addr, din, dout, addr_width=2, data_width=3) :
    ram_single_port = [Signal(intbv(0)[addr_width:0])
                for i in range(data_width)]

    @always(clk.posedge)
    def write_logic():
        """ write data to address 'addr' """
        if we == 1 :
            ram_single_port[addr].next = din

    @always_comb
    def read_logic():
        """ read data from address 'addr' """
        dout.next = ram_single_port[addr]

    return read_logic, write_logic

def main():
    addr_width = 3
    data_width = 3
    clk = Signal(bool(0))
    we = Signal(bool(0))
    addr = Signal(intbv(0)[addr_width:0])
    din = Signal(intbv(0)[data_width:0])
    dout = Signal(intbv(0)[data_width:0])

    single_port_ram_verilog = single_port_ram(clk, we, addr,
                din, dout, addr_width, data_width)

    single_port_ram_verilog.convert(hdl="Verilog", initial_values=True)

if __name__ == '__main__' :
    main()