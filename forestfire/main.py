## Forest Fire Simulation
from random import randint, uniform

TS = 16       # Tilesize
N_ROWS, N_COLS = 40, 30
PLOT_WIDTH = 720
PLOT_HEIGHT = N_COLS*TS
SCREEN_WIDTH, SCREEN_HEIGHT = N_ROWS*TS, N_COLS*TS   # 640x480 Pixel
# SCREEN_WIDTH, SCREEN_HEIGHT = N_ROWS*TS + PLOT_WIDTH, N_COLS*TS   # 640x480 Pixel + Plotbereich

empty = 0
tree = 1
burning = 20
w = h = TS

a = 4.0        # Wachstumswahrscheinlichkeit in Prozent
b = 0.2        # Wahrscheinlichkeit Blitzeinschlag in Prozent
s = 50         # Startbepflanzung in Prozent

grid = []
newgrid = []

trees = []
fires = []

def setup():
    global tree_image, fire_image, no_trees, no_fire
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    window_title("🌲 Forest Fire Simulation 🔥")
    window_move(1300, 30)
    tree_image = load_image("data/tree.png")
    fire_image = load_image("data/fire.png")
    no_trees = no_fire = 0
    create_new_forest()
    newgrid[:] = grid[:]
    frame_rate(1)
    print("Start: Bäume = ", no_trees, " Brände = ", no_fire)
    trees.append(no_trees)
    fires.append(no_fire)
    
def draw():
    background(210, 180, 140)
    print("Runde: ", frame_count, " Bäume = ", no_trees, " Brände = ", no_fire)
    display_plot()
    trees.append(no_trees)
    fires.append(no_fire)
    display_forest()
    calc_next()
    if frame_count == 30:
        no_loop()

def display_plot():
    pass

def create_new_forest():
    global no_trees
    for x in range(N_ROWS):
        grid.append([])
        newgrid.append([])
        for y in range(N_COLS):
            # Erstbepflanzung Wald
            if ((x > 0) and (y > 0) and (x < N_ROWS - 1)
                and (y < N_COLS - 1) and randint(0, 100) <= s):
                grid[x].append(tree)
                no_trees += 1
            else:
                # Ränder bleiben leer
                grid[x].append(empty)

def display_forest():
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if grid[i][j] == tree:
                image(tree_image, i*w, j*h, w, h)
            elif grid[i][j] == burning:
                image(fire_image, i*w, j*h, w, h)

def calc_next():
    global no_trees, no_fire
    newgrid[:] = grid[:]
    # Next Generation, Randfelder ignorieren
    for i in range(1, N_ROWS - 1):
        for j in range(1, N_COLS - 1):
            if grid[i][j] == burning:
                newgrid[i][j] = empty
                no_fire -= 1
                # Nachbarbaum anzünden (von-Neumann-Nachbarschaft)
                if grid[i-1][j] == tree:
                    newgrid[i-1][j] = burning
                    no_trees -= 1
                    no_fire += 1
                if grid[i][j-1] == tree:
                    newgrid[i][j-1] = burning
                    no_trees -= 1
                    no_fire += 1
                if grid[i][j+1] == tree:
                    newgrid[i][j+1] = burning
                    no_trees -= 1
                    no_fire += 1
                if grid[i+1][j] == tree:
                    newgrid[i+1][j] = burning
                    no_trees -= 1
                    no_fire += 1
            ## Neuer Baum?
            elif grid[i][j] == empty:
                if uniform(0, 100) < a:
                    newgrid[i][j] = tree
                    no_trees += 1
            # Schlägt ein Blitz ein?
            if grid[i][j] == tree:
                if uniform(0, 100) < b:
                    newgrid[i][j] = burning
                    no_fire += 1
    grid[:] = newgrid[:]
    