import time
from lcd1602 import LCD

lcd=LCD(2,0x27,True)

lcd.message("Hello line 1",1)
lcd.message("World line 2",2)


time.sleep(3)
lcd.message("Clearing.....",2)
time.sleep(2)
lcd.clear()
time.sleep(3)

lcd.message("World line 1",1)
lcd.message("Hello line 2",2)



time.sleep(5)
lcd.clear()


print("end of line")

