from myhdl import *

from myhdl import block, always_seq

colores = ['rojo', 'verde', 'amarrilo']
segundos = [10, 10, 5]

@block
def contador(enable, clock, reset, count):

    @always(delay(10))
    def clkgen():
        clock.next = not clock
   
    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            count.next = count + 1

    return clkgen, seq

def semaforo():
    initialState = 0
    initialColor = colores[initialState]
    initialDelayS = segundos[initialState]

    clk = Signal(bool(0))
    enable = Signal(bool(1))
    reset = Signal(bool(0))
    segundoContados = Signal(intbv(0)[5:0])

    semaforoI = contador(clk, enable, reset, segundoContados)

    print('segundoContados: ', int(segundoContados, 10))

    semaforoI.convert(hdl="Verilog", initial_values=True)

if __name__ == '__main__' :
    semaforo()