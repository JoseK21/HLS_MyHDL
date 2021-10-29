from myhdl import block, always_seq, Signal, modbv

@block
def newBit(data, clock, reset, bit_in):
    counter = Signal(modbv(7, min=0, max=8))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        bit_in.next = data[counter + 1: counter] # 1 or 0
        counter.next = counter - 1

    return seq

@block
def parseBits(clock, bit_in, reset, HGF, EDCBA):
    i = Signal(modbv(0, min=0, max=8))

    @always_seq(clock.negedge, reset=reset)
    def seq():
        if(i < 3):
            if(bit_in):
                if(i == 0):
                    HGF.next = HGF + 4
                elif(i == 1):
                    HGF.next = HGF + 2 
                elif(i == 2):
                    HGF.next = HGF + 1 
        else:
            if(bit_in):
                if(i == 3):
                    EDCBA.next = EDCBA + 16
                elif(i == 4):
                    EDCBA.next = EDCBA + 8
                elif(i == 5):
                    EDCBA.next = EDCBA + 4
                elif(i == 6):
                    EDCBA.next = EDCBA + 2
                elif(i == 7):
                    EDCBA.next = EDCBA + 1 # EDCBA si suma +1, pero al llehar al otro lado, no esta actualizado.
        i.next = i + 1

    return seq

@block
def convertion(clock, reset, HGF, EDCBA, fghj, abcdei):
    i = Signal(modbv(0, min=0, max=16))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if(i == 3): # 3er item
            if(HGF == 0):
                fghj.next = 4
            elif(HGF == 1):
                fghj.next = 9
            elif(HGF == 2):
                fghj.next = 5
            elif(HGF == 3):
                fghj.next = 3
            elif(HGF == 4):
                fghj.next = 2
            elif(HGF == 5):
                fghj.next = 10
            elif(HGF == 6):
                fghj.next = 6
            elif(HGF == 7):
                fghj.next = 1              
        if(i == 8): # 8to item
            if(EDCBA == 0):
                abcdei.next = 39
            elif(EDCBA == 1):
                abcdei.next = 29
            elif(EDCBA == 2):
                abcdei.next = 45
            elif(EDCBA == 3):
                abcdei.next = 49
            elif(EDCBA == 4): # 00100
                abcdei.next = 53
            elif(EDCBA == 5): # 00101
                abcdei.next = 41
            elif(EDCBA == 6):
                abcdei.next = 25
            elif(EDCBA == 7):
                abcdei.next = 56
            elif(EDCBA == 8):
                abcdei.next = 57
            elif(EDCBA == 9):
                abcdei.next = 37
            elif(EDCBA == 10):
                abcdei.next = 21
            elif(EDCBA == 11):
                abcdei.next = 52
            elif(EDCBA == 12):
                abcdei.next = 13
            elif(EDCBA == 13):
                abcdei.next = 44
            elif(EDCBA == 14):
                abcdei.next = 28
            elif(EDCBA == 15):
                abcdei.next = 23
            elif(EDCBA == 16):
                abcdei.next = 27
            elif(EDCBA == 17):
                abcdei.next = 35
            elif(EDCBA == 18):
                abcdei.next = 19
            elif(EDCBA == 19):
                abcdei.next = 50
            elif(EDCBA == 20):
                abcdei.next = 11
            elif(EDCBA == 21):
                abcdei.next = 42
            elif(EDCBA == 22):
                abcdei.next = 26
            elif(EDCBA == 23):
                abcdei.next = 58
            elif(EDCBA == 24):
                abcdei.next = 51
            elif(EDCBA == 25):
                abcdei.next = 38
            elif(EDCBA == 26):
                abcdei.next = 22
            elif(EDCBA == 27):
                abcdei.next = 54
            elif(EDCBA == 28):
                abcdei.next = 14
            elif(EDCBA == 29):
                abcdei.next = 46
            elif(EDCBA == 30):
                abcdei.next = 30
            elif(EDCBA == 31):
                abcdei.next = 43

        i.next = i + 1

        if(i == 8):
            reset.next = 0
            i.next = 0

    return seq
