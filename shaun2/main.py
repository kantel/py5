# Shaun das Schaf: Es kann nur eine Farbe geben!

from sheep import Sheep
import settings as s

# Farben der Schafe: blue, red, magenta, white, yellow
colors = ["blue", "red", "magenta", "white", "yellow"]
sheeps = []           # Array Schafe

def settings():
    size(s.window_width, s.window_height)    
    
def setup():
    window_title("Shaun das Schaf – es kann nur eine Farbe siegen!")
    window_move(1300, 30)
    
    # Bilder laden
    ## Blaue Schafe
    blue_left = load_image("data/sheep_left_blue.png")
    blue_right = load_image("data/sheep_right_blue.png")
    ## Rote Schafe
    red_left = load_image("data/sheep_left_red.png")
    red_right = load_image("data/sheep_right_red.png")
    ## Rosa Schafe
    magenta_left = load_image("data/sheep_left_magenta.png")
    magenta_right = load_image("data/sheep_right_magenta.png")
    ## Weiße Schafe
    white_left = load_image("data/sheep_left_white.png")
    white_right = load_image("data/sheep_right_white.png")
    ## Gelbe Schafe
    yellow_left = load_image("data/sheep_left_yellow.png")
    yellow_right = load_image("data/sheep_right_yellow.png")
    
    # Schafe initialisieren
    for _ in range(s.no_sheeps):
        c = random_choice(colors)
        if c == "blue":
            im_l, im_r = blue_left, blue_right
        elif c == "red":
            im_l, im_r = red_left, red_right
        elif c == "magenta":
            im_l, im_r = magenta_left, magenta_right
        elif c == "white":
            im_l, im_r = white_left, white_right
        elif c == "yellow":
            im_l, im_r = yellow_left, yellow_right
        sheep = Sheep(random(2, s.cols - 2), random(2, s.rows - 2), im_l, im_r)
        sheeps.append(sheep)
        
def draw():
    background(s.GREEN)
    for sheep in sheeps:
        sheep.update()
        sheep.display()