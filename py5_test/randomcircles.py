WIDTH = 640
HEIGHT = 480

malewitsch1 = [color(42, 40, 45), color(54, 50, 80), color(50, 80, 105),
               color(160, 51, 46), color(180, 144, 55), color(140, 82, 48),
               color(215, 158, 40)]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Random Circles")
    background(230, 226, 204)
    stroke_weight(1)
    # ellipse_mode(RADIUS)

def draw():
    pass

def mouse_released():
    x = random(width)
    y = random(height)
    radius = random(100) + 10     # Jeder Außenkreis hat mindestens einen Radius >= 10
    fill(malewitsch1[floor(random(len(malewitsch1)))], 150)
    no_stroke()
    circle(x, y, 2*radius)
    fill(malewitsch1[floor(random(len(malewitsch1)))], 255)
    stroke(0, 150)
    circle(x, y, 10)
    
