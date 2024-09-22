# python 3.12
"""known issues:
 - def univ_show_drawed(terr_list): must be renamed because of reasons
 """
import components
import shuffler as shu
import interface as inter
import os
# add terminal size command
IPT = '\t'  # input distance


def clean():  # Clean screen
    """Removes all characters from terminal window."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')


def menu():
    while True:
        clean()
        inter.logo()

        # Print main menu question
        inter.question_menu(inter.main_menu)
        opt = input(IPT)
        opt = opt.lower()

        if opt == '1':  # Draw terrains

            # Draw terrain
            draw = shu.drawing()
            # Show what was drawed
            clean()
            inter.logo()

            inter.question_menu(shu.univ_show_drawed(draw))

            # Ask to play with it
            inter.question_menu(inter.accept_terrnain)
            aff = input(IPT)
            if aff.lower() == 'y':
                # Here: start play
                """ Check function play() --> send draw?"""
                play(draw)
            else:
                continue

        elif opt == '2':  # chose terrain

            # Choose terrain
            choose = components.MainColection().categories.copy()
            choose.pop(0)  # remove Dungeon

            draw = []

            while len(draw) < 5:
                clean()
                inter.logo()
                inter.question_menu(shu.univ_show_drawed(choose))
                inter.question_menu(shu.univ_show_drawed(draw))
                aff = input(IPT)
                draw.append(choose.pop(int(aff)-1))  # insert position in list

            # Ask to play with it (second time. create function?)
            clean()
            inter.logo()
            inter.question_menu(shu.univ_show_drawed(draw))
            inter.question_menu(inter.accept_terrnain)
            aff = input(IPT)
            if aff.lower() == 'y':
                # Start play
                play(draw)
            else:
                continue

        elif opt == '3':  # bassic terrain

            # Basic terrain
            draw = []
            for i in range(1, 6):  # skip Dungeon
                draw.append(components.MainColection().categories[i])

            clean()
            inter.logo()
            inter.question_menu(shu.univ_show_drawed(draw))

            # Ask to play with it
            inter.question_menu(inter.accept_terrnain)

            aff = input(IPT)
            if aff.lower() == 'y':
                # Start play
                play(draw)
            else:
                continue
        elif opt == 'q' or opt == 'e':
            break
        else:
            continue


def play(terrain_in_play):  # add chosen terrains? (draw variable)
    # call create pile
    pile = shu.create_pile_2()
    end = False  # end game
    game_round = 1  # hmmm...

    # create dict with 4 "fields"
    market = {1: None, 2: None, 3: None, 4: None}
    # if field none - ad first value from pile
    while True:
        for place in market:  # maybe rebuild with /for place, tile in market.items()/ ?
            tile = market.get(place)
            if tile is None:
                if len(pile) == 0:  # after last tile used
                    continue
                market.update({place: pile.pop(0)})

        while True:
            # prepare args for show_markte()
            # terrain_in_play === (Terrain, tile in class list)
            names = []  # list of terrain names for tiles in market
            points = []  # list of points for tiles in market
            for mrkt_order, tile in market.items():
                if tile is None:
                    names.insert(mrkt_order, ' ')
                    points.insert(mrkt_order, ' ')
                else:
                    terr_class = tile[0]
                    tile_nmbr = tile[1]
                    names.insert(mrkt_order, terrain_in_play[terr_class].name)
                    points.insert(mrkt_order, terrain_in_play[terr_class].points(tile_nmbr))

            # print tiles
            clean()
            inter.logo()
            inter.show_market(names, points)

            # market menu
            inter.question_menu(inter.market_options)

            move = int(input(IPT))

            if move == 1:  # 1. take tile (remove)
                # Chose tile from market
                inter.question_menu(inter.chose_tile)
                take = int(input(IPT))
                market.get(take)  # get() method returns none if there's no key
                market.update({take: None})
            elif move == 2:  # Unnecessery at this point, placeholder for skils
                pass  # 2. destroy/ replace tile
            elif move == 3:  # 3. next round
                game_round += 1  # Hmmm...
                break
            elif move == 0:  # exit game
                end = True
                break
            else:
                continue

        if end:
            break


# Run app
menu()
