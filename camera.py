from pygame import *

scrWidth = 1024
scrHeight = 768

class Camera():
    def __init__(self, camera_function, camera_width, camera_heigh):
        self.camera_function = camera_function
        self.state = Rect(0, 0, camera_width, camera_heigh)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_function(self.state, target.rect)


