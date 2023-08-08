# Ein einfaches Partikelsystem in Py5
# Nach Daniel Shiffman: The Nature of Code (2012), p. 143pp
# Python-Port: Jörg Kantel, 2023
from particles import Particle, RectParticle

WIDTH, HEIGHT = 500, 500
START_X, START_Y = 250, 70

particles = []

def setup():
    size(WIDTH, HEIGHT)
    window_move(1400, 30)
    window_title("Partikelsystem 1")
    
def draw():
    background(49, 197, 244)   # Hellblau
    change = random(10)
    if change <= 5:
        particles.append(Particle(START_X, START_Y))
    else:
        particles.append(RectParticle(START_X, START_Y))
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].is_not_alive():
            particles.pop(i)
        