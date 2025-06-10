## Calculator
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display

# Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display")

import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Setup LCD Address
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize LCD
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
LCD = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

# Setup Button
button=machine.Pin(14,machine.Pin.IN)
# if button.value()==1 then button is pressed.

# Functions
def add(a: float, b: float):
    LCD.move_to(0,0)
    LCD.putstr(f'{a} + {b} = ')
    return a + b


def subtract(a: float, b: float):
    LCD.move_to(0,0)
    LCD.putstr(f'{a} - {b} = ')
    return a - b


def multiply(a: float, b: float):
    LCD.move_to(0,0)
    LCD.putstr(f'{a} x {b} = ')
    return a * b


def divide(a: float, b: float):
    LCD.move_to(0,0)
    LCD.putstr(f'{a} / {b} = ')
    return a / b


def main():

    print("main")
    
    LCD.clear()

    # User Input
    # Pico: Replace input with Button Routine
    menu = input("calc:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n  ")

    if menu == "1":
        a = float(input("num1: "))
        b = float(input("num2: "))
        LCD.move_to(10,0)
        LCD.putstr(f'{add(a, b)}')
    elif menu == "2":
        a = float(input("num1: "))
        b = float(input("num2: "))
        LCD.move_to(10,0)
        LCD.putstr(f'{subtract(a, b)}')
    elif menu == "3":
        a = float(input("num1: "))
        b = float(input("num2: "))
        LCD.move_to(10,0)
        LCD.putstr(f'{multiply(a, b)}')
    elif menu == "4":
        a = float(input("num1: "))
        b = float(input("num2: "))
        LCD.move_to(10,0)
        LCD.putstr(f'{divide(a, b)}')        
    else:
        print("invalid input")

    # Output to LCD Display
    #    lcd.message("calculation completed")
    #    time.sleep(10)
    #    lcd.clear()

    # End of Line
    print("end of line")


# Main
if __name__ == "__main__":
    main()