from rect import Rect

class Key(Rect):

	Keys = []

	def __init__(self, x, y):

		super(Key, self).__init__(x, y, 32, 32)

		Key.Keys.append(self)