# Response.py
# Nach einem Processing.py-Sketch von
# Allison Parrish, Ben Fry und Casey Reas
# »Getting Started with Processing.py«, San Francisco 2016, p70f

WIDTH = 360       # 360
HEIGHT = 480      # 480 / 315
x = 60            # 60
y = 440           # 440 / 300
radius = 45
body_height = 160 # 160 / 120
neck_height = 70  # 70 / 20
easing = 0.02

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Hallo HAL 9000! 🤖")
    ellipse_mode(RADIUS)

def draw():
    global x, neck_height, body_height
    target_x = mouse_x
    x += (target_x - x)*easing
    
    if is_mouse_pressed:
        neck_height = 16
        body_height = 90
    else:
        neck_height = 70
        body_height = 160
    
    ny = y - body_height - neck_height - radius
    background(0, 153, 204)
        
    # Neck
    stroke(255)
    line(x + 12, y - body_height, x + 12, ny)
    
    # Antennae
    line(x + 12, ny, x - 18, ny - 43)
    line(x + 12, ny, x + 42, ny - 99)
    line(x + 12, ny, x + 78, ny + 15)
    
    # Body
    no_stroke()
    fill(255, 204, 0)   # orange
    circle(x, y - 33, 33)
    fill(0)             # black
    rect(x - 45, y - body_height, 90, body_height - 33)
    
    # Head
    fill(0)             # black
    circle(x + 12, ny, radius)
    fill(255)           # white
    circle(x + 24, ny - 6, 14)
    fill(0, 0, 204)     # blue
    circle(x + 24, ny - 6, 3)