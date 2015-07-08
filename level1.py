from level import Level
from enemy import Enemy
from random import randint
from life import Life
from end import End
from surface import Surface

class Level1(Level):

	BLOCK_TILES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
	20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 40, 48, 50, 51, 54, 55, 56, 60,
	61, 62, 63, 73, 75, 76, 79, 84, 85, 86, 87, 88, 92, 93, 94, 95, 96, 98, 100, 101,
	103, 104, 107, 109, 118, 119, 120, 123, 125, 126, 134, 135, 136, 137, 138, 139,
	140, 144, 145, 147, 150, 151, 152, 153, 155, 156, 157, 163, 164, 165, 170, 172,
	175, 176, 180, 181, 182, 188, 189, 190, 191, 192, 193, 195, 197, 200, 201, 203,
	205, 209, 214, 215, 216, 217, 218, 220, 223, 225, 226, 228, 233, 234, 235, 245,
	248, 250, 251, 253, 258, 259, 260, 262, 275, 276, 278, 280, 281, 282, 283, 284,
	285, 287, 288, 289, 290, 293, 296, 297, 298, 299, 300, 301, 312, 313, 314, 315,
	320, 325, 326, 327, 328, 329, 330, 331, 341, 345, 350, 351, 359, 360, 361, 362,
	366, 368, 370, 372, 373, 375, 376, 379, 380, 381, 384, 385, 386, 389, 391, 393,
	397, 398, 400, 401, 404, 414, 418, 419, 420, 421, 422, 425, 426, 429, 431, 432,
	433, 434, 435, 436, 438, 448, 450, 451, 461, 464, 466, 467, 468, 469, 475, 476,
	477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492,
	493, 494, 495, 496, 497, 498, 499, 500]



	ENEMY_SPOT = [460, 465, 49, 110, 80, 121, 28, 321, 252]

	LIFE_SPOT = [460, 222, 124, 179, 41]

	def __init__(self):

		super(Level1, self).__init__(Level1.BLOCK_TILES, 27, Level1.ENEMY_SPOT)

		self.end = None

		Enemy.Enemies = []

	def create_enemy(self, player):

		spot_count = len(Level1.ENEMY_SPOT)
		spot_number = randint(0, spot_count - 1)
		enemy_tile = Surface.get_tile_by_number(Level1.ENEMY_SPOT[spot_number])

		type_count = len(Enemy.Types)
		type_index = randint(0, type_count - 1)

		Enemy(enemy_tile.x, enemy_tile.y, player, Enemy.Types[type_index])

	def create_life(self):

		spot_count = len(Level1.LIFE_SPOT)
		spot_number = randint(0, spot_count - 1)
		life_tile = Surface.get_tile_by_number(Level1.LIFE_SPOT[spot_number])

		Life(life_tile.x, life_tile.y)

	def create_end(self):

		pass



