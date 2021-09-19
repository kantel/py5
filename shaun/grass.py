from pvector import PVector
import settings as s
import py5

class Grass:
    
    def __init__(self, x, y, sz):
        self.pos = PVector(x, y)
        self.energy = 3    # Energy from eating this patch
        self.eaten = False # Hasn't been eaten yet
        self.sz = sz       # Patch size
    
    def update(self):
        if self.eaten:
            if py5.random_int(250) < 5:
                self.eaten = False  # Regeneration
            else:
                py5.fill(s.BROWN)
        else:
            py5.fill(s.GREEN)
        
    def show(self):
        py5.rect(self.pos.x, self.pos.y, self.sz, self.sz)