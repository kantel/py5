# Bouncing Balls w/ Classes (improved)
# nach Peter Farrell »Math Adventures with Python«, p183ff
# Einige Ungereimtheiten aus Farrells Code ausgeräumt und
# für Py5 mit meiner eigenen PVector-Implementierung ausgestattet.
from pvector import PVector

NO_BALLS = 40
WIDTH = 640
HEIGHT = 480

balls = [] # Empty list to put the balls in

class Ball:
    
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(-2, 2), random(-2, 2))
        # No horizontal or vertical move
        if self.vel.x == 0:
            self.vel.x = 1
        if self.vel.y == 0:
            self.vel.y = -1
        # Random colors
        self.col = color(random_int(5, 250), random_int(5, 250), random_int(5, 250))
        # Random size
        self.r = random_int(5, 20)
        
    def update(self):
        self.pos += self.vel
        self.check_boundaries()
        
    def check_boundaries(self):
        # check boundaries
        if self.pos.x > width - self.r or self.pos.x < self.r:
            self.vel.x *= -1
        if self.pos.y > height - self.r or self.pos.y < self.r:
            self.vel.y *= -1
    
    def show(self):
        fill(self.col)
        circle(self.pos.x, self.pos.y, 2*self.r)

def setup():
    size(WIDTH, HEIGHT)
    for _ in range(NO_BALLS):
        balls.append(Ball(random(20, width - 20), random(20, height - 20)))

def draw():
    background(125)  # Light grey
    for ball in balls:
        ball.update()
        ball.show()