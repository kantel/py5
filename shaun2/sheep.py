# PY5 IMPORTED MODE CODE
import py5
import settings as s

py5.image_mode(py5.CORNER)

class Sheep:
    
    def __init__(self, x, y, im_l, im_r):
        self.x = x*s.patch_size
        self.y = y*s.patch_size
        self.im_l = im_l
        self.im_r = im_r
        choice = py5.random(100)
        if choice <= 50:
            self.im = self.im_r
        else:
            self.im = self.im_l
    
    def update(self):
        pass
    
    def display(self):
        py5.image(self.im, self.x, self.y)