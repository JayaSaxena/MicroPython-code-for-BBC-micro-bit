#https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html
from microbit import *

sleep(10000)
#button_a.get_presses() returns the number of times button a was pressed
display.scroll(str(button_a.get_presses()))

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.CONFUSED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SURPRISED)
        break;
    else:
        display.show(Image.SAD)
display.clear()