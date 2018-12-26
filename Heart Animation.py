# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html
from microbit import *
import time

outerHeart = Image("09090:90009:90009:09090:00900")
hearts = [ Image.HEART_SMALL, outerHeart, Image.HEART ]
display.show(hearts,loop=True,delay=500)