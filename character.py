from rect import Rect


class Character(Rect):

    def __init__(self, x, y, width, height, health):

        self.health = health
        self.direction = "E"
        self.images = {}
        self.velocity_x = 0
        self.velocity_y = 0
        self.next_step_x = None
        self.next_step_y = None

        super(Character, self).__init__(x, y, width, height)


    def draw(self, screen):
        raise Exception("Not implemented")

