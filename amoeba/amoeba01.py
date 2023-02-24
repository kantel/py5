from random import randint, uniform

WIDTH, HEIGHT = 600, 400
MIN_DIA = 50
MIN_DIA2 = MIN_DIA//2
MAX_DIA = 150
MAX_DIA2  = MAX_DIA//2

class Amoeba():
  
  def __init__(self, _x, _y, _diameter):
    self.x = _x
    self.y = _y
    self.d = _diameter
    self.nucleus = {
      "fill": ["#FF0000", "#FF9900", "#FF00FF",
               "#00FF00", "#0099FF"][int(randint(0, 4))],
      "x": self.d*uniform(-0.15, 0.15),
      "y": self.d*uniform(-0.15, 0.15),
      "d": self.d/uniform(2.5, 4)
    }
  
  def circle_point(self, t, r):
    x = cos(t)*r
    y = sin(t)*r
    return([x, y])
    
  def display(self):
    # Cell Nucleus
    fill(self.nucleus["fill"])
    no_stroke()
    ellipse(self.x + self.nucleus["x"], self.y + self.nucleus["y"],
            self.nucleus["d"], self.nucleus["d"])
    # Cell Membrane
    fill(0x880099AA)
    stroke("#FFFFFF")
    stroke_weight(3)
    r = self.d/2.0
    # print("r = ", r/8)
    cpl = r*.55
    cpx, cpy = self.circle_point(frame_count*.5, r/4)
    xp, xm = self.x + cpx, self.x - cpx
    yp, ym = self.y + cpy, self.y - cpy
    begin_shape()
    vertex(self.x, self.y - r)   # top vertex
    bezier_vertex(xp + cpl, yp - r, xm + r, ym - cpl,
                 self.x + r, self.y)   # right vertex
    bezier_vertex(xp + r, yp + cpl, xm + cpl, ym + r,
                 self.x, self.y + r)   # bottom vertex
    bezier_vertex(xp - cpl, yp + r, xm - r, ym + cpl,
                 self.x - r, self.y)   # left vertex
    bezier_vertex(xp - r, yp - cpl, xm - cpl, ym - r,
                 self.x, self.y - r)   # top vertex
    end_shape()

amoebas = []

def setup():
  size(WIDTH, HEIGHT)
  for _ in range(8):
    amoeba = Amoeba(randint(MAX_DIA2, width - MAX_DIA2),
                    randint(MAX_DIA2, height - MAX_DIA2),
                    randint(MIN_DIA, MAX_DIA))
    amoebas.append(amoeba)
  
def draw():
  background("#004477")
  for amoeba in amoebas:
    amoeba.display()

