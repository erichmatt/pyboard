# main.py -- put your code here!
import pyb
from pyb import Pin, ExtInt, Switch
import time

start = time.ticks_ms()

def log(line):
    data = time.ticks_diff(time.ticks_ms(), start)
    start = time.ticks_ms()
    return print(data)    
    
#log = lambda e: print(time.ticks_diff(time.ticks_ms(), start))

sw.callback(log)

start = time.ticks_ms()
extint = pyb.ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_UP, log)
