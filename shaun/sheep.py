from pvector import PVector
import settings as s
import py5

class Sheep:
    
    def __init__ (self, x, y):
        self.pos = PVector(x, y)
        self.sz = 10 # Size
        self.energy = 200 # Energy level
        
    def update(self):
        move = 10
        self.energy -= 1 # Walking costs energy
        self.pos.x += py5.random(-move, move)
        self.pos.y += py5.random(-move, move)
        self.check_boundaries()
        
    def check_boundaries(self):
        if self.pos.x >= s.WIDTH - self.sz/2:
            self.pos.x = s.WIDTH - self.sz/2
        if self.pos.x <= self.sz/2:
            self.pos.x = self.sz/2
        if self.pos.y >= s.HEIGHT - self.sz/2:
            self.pos.y = s.HEIGHT - self.sz/2
        if self.pos.y <= self.sz/2:
            self.pos.y = self.sz/2
        
    
    def show(self):
        py5.fill(s.WHITE)
        py5.circle(self.pos.x, self.pos.y, self.sz)