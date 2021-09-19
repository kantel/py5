from pvector import PVector
import settings as s
import py5

class Sheep:
    
    def __init__ (self, x, y, col):
        self.pos = PVector(x, y)
        self.sz = 5      # Size
        self.move = 10
        self.energy = 20 # Energy level
        self.col = col
        
    def update(self):
        
        self.energy -= 1 # Walking costs energy
        self.pos.x += py5.random(-self.move, self.move)
        self.pos.y += py5.random(-self.move, self.move)
        self.check_boundaries()
        if self.energy >= 50:
            self.sz = 10
        elif self.energy >= 40:
            self.sz = 9
        elif self.energy >= 30:
            self.sz = 8
        elif self.energy >= 20:
            self.sz = 7
        elif self.energy >= 10:
            self.sz = 6
        else:
            self.sz = 5
        
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
        py5.fill(self.col)
        py5.circle(self.pos.x, self.pos.y, self.sz)