WIDTH = 640
HEIGHT = 200
STEP = 5

actor = None
x = 270
y = 75

def setup():
    global actor
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Hallo Kitty!")
    actor = load_image("horngirl.png")

def draw():
    global x
    background("#004477")
    image(actor, x, y)
    if is_key_pressed and key == CODED:
        if key_code == LEFT:
            x -= STEP
            if x <= 0:
                x = 0
        elif key_code == RIGHT:
            x += STEP
            if x >= width - 100:
                x = width - 100



# def key_pressed():
#     global x
#     if key == CODED:
#         if key_code == LEFT:
#             x -= STEP
#         if key_code == RIGHT:
#             x += STEP