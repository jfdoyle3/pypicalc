import sys
import os

# Add a directory to sys.path
sys.path.append("/display")

from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin
import utime as time
 
 
i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
 
while True:
      lcd.move_to(2,0)
      lcd.putstr('Hello world')