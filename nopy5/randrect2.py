# Random in Py5

WIDTH = 400
HEIGHT = 400
NO_RECT = 50

a = 150      # alpha

colors = ["#F6340C", "#156CD2", "#0D0B1B", "#F1E4E8", "#ECCA2D"]

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Random Rectangles – Genuary 2024")
    rect_mode(CENTER)
    no_loop()

def draw():
    background("#4F615D")
    for _ in range(NO_RECT):
        fill(random_choice(colors), a)
        rect_w = random_int(10, 80)
        rect_h = random_int(10, 80)
        rect(random_int(rect_w, width - rect_w), random_int(rect_h, height - rect_h),
             rect_w, rect_h)
    print("I did it, Babe!")
