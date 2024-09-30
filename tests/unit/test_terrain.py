from unittest import TestCase
from terrain import Terrain


class TestTerrain(TestCase):
    def test_create_terrain(self):
        ter = Terrain("Plain", '2 / 3 / 5')
        t = ter.create_tile(1, '2 + ')

        self.assertEqual('Plain', ter.name, f'Terrain name should be Plain, but it is {ter.name} instead.')
        self.assertEqual('2 / 3 / 5', ter.terr_points,
                         f'Terrain points should be "2 / 3 / 5", but it is "{ter.terr_points}" instead.')
        self.assertListEqual([], ter.tiles, f'Terrain list sholud be empty [], but it is {ter.tiles}')
