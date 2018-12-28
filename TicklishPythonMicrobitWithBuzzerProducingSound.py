#https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html
#https://microbit-micropython.readthedocs.io/en/latest/pin.html

#With one hand, hold your device by the GND pin. 
#Then, with your other hand, touch (or tickle) 
#the 0 (zero) pin. You should see the display 
#change from grumpy to happy!

from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
        #Piezo Buzzer is connected to pin1
        pin1.write_digital(1)
    else:
        display.show(Image.SAD)
        pin1.write_digital(0)
    