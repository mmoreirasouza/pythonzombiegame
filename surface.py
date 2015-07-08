from tile import Tile


class Surface(object):  

    Tiles = []

    def __init__(self, surface_size, tile_size, level):

        if ((surface_size[0] % tile_size[0]) != 0) or ((surface_size[1] % tile_size[1]) != 0):
            raise Exception("Surface size and tile size dont match")

        number = 0

        for y in range(0, surface_size[1], tile_size[1]):

            for x in range(0, surface_size[0], tile_size[0]):

                number += 1

                if number in level.no_walk:
                    Surface.Tiles.append(Tile(x, y, tile_size[0], tile_size[1], number, (255, 0, 0), False))
                else:
                    Surface.Tiles.append(Tile(x, y, tile_size[0], tile_size[1], number, (0, 0, 255), True))

    @staticmethod
    def get_tile_by_position(position):

        for tile in Surface.Tiles:
            if tile.x == position[0] and tile.y == position[1]:
                return tile

        return None

    @staticmethod
    def get_tile_by_number(number):

        for tile in Surface.Tiles:
            if tile.number == number:
                return tile

        return None