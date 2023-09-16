"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
import turtle
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list([" a"," b"," c"," d"," e"," f"," g"," h"," i"," j"," k"," l"," m"," n"," o"," p"," q"," r"," s"," t"," u"," v"," w"," x"," y"," z"," /"," :"," ="," ~"," []"," :p"])*2
#changed from numbers to letters
state = {'mark': None}
hide = [True] * 64
Ntap = 0  # created Ntap for the number of taps made
Succesful_taps = 0 #Created a variable to hold how many tiles have been completed

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    #took the global variable and increased it every time there is a tap
    global Ntap
    Ntap=Ntap+1
    global Succesful_taps
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        Succesful_taps += 2
        if Succesful_taps == 64:
            goto(0,0)
            style ('white') 
            write ("CONGRATULATIONS, YOU WON!", align="center", font=("Comic Sans MS", 30, "normal"))

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write("taps=" + str(Ntap), align='left', font=('Comic Sans MS', 10, 'normal'))
        write( tiles[mark], font=('Comic Sans MS', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
