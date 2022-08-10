# Hommage â Vasa Mihich
# Nach einer Idee von Joachim Wedekind
# Codierte Kunst, Seiten 75ff
from random import randint

WIDTH = 800
HEIGHT = 800

primaer   = [color(242, 119, 122), color(255, 212, 121), color(106, 126, 243)]
sekundaer = [color(252, 163, 105), color(255, 238, 166), color(118, 212, 214)]
tertiaer  = [color(146, 209, 146), color(225, 166, 242), color(172, 141, 88)]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Hommage â Vasa Mihich")
    background(45, 45, 45)
    stroke_weight(10)
    no_loop()
    
def draw():
    for i in range(width//24):
        stroke(primaer[randint(0, len(primaer) - 1)])
        line(i*width//12, 0, i*width//12, height)
    for j in range(height//24):
        stroke(sekundaer[randint(0, len(sekundaer) - 1)])
        line(0, j*height//12, width, j*height//12)
    for k in range(width//24):
        stroke(primaer[randint(0, len(primaer) - 1)])
        line((k*width//12) + width//24 , 0, (k*width//12) + width//24, height)
    for l in range(height//24):
        stroke(tertiaer[randint(0, len(tertiaer) - 1)])
        line(0, (l*height//12) + height//24, width, (l*height//12) + height//24)

print("I did it, Babe!")
    
    
    