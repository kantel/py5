import py5
from random import choice

simcode2 = [py5.color(92,97,130), py5.color(79,164,165), py5.color(202,166,122),
            py5.color(212,117,100)]

def setup():
    py5.size(640, 480)
    py5.window_title("Py5 lebt!")
    py5.background(30, 30, 30)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.fill(choice(simcode2))
    py5.circle(py5.mouse_x, py5.mouse_y, 20)

py5.run_sketch()