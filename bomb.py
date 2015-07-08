from rect import Rect


class Bomb(Rect):

	Bombs = []

	def __init__(self, x, y):

		self.total_frames = 0

		super(Bomb, self).__init__(x, y, 32, 32)

		Bomb.Bombs.append(self)