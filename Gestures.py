from microbit import *
''' 
The following gustures are available::
up, .... board is standing 
down,... in head stand position
left, ... left turn, between face up and face down
right, .... took right turn while sleeping
face up,...... board is sleeping 
face down,......board's lights are facing the ground
freefall,
3g, 6g, 8g,
shake
'''
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)