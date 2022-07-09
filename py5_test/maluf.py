WIDTH = 640    # 800
HEIGHT = 455   # 1000
STEP = 20      # 40
MARGIN = 10    # 20
OS = 50        # 150

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Hommage an Antonio Maluf")
    rect_mode(CENTER)
    no_loop()

def draw():
    no_stroke()
    step = STEP
    hs = step/2
    speed = 1/OS
    for y in range(MARGIN, height, step): 
        for x in range(MARGIN, width, step):
            w = hs + hs*cos(x*speed)*0.75
            h = hs + hs*sin(y*speed)*0.75
            fill(0)
            rect(x, y, w, h)
            next_x, next_y = x + step, y + step
            next_w = hs + hs * cos(next_x*speed)*0.75
            next_h = hs + hs * sin(next_y*speed)*0.75
            fill(255, 100, 0)
            xb = (x + w / 2 + next_x - next_w/2)/2
            yb = (y + h / 2 + next_y - next_h/2)/2
            wb = step - w /2 - next_w/2
            hb = step - h /2 - next_h/2
            rect(xb, yb, wb, hb)

    print("I did it, Babe")
    
