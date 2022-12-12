## Autonome Agenten 1
## Nach Daniel Shiffman: »The Nature of Code«, S. 260 ff

class Vehicle():
    
    def __init__(self,_x,_y):
        self.acc = Py5Vector(0, 0)    # Acceleration
        self.vel = Py5Vector(0, 0)    # Velocity
        self.loc = Py5Vector(_x, _y)  # Location
        self.r = 3.0
        self.maxspeed = 4.0           # Arbitrary value for maximum speed
        self.maxforce = 0.1           # Arbitrary value for maximum force
    
    def update(self):                 # Eulersche Polygonzug-Methode
        self.vel += self.acc
        self.vel.set_limit(self.maxspeed)
        self.loc += self.vel
        self.acc *= 0
        
    def apply_force(self, force):
        self.acc += force
        
    def seek(self, target):
        desired = Py5Vector(target - self.loc)
        desired.normalize()
        desired *= self.maxspeed
        steer = (desired - self.vel)
        steer.set_limit(self.maxforce)
        self.apply_force(steer)
        
    def display(self):
        theta = self.vel.heading + PI/2     # +PI/2 = Ausrichtung nach Osten
        fill(240, 80, 37)
        stroke(0)
        with push_matrix():
            translate(self.loc.x, self.loc.y)
            rotate(theta)
            with begin_closed_shape():
                vertex(0,      -self.r*2)
                vertex(-self.r, self.r*2)
                vertex(self.r,  self.r*2)

WIDTH = 400
HEIGHT = 400

def setup():
    global vehicle
    size(WIDTH, HEIGHT)
    window_title("🐁 Wo ist das Mäuschen? 🐁")
    window_move(1300, 40)
    vehicle = Vehicle(width/2, height/2)
    
def draw():
    background(49, 197, 244)
    target = Py5Vector(mouse_x, mouse_y)
    vehicle.seek(target)
    vehicle.update()
    vehicle.display()
        