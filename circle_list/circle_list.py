# Circle Sine Wave
# nach Peter Farrell: »Math Adventures with Python« p110ff.

R1 = 100   # Radius großer Kreis
R2 = 5     # Radius kleine Kreise

t = 0      # Zeit-Variable
circle_list = []

def setup():
    size(600, 600)

def draw():
    global t, circle_list
    background(132, 144, 163)
    translate(width/4, height/2) # Linkes Viertel des Fensters
    no_fill()                    # Keine Farbe im großen Kreis
    stroke(0)                    # Outline: schwarz
    circle(0, 0, 2*R1)
    
    fill(250, 0, 0, 150)         # Füllfarbe des kleinen Kreises
    y = R1*sin(t)                # auf dem großen Kreis
    x = R1*cos(t)
    circle(x, y, 2*R2)
    
    # Addiere einen Punkt zur Liste, aber nicht mehr als 250
    circle_list = [y] + circle_list[:199]
    no_stroke()
    fill(0, 255, 0, 150)         # sattes grün – leichte Transparenz)
    # Schleife über die Liste, um den Trail zu zeichnen
    for i, c in enumerate(circle_list):
        circle(200 + i, c, R2)
    
    stroke(0, 250, 0)            # Grün für die Verbindungslinie …
    line(x, y, 200, y)
    fill(0, 250, 0, 150)         # und den kleinen Endpunkt
    stroke(0)
    circle(200, y, 2*R2)    
    
    t += 0.05