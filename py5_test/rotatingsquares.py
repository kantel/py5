# Rotating Squares
# nach einem Sketch von Peter Farrell
# Math Adventures with Python, San Francisco (No Starch Press) 2019, p87ff

WIDTH = 600
HEIGHT = 600

t = 0

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Rotating Squares")
    rect_mode(CENTER)

def draw():
    global t
    background(230, 226, 204)
    translate(width/2, height/2)    
    rotate(radians(t))
    for i in range(12):
        with push_matrix():
            translate(200, 0)
            rotate(radians(2*t))
            if i%2:
                fill(160, 51, 46)
            else:
                fill(50, 80, 105)
            rect(0, 0, 50, 50)
        rotate(radians(360/12))
    t += 1
