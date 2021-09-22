
# RUN: python .\hello1.py

from myhdl import block, delay, always, now

@block # hardware ->module<-
def HelloWorld(): # parameter list is used to define the ->interface<- of the hardware block 

    @always(delay(10))
    def say_hello():
        print("%s Hello World!" % now())

    return say_hello

inst = HelloWorld() # instance of a hardware bloc
inst.run_sim(40) # To simulate the instance, 30: timesteps