# Random in Py5

WIDTH = 400
HEIGHT = 400
NO_RECT = 50

a = 150      # alpha

colors = [color(43, 51, 95), color(126, 32, 114), color(25, 149, 156), color(139, 72, 82),
          color(57, 92, 152), color(169, 193, 255),  color(212, 24, 108), color(211, 132, 65),
          color(112, 198, 169), color(118, 150, 222), color(255, 151, 152), color(237, 199, 176)]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Random Rectangles")
    rect_mode(CENTER)
    no_loop()

def draw():
    background(233, 195, 91)
    for _ in range(NO_RECT):
        fill(random_choice(colors), a)
        rect_w = random_int(10, 80)
        rect_h = random_int(10, 80)
        rect(random_int(rect_w, width - rect_w), random_int(rect_h, height - rect_h),
             rect_w, rect_h)
    print("I did it, Babe!")