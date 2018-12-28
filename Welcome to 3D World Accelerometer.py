#accelerometer: an instrument for measuring the 
#acceleration of a moving or vibrating body.
#But, the sensor called accelerometer, just returns 
#a number to show the current tilt of the sensor, 
#each time it is called.
#https://microbit-micropython.readthedocs.io/en/latest/tutorials/movement.html

# Game controllers also contain accelerometers 
# to help you steer and move around in games.

#Driving Game can be made


from microbit import *

#reading = accelerometer.get_x()
#display.show(str(reading))
#Can be used to explain 3 Dimensions of our world - 
#X, Y and Z axis


def displayXReading(reading):
    #Right and Left tilt
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
    return
    
def displayYReading(reading):
    #Tilt to Show and Hide the sceen
    if reading > 20:
        display.show("S")
    elif reading < -20:
        display.show("H")
    else:
        display.show("-")
    return
    
def displayZReading(reading):
    #Up and Down
    if reading > 20:
        display.show("D")
    elif reading < -20:
        display.show("U")
    else:
        display.show("-")
    return
    
    
while True:
    xReading = accelerometer.get_x()
    yReading = accelerometer.get_y()
    zReading = accelerometer.get_z()
    if(abs(xReading) > abs(yReading)):
        if(abs(xReading) > abs(zReading)):
            displayXReading(xReading)
        else:
            displayZReading(zReading)
    else:
        if(abs(yReading) > abs(zReading)):
            displayYReading(yReading)
        else:
            displayZReading(zReading)
            