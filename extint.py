import pyb
import time
from time import *
from pyb import Pin, ExtInt, Switch

start = ticks_us()

def log(line):
    global start
    
    print(ticks_us() - start)
    
    start = ticks_us()
    
    
extint = pyb.ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_UP, log)
