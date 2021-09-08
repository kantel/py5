# rotating triangles final
# after Roger Antonsen (University of Oslo)
# and Peter Farrell (Math Adventures with Python, p. 93ff.)

def setup():
    size(600, 600)
    color_mode(HSB, 100)

t = 0

def draw():
    global t
    background(255, 0, 100)  # white
    translate(width/2, height/2)
    for i in range(90):
        rotate(radians(360/90))
        push_matrix()
        translate(200, 0)
        stroke(i%360, 100, 80)
        rotate(radians(t + 2*i*360/90))
        tri(100)
        pop_matrix()
    t += 0.5

def tri(length):
    """Zeichnet ein gleichseitiges Dreieck
       rund um den Mittelpunkt des Dreiecks."""
    no_fill()
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)