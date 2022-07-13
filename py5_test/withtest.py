def setup():
    size(400, 400)
    window_move(1400, 30)
    window_title("With with")
    background(233, 195, 91)
    no_loop()


def draw():
    fill(color(25, 149, 156))
    circle(100, 100, 50)

    with push_style():
        fill(color(211, 132, 65))
        stroke_weight(5)
        circle(200, 200, 50)
    circle(300, 300, 50)
    
    print("I did it, Babe!")