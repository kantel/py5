import py5
import math

t = 0

def setup():
    py5.size(600, 600)
    py5.window_title("Rotating Squares 🐍")

def draw():
    global t
    py5.background("#9252a1")
    py5.fill("#f05025")
    py5.translate(py5.width/2, py5.height/2)
    py5.rotate(math.radians(t))
    for _ in range(12):
        py5.rect(200, 0, 50, 50)
        py5.rotate(math.radians(360/12))
    t += 1

py5.run_sketch()