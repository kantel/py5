WIDTH = 400
HEIGHT = 200

actor = None

def setup():
    global actor
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Hallo Kitty!")
    actor = load_image("horngirl.png")

def draw():
    background("#004477")
    image(actor, width/2 - 50, height/2 - 50)