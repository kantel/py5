# Mein kleines, bonbonbuntes Aquarium
# Assets: Fish Pack von Kenney.nl <https://www.kenney.nl/assets/fish-pack>
from random import choice, randint

N_FISHES = 25      # Anzahl der Fische

class Actor():
    
    def __init__(self, sprite):
        self.img = load_image("data/" + sprite)
        self.x = 0
        self.y = 0
        
    def update(self):
        pass
    
    def display(self):
        image(self.img, self.x, self.y)
        
class Background(Actor):
    
    def __init__(self, img):
        Actor.__init__(self, img)
        
class Fish(Actor):
    
    def __init__(self, img, x, y, speed):
        Actor.__init__(self, img)
        self.imgstr = img
        self.img_left0 = self.imgstr[:5] + "l_0.png"
        self.imgl0 = load_image(self.img_left0)
        self.img_left1 = self.imgstr[:5] + "l_1.png"
        self.imgl1 = load_image(self.img_left1)
        self.img_right0 = self.imgstr[:5] + "r_0.png"
        self.imgr0 = load_image(self.img_right0)
        self.img_right1 = self.imgstr[:5] + "r_1.png"
        self.imgr0 = load_image(self.img_right1)
        self.x = x
        self.y = y
        self.speed = speed*randint(1, 3)
    
    def update(self):
        self.x += self.speed
        if self.x > 600:
            self.img = self.imgl0
            self.speed = randint(1, 3)
            self.speed *= -1
        if self.x < 40:
            self.img = self.imgr0
            self.speed *= randint(-3, -1)
        
    
fish_images = ["fish1", "fish2", "fish3", "fish4", "fish5", "fish6", "fish7"]
fishes = []

def setup():
    global bg
    size(640, 416)
    window_title("Jörgs kleines, bonbonbuntes Aquarium")
    window_move(1300, 40)
    bg = Background("background.png")
    for _ in range(N_FISHES):
        direction = randint(0, 1)
        if direction == 0:
            dr = "r"
            speed = 1
        else:
            dr = "l"
            speed = -1
        x = randint(40, 360)
        y = randint(20, 300)
        fish = Fish(choice(fish_images) + dr + "_0.png", x, y, speed)
        fishes.append(fish)
    print(fishes[0].img_left0)
    
def draw():
    background(49, 197, 244)
    bg.display()
    for fish in fishes:
        fish.update()
        fish.display()