# Py5 Game 2
# Load images from a spritesheet and animate them
WIDTH  = 416
HEIGHT = 384
frame = 0
frames = 4
timer = 20    # 1: rasend schnell -> 60: laaaangsam
me = []

def setup():
    global bg, me
    size(WIDTH, HEIGHT)
    window_title("Me at Home 2")
    bg = load_image("assets/home.png")
    sprite_sheet = load_image("assets/wilson.png")
    # Wilsons sprite size is 32x49. Wilsons stand position is at (36, 102).
    for _ in range(frames):
        pic = create_image(32, 49, ARGB)
        me.append(pic)
    # Down: 0 - 3
    me[0].copy(sprite_sheet,  1, 102, 32, 49, 0, 0, 32, 49)
    me[1].copy(sprite_sheet, 36, 102, 32, 49, 0, 0, 32, 49)
    me[2].copy(sprite_sheet, 73, 102, 32, 49, 0, 0, 32, 49)
    me[3].copy(sprite_sheet, 36, 102, 32, 49, 0, 0, 32, 49)
    frame_rate(60)

def draw():
    global bg, me, frame
    background("white")
    image(bg, 0, 0)
    image(me[frame], 150, 75)
    if frame < frames:
        if frame_count % timer == 0:
            frame = (frame + 1) % frames
