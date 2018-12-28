from microbit import *
import random

#Sometimes you want to have repeatable random-ish behaviour: 
#a source of randomness that is reproducible. It’s like 
#saying that you need the same five random values each time 
#you throw a dice.
#This is easy to achieve by setting the seed value. 
#Given a known seed the random number generator 
#will create the same set of random numbers. 
#The seed is set with random.seed and any whole number 
#(integer). This version of the dice program always 
#produces the same results:

random.seed(1337)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))
        