from processing.pdf import *
from random import randint

WIDTH = 940
HEIGHT = 315

malewitsch1 = [color(42, 40, 45), color(54, 50, 80), color(50, 80, 105),
               color(160, 51, 46), color(180, 144, 55), color(140, 82, 48),
               color(215, 158, 40)]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Random Circles High Resolution")
    background(230, 226, 204)
    stroke_weight(1)    # ellipse_mode(RADIUS)
    no_loop()
    begin_record(PDF, "randcirc.pdf")

def draw():
    for _ in range(200):
        x = randint(50, width - 50)
        y = randint(50, height - 50)
        stroke(0, 150)
        fill(malewitsch1[(randint(0, len(malewitsch1) - 1))], 255)
        circle(x, y, 10)
        no_stroke()
        fill(malewitsch1[(randint(0, len(malewitsch1) - 1))], 100)
        radius = randint(7, 35)
        circle(x, y, 2*radius)
    end_record()
    print("I did it, Babe!")

