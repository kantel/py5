# PY5 IMPORTED MODE CODE

# Coding Train Farbpalette
codingtrain = [(240, 80, 37), (248, 158, 80), (248, 239, 34) , (240, 99, 164),
               (146, 82, 161), (129, 122, 198), (98, 199, 119)]

class Particle():
    
    def __init__(self, _x, _y):
        self.loc = Py5Vector(_x, _y)
        self.acc = Py5Vector(0, 0.05)
        self.vel = Py5Vector(random(-1.0, 1.0), random(-2.0, 0.0))
        self.col = random_choice(codingtrain)
        self.lifespan = 255.0
        self.d = 20
        
    def run(self):
        self.update()
        self.show()
        
    def update(self):
        self.vel += self.acc
        self.loc += self.vel
        self.lifespan -= random(0.5, 1.0)*2
        
    def show(self):
        stroke(0, self.lifespan)
        fill(self.col[0], self.col[1], self.col[2], self.lifespan)
        circle(self.loc.x, self.loc.y, self.d)
        
    def is_not_alive(self):
        if self.lifespan <= 0:
            return True
        else:
            return False
        
class RectParticle(Particle):
    
    def __init__(self, _x, _y):
        Particle.__init__(self, _x, _y)
        rect_mode(CENTER)
        self.rota = PI/3
    
    def show(self):
        stroke(0, self.lifespan)
        fill(self.col[0], self.col[1], self.col[2], self.lifespan)
        with push_matrix():
            translate(self.loc.x, self.loc.y)
            rotate(self.rota)
            rect(0, 0, 20, 20)
        self.rota += random(0.02, .10)
