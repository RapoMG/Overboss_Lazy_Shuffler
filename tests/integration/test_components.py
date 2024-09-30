from unittest import TestCase
from components import MainColection


class TestMainCilection(TestCase):
    def test_creation(self):
        elem = MainColection()

        # number of terrains
        self.assertEqual(len(elem.categories), 11)

        # number of tiles
        for terr in elem.categories:
            if terr.name == 'Dungeon':
                self.assertEqual(len(terr.tiles), 8)
            else:
                self.assertEqual(len(terr.tiles), 12)

        # test special values of tiles
        for terr in elem.categories:
            tile_values = []
            for tile in terr.tiles:
                tile_values.append(tile.value)
            if terr.name == 'Graveyard':
                self.assertEqual(tile_values.count('1'), 5, f"Terrain {terr.name} should have 5 tiles of value '1'.")
                self.assertEqual(tile_values.count('2'), 4, f"Terrain {terr.name} should have 4 tiles of value '2'.")
                self.assertEqual(tile_values.count('3'), 3, f"Terrain {terr.name} should have 3 tiles of value '3'.")
            elif terr.name == 'Camp':
                self.assertEqual(tile_values.count('(Black)'), 2,
                                 f"Terrain {terr.name} should have 2 tiles of value '(Black)'.")
                self.assertEqual(tile_values.count('(Blue)'), 2,
                                 f"Terrain {terr.name} should have 2 tiles of value '(Blue)'.")
                self.assertEqual(tile_values.count('(Orange)'), 2,
                                 f"Terrain {terr.name} should have 2 tiles of value '(Orange)'.")
                self.assertEqual(tile_values.count('(Red)'), 2,
                                 f"Terrain {terr.name} should have 2 tiles of value '(Red)'.")
                self.assertEqual(tile_values.count('(Yellow)'), 2,
                                 f"Terrain {terr.name} should have 2 tiles of value '(Yellow)'.")
            elif terr.name == 'Dungeon':
                self.assertEqual(tile_values.count(''), 8, f"Terrain {terr.name} should have 8 tiles of value ''.")
            else:
                self.assertEqual(tile_values.count(''), 12, f"Terrain {terr.name} should have 12 tiles of value ''.")
