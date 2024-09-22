# Questions
accept_terrnain = 'Do you want play with this terrains?', {'Y': 'Yes', 'N': 'No'}
main_menu = ('Chose your action:',
             {1: 'Draw terrains',  # (A) Answer = 1
              2: 'Select terrains yourself',  # (B) Answer = 2
              3: 'Basic terrains',  # (C) Answer = 3
              'e/q': 'Exit Shuffler'  # (Exit) Answer = q/e
              })
market_options = ('Chose your action:',
                  {1: 'Take tile',  # (A) Answer = 1
                   2: "Destroy tile (IT'S PLACEHOLDER)",  # (B) Answer = 2
                   3: 'Next round',  # (C) Answer = 3
                   0: 'Exit Shuffler'  # (Exit) Answer = 0
                   })
chose_tile = ("Chose tile 1-4 (counting from left):", {})  # is empty dict ok here?


def logo():
    # terminal size 120?
    width = 80
    nl = '\n'  # new line; formating purpouses

    # title size:59 (only 'text')
    l1 = ' █████  ██   ██ █████  █████  █████    █████  ██████ ██████'
    l2 = '██   ██ ██   ██ ██     ██  ██ ██   ██ ██   ██ ██     ██    '
    l3 = '██   ██ ██   ██ █████  ████   █████   ██   ██ ██████ ██████'
    l4 = '██   ██  ██ ██  ██     ██ ██  ██   ██ ██   ██     ██     ██'
    l5 = ' █████    ███   █████  ██  ██ ██████   █████  ██████ ██████'
    title = f'{l1: ^{width}}\n'\
        f'{l2: ^{width}}\n'\
        f'{l3: ^{width}}\n'\
        f'{l4: ^{width}}\n'\
        f'{l5: ^{width}}'
    # subtitle size:24
    subtittle = 'A Boss Monster Adventure'
    # name size:13
    name = 'Lazy Shuffler'

    full = f'\n{title}\n' \
        f'{subtittle: ^{width}}\n' \
        f'{name: ^{width}}' \
        f'{nl * 2}'

    print(full)


def main_menu_q():  # (order, options): for universal purposes
    """**OBSOLETE**"""
    tab = 11  # base distance from window border

    order = 'Chose your action:'
    options = {
        1: 'Draw terrains',  # (A) Answer = 1
        2: 'Select terrains yourself',  # (B) Answer = 2
        3: 'Basic terrains',  # (C) Answer = 3
        'e/q': 'Exit Shuffler'  # (Exit) Answer = q/e
    }

    final_tab = tab + len(order)-5  # distance based on element

    full = f'{order: >{final_tab}}\n\n'  # First line of user menu

    for number, option in options.items():  # Create menu lines
        final_tab = tab - len(str(number))
        if type(number) == str:  # empty line for additional options
            full += '\n'
        full += f'{"[": >{final_tab}}{number}]. {option} \n'

    print(full)


def show_market(names, points):
    """***WORK IN PROGRES***\n
    Print name, "picture" and poins of tiles in market.
    :param names: 4 element *list* containing *strings* with terrain names.
    :param points: 4 element *list* containing *strings* with points for tile
    :return: *print* arranged lines (9) with: names (1), graphical representation of tiles (7) and their poinst (1).
           """

    sp = 20  # print space for tile
    """create dict or list for every tile with each row?
        'loop for' to chose from empty or used rows?
        every line calls specific position in list/dict"""
    # dict for tiles elements
    tg = {1: [], 2: [], 3: [], 4: []}

    # tile elements
    row0 = f"┌{'─'*13}┐"
    row1 = "│    ╲   ╱    │"
    row2 = '│     ╲ ╱     │'
    row3 = '│      ╳      │'
    row4 = '│     ╱ ╲     │'
    row5 = '│    ╱   ╲    │'
    row6 = f"└{'─'*13}┘"
    rowe = f"│{' ' * 13}│"

    # assign row elements based on tile terrain name
    for n in range(0, len(names)):
        if names[n] == ' ':  # no tile in this market space
            tg[n+1] = [row0, row1, row2, row3, row4, row5, row6]
        else:
            tg[n+1] = [row0, rowe, rowe, rowe, rowe, rowe, row6]

    # create line n: terrain name
    ln = f'{names[0]: ^{sp}}{names[1]: ^{sp}}{names[2]: ^{sp}}{names[3]: ^{sp}}'
    # create line 0-6
    l0 = f'{tg.get(1)[0]: ^{sp}}{tg.get(2)[0]: ^{sp}}{tg.get(3)[0]: ^{sp}}{tg.get(4)[0]: ^{sp}}'
    l1 = f'{tg.get(1)[1]: ^{sp}}{tg.get(2)[1]: ^{sp}}{tg.get(3)[1]: ^{sp}}{tg.get(4)[1]: ^{sp}}'
    l2 = f'{tg.get(1)[2]: ^{sp}}{tg.get(2)[2]: ^{sp}}{tg.get(3)[2]: ^{sp}}{tg.get(4)[2]: ^{sp}}'
    l3 = f'{tg.get(1)[3]: ^{sp}}{tg.get(2)[3]: ^{sp}}{tg.get(3)[3]: ^{sp}}{tg.get(4)[3]: ^{sp}}'
    l4 = f'{tg.get(1)[4]: ^{sp}}{tg.get(2)[4]: ^{sp}}{tg.get(3)[4]: ^{sp}}{tg.get(4)[4]: ^{sp}}'
    l5 = f'{tg.get(1)[5]: ^{sp}}{tg.get(2)[5]: ^{sp}}{tg.get(3)[5]: ^{sp}}{tg.get(4)[5]: ^{sp}}'
    l6 = f'{tg.get(1)[6]: ^{sp}}{tg.get(2)[6]: ^{sp}}{tg.get(3)[6]: ^{sp}}{tg.get(4)[6]: ^{sp}}'
    # create line p: points
    lp = f'{points[0]: ^{sp}}{points[1]: ^{sp}}{points[2]: ^{sp}}{points[3]: ^{sp}}'

    # construct market field with tiles
    tot = f'{ln}\n{l0}\n{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{lp}\n'

    print(tot)


def question_menu(question):  # for universal purposes
    """Print order and list of possible actions with it.
       :param question: **list** containing *string* with question asked user
       and *dictionary* with actions user can take.
       :return: *print* menu based on args with set distance from window border.
       """
    order = question[0]
    options = question[1]
    tab = 11  # base distance from window border

    final_tab = tab + len(order)-5  # distance based on element

    full = f'{order: >{final_tab}}\n\n'  # First line of user menu

    for number, option in options.items():  # Create menu text lines
        final_tab = tab - len(str(number))
        # if type(number) == str:  # empty line for additional options
        #     full += '\n'
        full += f'{"[": >{final_tab}}{number}]. {option} \n'

    print(full)
