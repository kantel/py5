import py5

WIDTH, HEIGHT = 640, 480

palette = [py5.color(189,183,110), py5.color(0,100,0), py5.color(34,139,105),
           py5.color(152,251,152), py5.color(85,107,47), py5.color(139,69,19),
           py5.color(154,205,50), py5.color(107,142,35), py5.color(139,134,78),
           py5.color(139, 115, 85)]

xmax = 600
xmitte = 300
ymax = 440
level = 12
w1 = 0.36   # Winkel 1
w2 = 0.48   # Winkel 2

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.window_title("Asymmetrischer Pythagorasbaum")
    py5.background(234, 218, 184)
    py5.stroke_weight(1)
    py5.no_loop()

def draw_pythagoras(a1, a2, b1, b2, level):
    if (level > 0):
        # Eckpunkte berechnen
        n1 = -b2 + a2
        n2 = -a1 + b1
        c1 = b1 + n1
        c2 = b2 + n2
        d1 = a1 + n1
        d2 = a2 + n2
        # Start-Rechteck zeichnen
        py5.fill(palette[(level-1)%10])
        with py5.begin_closed_shape():
            py5.vertex(a1 + xmitte, ymax - a2)
            py5.vertex(b1 + xmitte, ymax - b2)
            py5.vertex(c1 + xmitte, ymax - c2)
            py5.vertex(d1 + xmitte, ymax - d2)
        e1 = d1 + w1*(c1 - d1) + w2*n1
        e2 = d2 + w1*(c2 - d2) + w2*n2
        # Schenkel-Quadrate zeichnen
        draw_pythagoras(e1, e2, c1, c2, level-1)
        draw_pythagoras(d1, d2, e1, e2, level-1)

def draw():
    draw_pythagoras(-(xmax/10), 0, xmax/20, 0, level)
    print("I did it, Babe!")

py5.run_sketch()