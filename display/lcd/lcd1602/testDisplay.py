from lcd1602 import LCD
import utime

lcd = LCD()
string = "Hello\n"
lcd.message(string)
utime.sleep(2)
string = "Me"
lcd.message(string)
utime.sleep(5)
lcd.clear()
