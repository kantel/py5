# Random in Py5

WIDTH = 400
HEIGHT = 400
NO_RECT = 50

a = 150      # alpha

colors = [(43, 51, 95), (126, 32, 114), (25, 149, 156), (139, 72, 82),
          (57, 92, 152), (169, 193, 255),  (212, 24, 108), (211, 132, 65),
          (112, 198, 169), (118, 150, 222), (255, 151, 152), (237, 199, 176)]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Random Rectangles")
    rect_mode(CENTER)
    no_loop()

def draw():
    background(233, 195, 91)
    for _ in range(NO_RECT):
        c = random_choice(colors)
        fill(c[0][0], c[0][1], c[0][2], a)
        rect_w = random_int(10, 80)
        rect_h = random_int(10, 80)
        rect(random_int(rect_w, width - rect_w), random_int(rect_h, height - rect_h),
             rect_w, rect_h)
    print("I did it, Babe!")