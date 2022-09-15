# Fractal Spirograph

WIDTH  = 600
HEIGHT = 600

caseincolors = [color(40, 129, 46), color(55, 42, 33), color(222, 106, 35),
                color(181, 115, 65), color(180, 100, 60), color(255, 80, 32), 
                color(250, 50, 37), color(200, 40, 25), color(180, 45, 39), 
                color(122, 41, 37), color(160, 30, 45), color(30, 25, 50), 
                color(23, 23, 23), color(66, 114, 188), color(45, 78, 185),
                color(60, 117, 160), color(25, 79, 53), color(75, 102, 54)]
ci = 0    # Farbindex

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Fractal Spirograph")
    background(235, 215, 182)   # Packpapier
    stroke_weight(2)
    # stroke(caseincolors[1])
    
def draw():
    global ci
    stroke(caseincolors[ci])
    translate(width/2, height/2)
    R, k = 120, 1
    for i in range(5):
        rotate(frame_count*k*5**i/36)
        translate(R + R/3, 0)
        R /= 3
        k = -k
    point(0, 0)
    if frame_count%120 == 0:
        ci += 1
        ci %= len(caseincolors)
        # print(ci)
