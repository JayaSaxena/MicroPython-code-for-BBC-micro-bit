import music
#https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html
#http://www.microbitsandbobs.co.uk/projects/Project31.pdf

# Use crocodile clips to attach pin 0 and GND to the 
#positive and negative inputs on the speaker - 
#it doesn’t matter which way round they are connected 
#to the speaker. Do not attempt this with a Piezo buzzer - 
#such buzzers are only able to play a single tone.

#Connecting a head phone worked!!!
#music.play(music.NYAN)
#while True:
    #music works only on pin0
    #music.play(music.BIRTHDAY)
    
#Next Christmas, Jingle Bell sound will come from XMas Tree
#with lights dancing with the music 

#NOTE[octave][:duration]

jingle = [
 "e:2","e:2","e:4",
 "e:2","e:2","e:4",
 "e:2","g:2","c:1","d:1",
 "e:8",
 "f:2","f:2","f:3",
 "f:1","f:2","e:2",
 "e:2","e:1","e:1",
 "e:2","d:2","d:2",
 "e:2","d:4","g:4",
 "e:2","e:2","e:4",
 "e:2","e:2","e:4",
 "e:2","g:2","c","d",
 "e:8","f:2","f:2","f:2",
 "f:2","f:2","e:2",
 "e:2","e:1","e:1",
 "g:2","g:2","f:2",
 "d:2", "c:4"
]

i = 0
while True: #i < 5:
    music.play(jingle)
    i = i + 1
    
'''while True:
    for freq in range(880, 1760, 16):
        music.pitch(freq, 6)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 6)
'''        