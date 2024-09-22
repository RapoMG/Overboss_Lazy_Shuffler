from terrain import Terrain


class MainColection:  # def?
    """Creation of Terrain types and it's tile sets"""

    # Terrain creation
    categories = [
        Terrain('Dungeon', '1+ ≠1🡘'),
        Terrain('Forest', '1/3/6/10/15'),
        Terrain('Cave', '1+2'),
        Terrain('Graveyard', ' +{5}/(2)'),
        Terrain('Swamp', '1+1+1'),
        Terrain('Camp', ' 1/4/9/16'),
        Terrain('Castle', '2+2'),
        Terrain('Cloud Island', '7 -≠1'),
        Terrain('Desert', '0/2/6/12/20'),
        Terrain('Summoning Circle', '1'),
        Terrain('Vulcano', '4')
    ]

    # Tiles creation
    for cat in categories:
        if cat.name == 'Dungeon':  # dungeon has 8 tiles
            for i in range(8):
                cat.create_tile(i + 1)
        elif cat.name == 'Graveyard':  # Graveyard has valuea for each tile
            p = ('1', '1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3')  # vallue of each tile
            for i in range(12):
                cat.create_tile(i+1, str(p[i]))
        elif cat.name == 'Camp':  # Camp has colored flag for each tile
            p = ('(Black)', '(Black)', '(Blue)', '(Blue)', '(Orange)', '(Orange)', '(Purple)', '(Purple)',
                 '(Red)', '(Red)', '(Yellow)', '(Yellow)')  # color of each tile
            for i in range(12):
                cat.create_tile(i+1, str(p[i]))
        else:
            for i in range(12):
                cat.create_tile(i+1)
