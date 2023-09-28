# Einfache Simulation eines Weltmodells
# nach Hartmut Bossel: Modellbildung und Simulation
# Braunschweig 2. Auflage 1994, Seiten 78ff.

WIN_WIDTH, WIN_HEIGHT = 740, 480

# Plot-Parameter
plot_x1 = 140                    # Start Fensterbreite rechts
plot_x2 = WIN_WIDTH - 40         # Ende Fensterbreite links
label_x = 10
plot_y1 = 60                     # Start Fensterhöhe oben
plot_y2 = WIN_HEIGHT - 80        # Ende Fensterhöhe unten
label_y = WIN_HEIGHT - 35
plot_title = "Dynamik eines nichtlinearen Mini-Weltmodells"

## Sonstige Parameter
final = 500    # Simulationszeitraum (Jahre)
dt = 0.2       # Schrittweite

## Funktionsabhängige Konstanten
x_min = 0                        # Startwert x
x_max = final                    # Maximalwert x
y_min = 0                        # Startwert f(x)
y_max = 16                       # Maximalwert f(x)
stepsize_x = x_max//10           # Ticks auf der x-Achse
stepsize_y = -2                  # Ticks auf der y-Achse


# Farben
bg_color = color(234, 218, 184)           # Packpapier
text_color = color(0, 150, 0)             # Grün
text_color_2 = color(20, 20, 20)          # Schwarz
plot_window_color = color(250, 250, 250)  # Weiß
grid_color = color(0, 250, 250)           # Blau-Grau
line_color_1 = color(250, 0, 0)           # Rot
line_color_2 = color(0, 0, 250)           # Blau
line_color_3 = color(235, 146, 52)        # Orange


# Paramteter des Weltmodells

## Bevölkerungsentwicklung
b = 0.03       # Geburtenrate
d = 0.01       # Sterberate

## Umweltbelastung
a = 0.1        # Abbaurate Umweltbelastung
e = 0.02       # Wichtungsfaktor Schadstoffeintrag

## Konsum
c = 0.05       # Wachstumsrate Konsum

## Eingriffsfaktoren -- Hier kann geändert werden ###################
u = 1.0        # Wirkung Umweltqualität auf Bevölkerungsentwicklung #
f = 0.03       # Kapazitätsfaktor Sättigung Konsum                  #
#####################################################################

volk_array = []
last_array = []
kons_array = []

def settings():
    size(WIN_WIDTH, WIN_HEIGHT)

def setup():
    global t, volk, last, kons
    window_title("Dynamik eines nichtlinearen Mini-Weltmodells")
    window_move(1300, 30)

    ## Anfangswerte
    t = 1.0
    volk = 1.0     # Bevölkerungsentwicklung
    last = 1.0     # Umweltbelastung
    kons = 1.0     # Konsum
    
def draw():
    background(bg_color)
    draw_plot_window()
    calc_world_model()
    
    if t >= final:
        print(volk, last, kons)
        x = x_min
        i = 0
        while i < len(volk_array):
            stroke(line_color_1)
            x_v = remap(x, x_min, x_max, plot_x1, plot_x2)
            y_v = remap(volk_array[i], y_min, y_max, plot_y2, plot_y1)
            circle(x_v, y_v, 2)
            stroke(line_color_2)
            x_v = remap(x, x_min, x_max, plot_x1, plot_x2)
            y_v = remap(last_array[i], y_min, y_max, plot_y2, plot_y1)
            circle(x_v, y_v, 2)
            stroke(line_color_3)
            x_v = remap(x, x_min, x_max, plot_x1, plot_x2)
            y_v = remap(kons_array[i], y_min, y_max, plot_y2, plot_y1)
            circle(x_v, y_v, 2)
            x += dt
            i += 1
                                
        stroke(text_color)                       
        print("I did it, Babe")
        no_loop()
    

def calc_world_model():
    global t, volk, last, kons
    qual = 1/last
    volk_rate = b*volk*u*qual*kons - d*volk*last
    if qual >= 1:
        abbau = a*last
    else:
        abbau = a*last*qual
    last_rate = e*kons*volk - abbau
    kons_rate = c*kons*last*(1 - (kons*last*f))
    # Numerische Lösung nach Euler
    volk = volk + volk_rate*dt
    last = last + last_rate*dt
    kons = kons + kons_rate*dt
    volk_array.append(volk)
    last_array.append(last)
    kons_array.append(kons)
    t += dt
 
def draw_plot_window():
    # Den Plot in einem weißen Kasten zeichnen
    fill(plot_window_color)
    rect_mode(CORNERS)
    no_stroke()
    rect(plot_x1, plot_y1, plot_x2, plot_y2)
    # Kasten für y-Label
    stroke(grid_color)
    stroke_weight(1)
    rect(label_x - 5, (plot_y1 + plot_y2)//2 - 25, label_x + 100, (plot_y1 + plot_y2)//2 + 30)
    no_stroke()
    # Kasten für x-Label
    stroke(grid_color)
    stroke_weight(1)
    rect(plot_x1, label_y - 15, plot_x1 + 450, label_y + 15)
    no_stroke()
    # Titel des Plots zeichnen
    fill(text_color)
    text_size(20)
    text_align(LEFT)
    text(plot_title, plot_x1, plot_y1 - 10)
    draw_grid()
    draw_axis_labels()
    
def draw_grid():
    # Zeichne Gitter und Label
    text_size(10)
    text_align(CENTER, TOP)
    # x_Achse
    for i in range(x_min, x_max + 1, stepsize_x):
        x = remap(i, x_min, x_max, plot_x1, plot_x2)
        fill(text_color)
        text(str(i), x, plot_y2 + 10)
        stroke_weight(1)
        stroke(grid_color)
        line(x, plot_y1, x, plot_y2)
    # y-Achse
    for j in range(y_max, y_min - 1, stepsize_y):
        y = remap(j, y_max, y_min, plot_y1, plot_y2)
        if j == y_min:
            text_align(RIGHT, BOTTOM)   # Unten
        elif j == y_max:
            text_align(RIGHT, TOP)      # Open
        else:
            text_align(RIGHT, CENTER)   # Vertikal zentrieren
        fill(text_color)
        text(str(j), plot_x1 - 10, y)
        stroke_weight(1)
        stroke(grid_color)
        line(plot_x1, y, plot_x2, y)
        
def draw_axis_labels():
    text_size(13)
    text_leading(15)
    # y-Achse
    text_align(LEFT, CENTER)
    fill(line_color_1)
    text("Bevölkerung", label_x, (plot_y1 + plot_y2)//2 - 20)
    fill(line_color_2)
    text("Umweltbelastung", label_x, (plot_y1 + plot_y2)//2)
    fill(line_color_3)
    text("Konsum", label_x, (plot_y1 + plot_y2)//2 + 20)
    # x-Achse
    fill(text_color_2)
    text_size(13)
    text("Eingriffsparameter: Umwelt-Qualität: " + str(u) + ", Konsum-Faktor: " + str(f), plot_x1 + 5, label_y)
    fill(text_color)