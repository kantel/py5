import py5

def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)
    
def draw():
    py5.fill(py5.color(py5.random_int(5, 250), py5.random_int(5, 250), py5.random_int(5, 250)))
    py5.square(py5.mouse_x, py5.mouse_y, 20)

py5.run_sketch()