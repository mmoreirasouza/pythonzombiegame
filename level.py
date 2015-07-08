class Level(object):

	Borders = []

	def __init__(self, no_walk, player_position, enemy_positions):

		for index in range(1, 26):
			Level.Borders.append(index)

		for index in range(50, 501, 25):
			Level.Borders.append(index)

		for index in range(26, 477, 25):
			Level.Borders.append(index)

		for index in range(477, 500):
			Level.Borders.append(index)			


		self.no_walk = []
		self.no_walk.extend(Level.Borders)
		self.no_walk.extend(no_walk)

		self.player_position = player_position
		self.enemy_positions = enemy_positions

	def create_enemy(self, player):

		raise Exception("Not implemented")