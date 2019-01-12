import pyb
from pyb import Pin, ExtInt
callback = lambda e: print("stop interupting me")
extint = pyb.ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_UP, callback)
