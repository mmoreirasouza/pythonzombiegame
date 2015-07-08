from rect import Rect

class Life(Rect):

	Lifes = []


	def __init__(self, x, y):

		self.health = 200
		self.total_frames = 0

		super(Life, self).__init__(x, y, 32, 32)

		Life.Lifes.append(self)