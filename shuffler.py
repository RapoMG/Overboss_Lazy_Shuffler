from random import randint
from components import MainColection


def drawing():  # def or class
    """Drawing terrain type that will be used in play.
       :return: List of Terrain objects"""
    # get category (list of terrain type)
    col = MainColection().categories.copy()
    drawed = []

    for i in range(5):
        draw = randint(1, len(col)-1)  # Picks one of terrain (exclude dungeon)
        drawed.append(col.pop(draw))

    drawed.insert(0, col[0])  # Add Dungeon
    return drawed


def show_drawed(terr_list):  # list of terrain
    """Creating string listing terraint types that will be in play.
    :param terr_list: *list* of terrain objects.
    :return: formated *str* of terrain name and points gained"""
    # p = drawing()
    a = '\n'
    for i in range(len(terr_list)):
        a += f'{i+1}.{terr_list[i].name}: {terr_list[i].terr_points}'
        if i < len(terr_list):
            a += ',\n'

    return a


def univ_show_drawed(terr_list):  # list of terrain
    # Probably it should be part of interface
    """**RENAME IT!**\n
    Creating question listing terraint types that will be in play.
    :param terr_list: *list* of terrain objects.
    :return: list with 'empty' order *str* and *dict* of terrain name and points gained
     as {printed in position: name + points} —
     [' ', {keys: values}]"""
    # prepare column with points
    max_name = 0
    for i in range(len(terr_list)):
        if len(terr_list[i].name) > max_name:  # is it max lenght?
            max_name = len(terr_list[i].name)

    d = {}
    for i in range(len(terr_list)):
        tab = max_name - len(terr_list[i].name) + 1
        d.update({i + 1: f'{terr_list[i].name}{":": <{tab}} {terr_list[i].terr_points}'})

    # s = ''
    # a = [s, d]

    # simpler
    a = ['', d]  # [fake question, dict of lines "name -  points"]

    return a


def create_pile():
    pile = []  # list for pile of Tiles
    counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # count = 0

    # pick terrain (random)
    while len(pile) < 68:  # sum of tiles > 0 ? / len(pile)=< 68 (all tiles)
        ter = randint(0, 5)  # number of terrain in list
        # add counter for each Terrain to reduce repetitions?
        if counter[ter] >= 12:
            # count += 1
            continue

        if ter == 0:  # if it's Dungeon
            tile = randint(0, 7)  # 8 tiles
        else:
            tile = randint(0, 11)  # standard 12
        try:
            pile.index((ter, tile))
        except ValueError:
            pile.append((ter, tile))
            counter[ter] = counter[ter]+1

    return pile


def create_pile_2():  # concept 2: around 3 times fewer iterations
    pile = []  # list for drawed tiles
    tiles = {0: [0, 1, 2, 3, 4, 5, 6, 7],
             1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             4: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}

    while len(pile) < 68:
        # draw terrain (dictionary key)
        ter = randint(0, 5)
        if len(tiles[ter]) == 0:
            continue
        # draw tile of that terrain (dictionary value)
        tile = randint(0, len(tiles[ter])-1)
        # remainning tiles in thet terrain pool
        left_tiles = tiles[ter]
        # save drawed tile
        pile.append(
            (ter, left_tiles[tile])
        )

        # remove tile from drawing pool
        left_tiles.pop(tile)

    return pile
