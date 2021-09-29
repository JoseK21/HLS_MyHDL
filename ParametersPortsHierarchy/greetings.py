from myhdl import block, Signal

from myhdl import intbv, modbv
from myhdl import bin

from ClkDriver import ClkDriver

from Hello import Hello

@block
def Greetings(): #  higher-level function

    a = intbv(24, min=0, max=25) #By default return the value as Hex - To Dec -> int(#)

    print('a: ', a)
    print(int(a))

    count = Signal(modbv(24, min=0, max=28))
    print('1 count: ', count)
    
    count.next = int(count) + 1

    print('2 count: ', count)
    print(int(count))

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClkDriver(clk1)  # positional and default association
    clkdriver_2 = ClkDriver(clk=clk2, period=19)  # named association
    hello_1 = Hello(clk=clk1)  # named and default association
    hello_2 = Hello(to="MyHDL", clk=clk2)  # named association

    return clkdriver_1, clkdriver_2, hello_1, hello_2
    # return instances()

inst = Greetings()
inst.run_sim(50)