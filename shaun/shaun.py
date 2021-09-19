# Shaun das Schaf und seine Spießgesellen
# nach Peter Farrell »Math Adventures in Python«, p168ff
from sheep import Sheep
from grass import Grass
import settings as s

sheeps = [] # List to store sheeps
grasses = [] # List to store grass patches
colors = [s.WHITE, s.RED, s.BLUE, s.YELLOW]


def setup():
    size(s.WIDTH, s.HEIGHT)
    global row_of_grass
    row_of_grass = height/s.patch_size
    # Initialize a list with sheeps
    for _ in range(s.NO_SHEEPS):
        sheeps.append(Sheep(random_int(50, width - 50),
                            random_int(50, height - 50), random_choice(colors)))
    # Create the grass
    for x in range(0, width, s.patch_size):
        for y in range(0, height, s.patch_size):
            grasses.append(Grass(x, y, s.patch_size))

def draw():
    background(s.WHITE)
    for grass in grasses:
        grass.update()
        grass.show()
    for sheep in sheeps:
        sheep.update()
        xscl = int(sheep.pos.x/s.patch_size)
        yscl = int(sheep.pos.y/s.patch_size)
        grass = grasses[int(xscl*row_of_grass + yscl)]
        if not grass.eaten:
            sheep.energy += grass.energy
            grass.eaten = True
        if sheep.energy <= 0:
            sheeps.remove(sheep)
        if sheep.energy >= 50:
            sheep.energy -= 30  # Giving birth takes energy
            # Add a new sheep to the list
            sheeps.append(Sheep(sheep.pos.x, sheep.pos.y, sheep.col))
            
        sheep.show()
        # print("Anzahl der Schafe: " + str(len(sheeps)))