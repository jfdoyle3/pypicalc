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

# lcd.move_to(x,y) 
lcd.move_to(2,0)
lcd.putstr('Display Works')
time.sleep(5)
lcd.clear()
lcd.move_to(2,0)
lcd.putstr('Turning off')
lcd.move_to(0,1)
for count in range(1,4):
    lcd.putstr(f'{count}.. ')
    cursor=count*4
    lcd.move_to(cursor, 1)
    time.sleep(2)

lcd.clear()
lcd.backlight_off()
lcd.display_off()