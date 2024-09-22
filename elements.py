class Tile:
    def __init__(self, tile_id, value=""):
        self.tile_id = tile_id  # counting number 1-12
        self.value = value  # individual value of tile
        # self.type

    def image(self):
        """Empty method placeholder for image data in future"""
        pass

    def __repr__(self):
        return f"Tile number {self.tile_id}, points {self.value}"


class Token:
    pass
    # Type
    # image
    # used/ unused ?
