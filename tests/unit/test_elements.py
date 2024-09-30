from unittest import TestCase
from elements import Tile


class TestTile(TestCase):
    def test_create_tile(self):
        # Test with default value
        t = Tile(1,)

        self.assertEqual(1, t.tile_id, f'Tile_id should be set to 1, insead it is {t.tile_id}.')
        self.assertEqual("", t.value, f"Value should be set to '', insead it is '{t.value}'.")

        # Test with set value
        t2 = Tile(2, '3 +')

        self.assertEqual('3 +', t2.value, f"Value should be set to '3 +', insead it is '{t2.value}'.")

    def test_repr(self):
        t = Tile(3, "2 +")

        self.assertEqual(t.__repr__(), "Tile number 3, points 2 +")
