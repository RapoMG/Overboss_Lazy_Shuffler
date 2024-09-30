from elements import Tile


class Terrain:
    """Terrain tile type\n
        **name** - str name of terrain\n
        **terr_points** - string of value of gained points"""
    def __init__(self, name, terr_points=""):
        self.name = name  # Terrain name
        self.terr_points = terr_points
        self.tiles = []  # list of tiles

    def create_tile(self, tile_id, value=""):
        """**tile_id** suposed stand for individual number of tile.\n
        **value** represents aditional points for that specific tile, if there is one. For now, it is string.
         """
        self.tiles.append(Tile(tile_id, value))

    def points(self, position):
        """Total points from tile in that terrain
        :arg position: *int* of value 0-11 for element in tiles *list*"""
        return f'{self.tiles[position].value}{self.terr_points}'
