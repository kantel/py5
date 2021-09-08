def setup():
    size(600, 600)

t = 0

def draw():
    global t
    translate(width/2, height/2)
    rotate(radians(t))
    tri(200)
    t += 0.5

def tri(length):
    """Zeichnet ein gleichseitiges Dreieck
       rund um den Mittelpunkt des Dreiecks."""
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)