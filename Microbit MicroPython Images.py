from microbit import *
import time
display.show(Image.ALL_CLOCKS, delay= 2000)

#images is a list
images = [Image.HAPPY,Image.HEART, Image.HEART_SMALL,Image.SAD,
Image.CONFUSED,Image.ANGRY,Image.ASLEEP,Image.SURPRISED,
Image.SILLY,Image.FABULOUS,Image.MEH,Image.YES,Image.NO,
Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1,
Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW,
Image.TRIANGLE,Image.TRIANGLE_LEFT,Image.CHESSBOARD,
Image.DIAMOND,Image.DIAMOND_SMALL,Image.SQUARE,
Image.SQUARE_SMALL,Image.RABBIT,Image.COW,
Image.MUSIC_CROTCHET,Image.MUSIC_QUAVER,Image.MUSIC_QUAVERS,
Image.PITCHFORK,Image.XMAS,Image.PACMAN,Image.TARGET,
Image.TSHIRT,Image.ROLLERSKATE,Image.DUCK,Image.HOUSE,
Image.TORTOISE,Image.BUTTERFLY,Image.STICKFIGURE,
Image.GHOST,Image.SWORD,Image.GIRAFFE,Image.SKULL,
Image.UMBRELLA,Image.SNAKE]
#loop = True, to loop forever
display.show(images, loop= False, delay=2000)

display.scroll("Hello, World!")
time.sleep(5)
display.show(Image.SMILE)
time.sleep(5)

#There are five lines of five numbers 
#so it’s possible to specify the individual brightness 
#for each of the five pixels on each of the five lines 
#on the physical display. 
#The values 1 to 8 represent the brightness levels between off (0) and full on (9).

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)
time.sleep(5)

plus = Image("00900:00900:99999:00900:00900")
display.show(plus)
time.sleep(5)
smily = Image("00000:00000:00000:90009:09990")
display.show(smily)

boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

boat2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boat3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boat4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050")

boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "05050")

boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
display.show(all_boats, delay=200)

light0 = Image("00000:00000:00000:00000:00000")
light1 = Image("11111:11111:11111:11111:11111")
light2 = Image("22222:22222:22222:22222:22222")
light3 = Image("33333:33333:33333:33333:33333")
light4 = Image("44444:44444:44444:44444:44444")
light5 = Image("55555:55555:55555:55555:55555")
light6 = Image("66666:66666:66666:66666:66666")
light7 = Image("77777:77777:77777:77777:77777")
light8 = Image("88888:88888:88888:88888:88888")
light9 = Image("99999:99999:99999:99999:99999")
lights = [light0,light1, light2,light3,light4,light5,
            light6, light7,light8,light9,
            light8,light7,light6,light5,light4,light3,
            light2,light1]
display.show(lights,loop=True,delay=2000)
#display.show(lights,loop=False,delay=2000)
time.sleep(5)