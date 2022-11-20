# Mein kleines, bonbonbuntes Aquarium
# Assets: Fish Pack von Kenney.nl <https://www.kenney.nl/assets/fish-pack>
from random import randint

N_FISHES = 25      # Anzahl der Fische

        
class Background():
    
    def __init__(self, img):
        self.img = load_image("data/" + img + ".png")
    
    def display(self):
        image(self.img, 0, 0)
        
class Fish():
    
    def __init__(self, idx, x, y, dr, speed):
        self.imgr0 = load_image("data/fish" + str(idx) + "r_0.png")
        self.imgl0 = load_image("data/fish" + str(idx) + "l_0.png")
        self.imgr1 = load_image("data/fish" + str(idx) + "r_1.png")
        self.imgl1 = load_image("data/fish" + str(idx) + "l_1.png")
        self.x = x
        self.y = y
        self.dir = dr
        if self.dir == "rt":
            self.img = self.imgr0
        elif self.dir == "lt":
            self.img = self.imgl0
        self.speed = speed*randint(1, 3)
        self.switch = 5
        self.timer = self.switch
    
    def update(self):
        self.x += self.speed
        if self.timer <= 0:
            self.timer = self.switch
            if self.img == self.imgr0:
                self.img = self.imgr1
            elif self.img == self.imgr1:
                self.img = self.imgr0
            elif self.img == self.imgl0:
                self.img = self.imgl1
            elif self.img == self.imgl1:
                self.img = self.imgl0
        if self.x > width + randint(40, 200):
            self.img = self.imgl0
            self.y = randint(20, 300)
            self.speed = randint(-3, -1)
        if self.x < randint(-200, -40):
            self.img = self.imgr0
            self.y = randint(20, 300)
            self.speed = randint(1, 3)
        self.timer -= 1
        
    def display(self):
        image(self.img, self.x, self.y)

fishes = []
    
def setup():
    global bg
    size(640, 416)
    window_title("🐠 Jörgs kleines, bonbonbuntes Aquarium 🐡")
    window_move(1300, 40)
    bg = Background("background")
    for _ in range(N_FISHES):
        direction = randint(0, 1)
        if direction == 0:
            dr = "rt"
            speed = 1
        else:
            dr = "lt"
            speed = -1
        x = randint(-100, width + 200)
        y = randint(20, 300)
        fish = Fish(randint(1, 7), x, y, dr, speed)
        fishes.append(fish)

def draw():
    background(49, 197, 244)
    bg.display()
    for fish in fishes:
        fish.update()
        fish.display()