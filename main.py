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



# Functions
def add(a: float, b: float):
    return a + b


def subtract(a: float, b: float):
    return a - b


def multiply(a: float, b: float):
    return a * b


def divide(a: float, b: float):
    return a / b


def main():
    I2C_ADDR     = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16

    #Test function for verifying basic functionality
    print("main")
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    
    lcd.clear()

    # User Input
    # Pico: Replace input with Button Routine
    menu = input("calc:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n  ")

    if menu == "1":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(add(a, b))
    elif menu == "2":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(subtract(a, b))
    elif menu == "3":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(multiply(a, b))
    elif menu == "4":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(divide(a, b))
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