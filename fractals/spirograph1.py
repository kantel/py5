# Fractal Spirograph

WIDTH  = 600
HEIGHT = 600

mikart = [color(255, 13, 12), color(0, 187, 100), color(1, 152, 221),
         color(251, 177, 0), color(253, 84, 3), color(221, 15, 160)]

ci = 0    # Farbindex

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Fraktaler Spirograph als Punktmenge")
    background(235, 215, 182)   # Packpapier
    stroke_weight(2)
    # stroke(caseincolors[1])
    
def draw():
    global ci
    stroke(mikart[ci])
    translate(width/2, height/2)
    R, k = 120, 1
    for i in range(5):
        rotate(frame_count*k*5**i/36)
        translate(R + R/3, 0)
        R /= 3
        k = -k
    point(0, 0)
    if frame_count%500 == 0:
        ci += 1
        ci %= len(mikart)
        # print(ci)
    if frame_count == 7500:
        print("I did it Babe!")
        no_loop()
