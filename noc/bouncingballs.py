# Bouncing Balls w/ Classes (improved)
# nach Peter Farrell »Math Adventures with Python«, p183ff
# Einige Ungereimtheiten aus Farrells Code ausgeräumt und
# erstmals Py5Vector anstelle meiner eigenen PVector-Implementierung genutzt
from random import randint, choice

WIDTH = 640
HEIGHT = 480
NO_BALLS = 40

# Coding Train Farbpalette
codingtrain = [(240, 80, 37), (248, 158, 80), (248, 239, 34) , (240, 99, 164),
               (146, 82, 161), (129, 122, 198), (98, 199, 119)]

class Ball():
    
    def __init__(self):
        self.radius = randint(8, 24)
        self.dia = 2*self.radius
        self.location = Py5Vector(randint(self.dia, WIDTH - self.dia),
                                  randint(self.dia, HEIGHT - self.dia))
        self.vel = Py5Vector(random(-2, 2), random(-2, 2))
        # No horizontal or vertical move
        if self.vel.x == 0:
            self.vel.x = 1
        if self.vel.y == 0:
            self.vel.y = -1
        self.dir = Py5Vector(-1.5, 1.5)
        self.col = choice(codingtrain)
        
    def update(self):
        self.location.x += self.vel.x*self.dir.x
        self.location.y += self.vel.y*self.dir.y
    
    def show(self):
        fill(self.col[0], self.col[1], self.col[2])
        circle(self.location.x, self.location.y, self.dia)
    
    def check_boundaries(self):
        if self.location.x > width - self.radius or self.location.x < self.radius:
            self.vel.x *= -1
        if self.location.y > height - self.radius or self.location.y < self.radius:
            self.vel.y *= -1            
balls = []       

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Bouncing Balls w/Py5Vector")
    for _ in range(NO_BALLS):
        balls.append(Ball())

def draw():
    background(49, 197, 244)   # Hellblau
    for ball in balls:
        ball.show()
        ball.check_boundaries()
        ball.update()
