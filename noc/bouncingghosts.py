# Bouncing Balls w/ Classes (improved)
# nach Andrew Glassner: Processing for Visual Artists, p. 341pp
from random import randint

WIDTH = 600
HEIGHT = 400
BG_COLOR = color(240, 215, 175)  # color(164, 164, 164)
a = 50              # alpha
BORDER = 50
NO_GHOSTS = 30

class Disk():
    
    def __init__(self, _x, _y, _vx, _vy, _radius, _col):
        self.r = _radius
        self.d = self.r*2
        self.c = _col
        self.pos = Py5Vector(_x, _y)
        self.vel = Py5Vector(_vx, _vy)
    
    def check_boundaries(self):
        if self.pos.x > width - self.r or self.pos.x < self.r:
            self.vel.x *= -1
            self.pos.x += 2*self.vel.x
        if self.pos.y > height - self.r or self.pos.y < self.r:
            self.vel.y *= -1
            self.pos.y += 2*self.vel.y
    
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
    
    def show(self):
        stroke(0)
        stroke_weight(1)
        fill(self.c)
        circle(self.pos.x, self.pos.y, self.d)
        
ghosts = []

def build_ghosts(n):
    border = BORDER
    for _ in range(n):
        xpos = randint(border, width - border)
        ypos = randint(border, height - border)
        xvel = randint(-2, 2)
        # no vertical move
        if xvel == 0: xvel = -1
        yvel = randint(-2, 2)
        # no horizontal move
        if yvel  == 0: yvel = 1
        radius = randint(10, 20)
        clr = color(randint(20, 230), randint(20, 230), randint(20, 230), a)
        ghost = Disk(xpos, ypos, xvel, yvel, radius, clr)
        ghosts.append(ghost)
                    
def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Bouncing Ghosts")
    build_ghosts(NO_GHOSTS)
    
def draw():
    no_stroke()
    fill(BG_COLOR, 30)
    rect(0, 0, width, height)
    for ghost in ghosts:
        ghost.show()
        ghost.check_boundaries()
        ghost.update()