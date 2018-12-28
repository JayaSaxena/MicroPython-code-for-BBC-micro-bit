from microbit import *
import random

names = ["Aarav  ", "Akshath  ", "Saakshi  ", "Nana  ",
            "Alfred  ", "Aarti  ", "Aaron  ", "Mummy  ",
            "Mousi  "]
#while True:
display.scroll(random.choice(names))

#random.randint returns a whole number 
#between the two arguments, inclusive 
#display.show expects a character then we use the str function 
#to turn the numeric value into a character (we turn, 
#for example, 6 into "6").

#display.show(str(random.randint(1, 6)))

#random.random method. This only returns values 
#between 0.0 and 1.0 inclusive.
#Similar functions are also available.
