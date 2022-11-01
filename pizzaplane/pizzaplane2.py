# Pizza Plane Stage 2
# Endless Scrolling Background
# Background Image: »PWL« (https://opengameart.org/content/seamless-desert-background-in-parts)
# Aeroplane: Tappy Plane, Kenney (https://www.kenney.nl/assets/tappy-plane)

WIDTH = 720
HEIGHT = 480
BG_WIDTH    = 1067   # Breite des Hintergrundbildes


class Background():
    
    def __init__(self):
        self.back1 = load_image("data/desert.png")
        self.back2 = self.back1
        self.bx = 0
        
    def update(self):
        self.bx -= 1
        if self.bx == -BG_WIDTH:
            self.bx = 0
    
    def show(self):
        image(self.back1, self.bx, 0)
        image(self.back2, BG_WIDTH + self.bx, 0)

class Plane():
        
    def __init__(self):
        self.planes = []
        for i in range(3):
            plane = load_image("data/planered_" + str(i) + ".png")
            self.planes.append(plane)
        self.h = 37    # Höhe des Sprites
        self.r = 0
        self.x = 50
        self.y = 200
        self.updown = 5
        self.state = "NULL"
    
    def update(self):
        if self.state == "UP":
            self.y -= self.updown
            if self.y <= 0:
                self.y = 0
        elif self.state == "DOWN":
            self.y += self.updown
            if self.y >= height - self.h:
                self.y = height - self.h
        elif self.state == "NULL":
            self.y = self.y
        self.r += 0.2
        if self.r >= 3:
            self.r = 0
             
    def show(self):
        image(self.planes[int(self.r)], self.x, self.y)
    
class Missile():
    
    def __init__(self):
        self.img = load_image("data/missile.png")
        self.x = plane.x + 44
        self.y = plane.y + 20
        # self.fire = False
        self.firecount = 0
        self.speed = 0
    
    def update(self):
        if self.firecount < 0:
            self.speed = 20
            self.x += self.speed
            self.firecount = 1
            if self.x >= width + 40:
                self.x = plane.x + 44
                self.y = plane.y + 20
                self.speed = 0
        self.firecount -= 1
    
    def show(self):
        image(self.img, self.x, self.y)
                
        
def setup():
    global bg, plane, missile
    size(WIDTH, HEIGHT)
    window_title("Pizza Plane 2 with Py5 and Classes")
    window_move(1300, 30)
    bg = Background()
    plane = Plane()
    missile = Missile()
    
def draw():
    global bg, plane, missile
    bg.show()
    bg.update()
    plane.update()
    plane.show()
    missile.update()
    missile.show()
        

def key_pressed():
    if key_pressed and key == CODED:
        if key_code == UP:
            plane.state = "UP"
        if key_code == DOWN:
            plane.state = "DOWN"
    if key == " ":   # SPACE
        missile.firecount = 0

def key_released():
    plane.state = "NULL"
