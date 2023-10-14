# Pumpkin.py
# Halloween 2023

NO_PUMP = 25
WIDTH = 640
HEIGHT = 400

pumpkins = []                # Leere Liste, die die Kürbisse aufnimmt

class Pumpkin():
    
    def __init__(self, x, y):
        self.img = load_image("data/pumpkin.png")
        self.pos = Py5Vector(x, y)
        self.vel = Py5Vector(random(-2, 2), random(-2, 2))
        self.d = 36
        self.r = self.d//2
        # No horizontal or vertical move
        if self.vel.x == 0:
            self.vel.x = 1
        if self.vel.y == 0:
            self.vel.y = -1
    
    def update(self):
        self.pos += self.vel
        self.check_boundaries()
    
    def check_boundaries(self):
        if self.pos.x > width - self.d or self.pos.x < 0:
            self.vel.x *= -1
        if self.pos.y > height - self.d or self.pos.y < 0:
            self.vel.y *= -1
    
    def display(self):
        image(self.img, self.pos.x, self.pos.y, self.d, self.d)
        
        
    

def settings():
    size(WIDTH, HEIGHT)
    
def setup():
    window_title("Happy Halloween!")
    window_move(1300, 30)
    for _ in range(NO_PUMP):
        pumpkins.append(Pumpkin(random(6, width - 40), random(6, height - 40)))
    
def draw():
    background(120, 120, 120)  # Light grey
    for pumpkin in pumpkins:
        pumpkin.update()
        pumpkin.display()
    
    