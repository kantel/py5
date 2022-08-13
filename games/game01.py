# Py5 Game 1

WIDTH  = 416
HEIGHT = 384

def setup():
    global bg, me
    size(WIDTH, HEIGHT)
    window_title("Me at Home 1")
    bg = load_image("assets/home.png")
    sprite_sheet = load_image("assets/wilson.png")
    # Wilsons sprite size is 32x49.
    # Wilsons stand position is at (36, 102).
    me = create_image(32, 49, ARGB)
    me.copy(sprite_sheet, 35, 102, 32, 49, 0, 0, 32, 49)


def draw():
    global bg, me
    background("white")
    image(bg, 0, 0)
    image(me, 150, 75)