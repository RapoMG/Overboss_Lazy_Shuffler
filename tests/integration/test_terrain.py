from unittest import TestCase
from terrain import Terrain


class TestTerrain(TestCase):
    def test_create_tile(self):
        ter = Terrain("Plain", '2 / 3 / 5')
        ter.create_tile(1, '2 + ')

        self.assertEqual(len(ter.tiles), 1, f'List should have 1 element, but instead has {len(ter.tiles)}.')
        self.assertEqual(ter.tiles[0].tile_id, 1, 'Tile id incorrect.')
        self.assertEqual(ter.tiles[0].value, '2 + ', 'Value incorrect.')

    def test_points(self):
        ter = Terrain("Plain", '2 / 3 / 5')
        ter.create_tile(1, '2 + ')

        self.assertEqual('2 + 2 / 3 / 5', ter.points(0), f"Points should be 2 + 2 / 3 / 5, but it's {ter.points(0)}.")
