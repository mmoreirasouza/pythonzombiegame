import math
from surface import Surface

class AStar(object):

	@staticmethod
	def get_path(enemy):

		for tile in Surface.Tiles:
			tile.parent = None
			tile.g = 0
			tile.h = 0
			tile.f = 0

		open_list = []
		close_list = []
		neighbors = []
		path = []


		enemy_tile = Surface.get_tile_by_position((enemy.x, enemy.y))
		player_tile = Surface.get_tile_by_position((enemy.player.x, enemy.player.y))

		open_list.append(enemy_tile)

		def check_neighbor(tile):

			if tile != None and tile.walk == True:
				return True
			else:
				return False

		def update_neighbors_list(tile):

			neighbors = []

			neighbor_left = Surface.get_tile_by_position((tile.x - tile.width, tile.y))
			neighbor_right = Surface.get_tile_by_position((tile.x + tile.width, tile.y))
			neighbor_top = Surface.get_tile_by_position((tile.x, tile.y - tile.height))
			neighbor_botton = Surface.get_tile_by_position((tile.x, tile.y + tile.height))

			if check_neighbor(neighbor_left):
				neighbors.append(neighbor_left)

			if check_neighbor(neighbor_right):
				neighbors.append(neighbor_right)

			if check_neighbor(neighbor_top):
				neighbors.append(neighbor_top)

			if check_neighbor(neighbor_botton):
				neighbors.append(neighbor_botton)

			return neighbors

		while open_list:

			tile_min_f = min(open_list, key = lambda p : p.g + p.h)

			open_list.remove(tile_min_f)
			close_list.append(tile_min_f)

			if tile_min_f == player_tile:

				while tile_min_f.parent != None:

					path.append(tile_min_f)
					tile_min_f = tile_min_f.parent

				return path
				

			neighbors = update_neighbors_list(tile_min_f)

			for neighbor in neighbors:

				if neighbor in close_list:
					continue

				else:

					if neighbor in open_list:

						new_g = tile_min_f.g + 10

						if new_g < neighbor.g:

							neighbor.g = new_g
							neighbor.parent = tile_min_f						

					else:

						neighbor.g = tile_min_f.g + 10
						neighbor.h = math.sqrt((player_tile.x - neighbor.x)**2 + (player_tile.y - neighbor.y)**2)
						neighbor.f = neighbor.g + neighbor.h
						neighbor.parent = tile_min_f
						open_list.append(neighbor)

		return path

