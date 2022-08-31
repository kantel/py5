# Rotating Triangles Final
# nach Roger Antonsen (University of Oslo)
# und Peter Farrell (Math Adventures with Python, p. 93ff.)

t = 0

def setup():
    size(600, 600)
    window_title("Rotierende Dreiecke")

def draw():
    global t
    background(30, 30, 30)  # Dark Gray
    stroke_weight(3)
    translate(width/2, height/2)
    color_mode(HSB, 100)
    for i in range(90):
        rotate(radians(360/90))
        with push_matrix():
            translate(200, 0)
            stroke(i%360, 100, 80)
            rotate(radians(t + 2*i*360/90))
            tri(100)
    t += 0.5
    color_mode(RGB, 255)

def tri(length):
    """Zeichnet ein gleichseitiges Dreieck
       rund um den Mittelpunkt des Dreiecks."""
    no_fill()
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)