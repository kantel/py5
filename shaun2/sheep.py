# PY5 IMPORTED MODE CODE
import settings as s

class Sheep:
    
    def __init__(self, x, y, im_l, im_r):
        self.x = x*s.patchsize
        self.y = y*s.patchsize
        self.im_l = im_l
        self.im_r = im_r
        choice = random(100)
        if choice <= 50:
            self.im = self.im_r
        else:
            self.im = self.im_l
    
    def update(self):
        pass
    
    def display(self):
        image(self.im, self.x, self.y)