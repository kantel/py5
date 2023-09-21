## Forest Fire Simulation
from random import randint, uniform

TS = 16   # Tilesize
N_ROWS, N_COLS = 40, 30
SCREEN_WIDTH, SCREEN_HEIGHT = N_ROWS*TS, N_COLS*TS

empty = 0
tree = 1
burning = 20
w = h = TS

a = 4.0     # Wachstumswahrscheinlichkeit in Prozent
b = 0.2     # Wahrscheinlichkeit Blitzeinschlag in Prozent

grid = []
newgrid = []

def setup():
    global tree_image, fire_image
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    window_title("🌲 Forest Fire Simulation 🔥")
    window_move(1300, 30)
    tree_image = load_image("data/tree.png")
    fire_image = load_image("data/fire.png")
    create_new_forest()
    newgrid[:] = grid[:]
    frame_rate(1)
    
def draw():
    # global tree
    background(210, 180, 140)
    display_forest()
    calc_next()

def create_new_forest():
    for x in range(N_ROWS):
        grid.append([])
        newgrid.append([])
        for y in range(N_COLS):
            # Randbedingugen
            if ((x > 0) and (y > 0) and (x < N_ROWS - 1)
                and (y < N_COLS - 1) and randint(0, 100) <= 50):
                grid[x].append(tree)
            else:
                grid[x].append(empty)

def display_forest():
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if grid[i][j] == tree:
                image(tree_image, i*w, j*h, w, h)
            elif grid[i][j] == burning:
                image(fire_image, i*w, j*h, w, h)

def calc_next():
    newgrid[:] = grid[:]
    # Next Generation
    for i in range(1, N_ROWS - 1):
        for j in range(1, N_COLS - 1):
            if grid[i][j] == burning:
                newgrid[i][j] = empty
                # Nachbarbaum anzünden (von-Neumann-Nachbarschaft)
                if grid[i-1][j] == tree:
                    newgrid[i-1][j] = burning
                if grid[i][j-1] == tree:
                    newgrid[i][j-1] = burning
                if grid[i][j+1] == tree:
                    newgrid[i][j+1] = burning
                if grid[i+1][j] == tree:
                    newgrid[i+1][j] = burning
            ## Neuer Baum?
            elif grid[i][j] == empty:
                if uniform(0, 100) < a:
                    newgrid[i][j] = tree
            # Schlägt ein Blitz ein?
            if grid[i][j] == tree:
                if uniform(0, 100) < b:
                    newgrid[i][j] = burning
    grid[:] = newgrid[:]
                
                
                
                
                