from rect import Rect

class Tile(Rect):



    def __init__(self, x, y, width, height, number = 0, color = (0, 0, 0), walk = True):

        self.number = number
        self.color = color
        self.walk = walk
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
        

        super(Tile, self).__init__(x, y, width, height)