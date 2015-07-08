class Rect(object):

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height =  height
        self._x_center = x + (width / 2)
        self._y_center = y + (height / 2)

    @property
    def x_center(self):
        return int(self.x +(self.width / 2))

    @property
    def y_center(self):
        return int(self.y +(self.height / 2))

    def check_collision(self, other_rect):

        if self.x + self.width in range(other_rect.x, other_rect.x + other_rect.width) and self.y + self.height in range(other_rect.y, other_rect.y + other_rect.height) or \
           self.x in range(other_rect.x, other_rect.x + other_rect.width) and self.y in range(other_rect.y, other_rect.y + other_rect.height):
            return True

        return False