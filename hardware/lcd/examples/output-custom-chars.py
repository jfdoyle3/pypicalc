#GitHub/Doc for I2cLcd
# https://github.com/dhylands/python_lcd
import sys
import os

# Add a directory to sys.path
sys.path.append("/display")


import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def main():
    #Test function for verifying basic functionality
    print("main")
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("It Works!")
    utime.sleep(2)
    lcd.clear()
    happy_face = bytearray([0x10,0x08,0x04,0x1F,0x04,0x04,0x02,0x01])
    lcd.custom_char(0, happy_face)
    lcd.putchar(chr(0))
    lcd.putchar(b'\x00')

#GitHub/Doc for I2cLcd
# https://github.com/dhylands/python_lcd
#if __name__ == "__main__":
main()
