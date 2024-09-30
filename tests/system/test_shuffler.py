import shuffler as shu
from unittest import TestCase


class TestShuffler(TestCase):
    def test_drawing(self):
        draw = shu.drawing()
        # test if drawed have 6 elements (dungeon included
        self.assertEqual(len(draw), 6, f'List should have 6 elaements, but it has only {len(draw)}')
        # Test if all are different?
        for i in draw:
            self.assertEqual(draw.count(i), 1, f'Element {i} should be unique, but it appears {draw.count(i)} times.')

    def test_show_drawed(self):
        draw = shu.univ_show_drawed(shu.drawing())
        # Is first element string ''
        self.assertEqual(draw[0], '', f"First element should have value '', but it is '{draw[0]}' instead.")
        # is secound element dict
        self.assertEqual(type(draw[1]), dict, f'Secound element should be dictionary, but it is {type(draw[1])}.')
        # test string correct value in dictionary?
        # ????????????????????????????????????????????????????????????????????????????????????????????
        # Rewrite everything to string they should show? As in here? String won't have method .name.
        # Should I create class instance? Terrain('Dungeons', ' 1+1')?
        self.assertEqual(f'Dungeon{":": <{len(draw[1][1])-14}} 1+ ≠1🡘', draw[1].get(1))

    def test_create_ppile(self):
        # is pile lenght is 68
        pile = shu.create_pile_2()
        self.assertEqual(len(pile), 68, f" there are  {len(pile)} elements.")
        # Test if any element is reapeted
        for pair in pile:
            self.assertEqual(pile.count(pair), 1, f"Element {pair} is {pile.count(pair)} times in list")
