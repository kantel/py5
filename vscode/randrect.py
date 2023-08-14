# Random Rectangles in Py5
# Module Mode
import py5

WIDTH = 400
HEIGHT = 400
NO_RECT = 50

a = 150      # alpha

colors = [py5.color(43, 51, 95), py5.color(126, 32, 114), py5.color(25, 149, 156),
          py5.color(139, 72, 82), py5.color(57, 92, 152), py5.color(169, 193, 255),
          py5.color(212, 24, 108), py5.color(211, 132, 65), py5.color(112, 198, 169),
          py5.color(118, 150, 222), py5.color(255, 151, 152), py5.color(237, 199, 176)]

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.window_move(1400, 30)
    py5.window_title("Random Rectangles")
    py5.rect_mode(py5.CENTER)
    py5.no_loop()

def draw():
    py5.background(233, 195, 91)
    for _ in range(NO_RECT):
        py5.fill(py5.random_choice(colors), a)
        rect_w = py5.random_int(10, 80)
        rect_h = py5.random_int(10, 80)
        py5.rect(py5.random_int(rect_w, py5.width - rect_w),
                 py5.random_int(rect_h, py5.height - rect_h),
                 rect_w, rect_h)
    print("I did it, Babe!")

py5.run_sketch()