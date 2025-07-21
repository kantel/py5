import py5
from random import randint

WIDTH, HEIGHT = 640, 480
ITER = 10000
RAD = 5

# Parameter
a = -0.48
b = 0.93

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.window_title("Fantastic Feather Fractal")
    py5.background(132, 144, 163)
    py5.stroke_weight(1)
    py5.no_loop()

def f(x):
    return a * x - (1.0 - a) * ((2 * (x**2)) / (1.0 + x**2))

def draw():
    x = 4.0
    y = 0.0
    for _ in range(ITER):
        x1 = b * y + f(x)
        y = -x + f(x1)
        x = x1
        # Skalierungsparameter für die Fenstergröße:
        xx = int(350 + x*26)
        yy = int(280 - y*26)
        red_val = randint(100, 250)
        green_val = randint(100, 250)
        blue_val = randint(100, 250)
        py5.fill(red_val, green_val, blue_val)
        py5.circle(xx, yy, RAD)
    print("I did it, Babe!")

py5.run_sketch()