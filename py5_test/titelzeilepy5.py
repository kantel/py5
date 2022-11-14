# Titelzeile in py5

def setup():
    global artist
    size(400, 200)
    window_title("👩‍🎨 Hallo Py5 👩‍🎨")
    artist = load_image("artist.png")
    no_loop()
    
    
def draw():
    background(color(230, 226, 204))  # Packpapier
    image(artist, 220, 20)
    print("I did it, Babe!")