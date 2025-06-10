# Pico Calculator

Google Search on Keyboard Martix building
https://www.google.com/search?q=building+a+keyboard+matrix&ie=UTF-8



Pico calc:

LCD:        PICO:  
     PIN  
1 GND   -- ANY GND  3,8,13,18,23,28,33,38
2 VCC   -- VBUS     40
3 SDA   -- I2C0 SDA 1  (GPIO0)
4 SDL   -- I2C0 SCL 2  (GPIO1)


Button
Button has 4 legs put button in the middle
of board to split.

Side 1                      Side 2
Pico pin 19 (GPIO14)        PIN 36 (3V3 OUT)
10k Resistor to GND