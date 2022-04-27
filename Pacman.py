
# Features:
# 1. menu, choose dificulty (with time)
# 2. win, lose (after passing time or after moving 700 times!)
# 3. they choose to start again or exit (after win or lose)
# 4. unicode emojies.
# 5. colorize the text
# 6. print the map in the middle of the screen


# missing features:
# 1. timer (we need to use threading and it is not easy to do for a student)

import curses
import time


def main(stdscr, screen_y, screen_x):
    game_duration = choose_dificulty(stdscr, screen_y, screen_x)
    score = 0
    curses.curs_set(0)  # hide cursor

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    l = ['┼', '└', '┘', '┌', '┐', '│', '|' '─', '─',
         '┤', '┬', '-', '+', '├', '┴', '+', '-']
    create_base_map(stdscr, screen_y, screen_x)

    y = 27
    x = 72

    stdscr.move(y, x)  # move cursor to (20, 20)

    stdscr.addch(y, x, '@', curses.color_pair(2))

    curses.napms(1000)
    start = time.time()
    end = start + game_duration
    for times in range(700):

        # ------------------
        if time.time() >= end or times == 699:
            game_over(stdscr, screen_y, screen_x)
        # -----------------

        key = stdscr.getkey()
        if key == 'KEY_UP':
            character = chr(stdscr.inch(y-1, x))
            if character not in l:
                stdscr.addch(y, x, ' ')
                y -= 1

        elif key == 'KEY_DOWN':
            character = chr(stdscr.inch(y+1, x))
            if character not in l:
                stdscr.addch(y, x, ' ')
                y += 1

        elif key == 'KEY_LEFT':
            character = chr(stdscr.inch(y, x-1))
            if character not in l:
                stdscr.addch(y, x, ' ')
                x -= 1

        elif key == 'KEY_RIGHT':
            character = chr(stdscr.inch(y, x+1))
            if character not in l:
                stdscr.addch(y, x, ' ')
                x += 1
        else:
            pass  # wrong input

        # stdscr.addch(y, x, ' ')
        character = chr(stdscr.inch(y, x))
        if character == '.':
            score += 1
            if score == 431:
                stdscr.clear()
                stdscr.refresh()
                win(stdscr, screen_y, screen_x)

            stdscr.addstr(
                6, 70, f'Your score is: {score}', curses.color_pair(3))
        stdscr.addch(y, x, '@', curses.color_pair(2))
        stdscr.refresh()


def create_base_map(stdscr, screen_y, screen_x):
    y, x = stdscr.getyx()

    base_map = """
                                                    ┌─────────────────────────┬──┬─────────────────────────┐
                                                    │ ....................... │  │  ...................... │
                                                    │ . ┌──────┐ .. ┌─────┐   │  │  . ┌──────┐ . ┌─────┐ . │
                                                    │ . │      │ .. │     │   │  │  . │      │ . │     │ . │
                                                    │ . └──────┘ .. └─────┘   │  │  . └──────┘ . └─────┘ . │
                                                    │ .          ...........  └──┘  ...................... │
                                                    │ . ┌──────┐ ............................... ┌──────┐. │
                                                    │ . │      │ ............................... │      │. │
                                                    │ . └──────┘ ..  ┌────┬─┐       ┌─┬────┐  .  └──────┘. │
                                                    │ .............  └────┤ │       │ ├────┘  ............ │
                                                    ├───────────┐ ....... ├─┴───────┴─┤ ....... ┌──────────┤
                                                    ├───────────┘ ..    . │           │ .     . └──────────┤
                                                    │             .. ┌┐ . │           │ . ┌─┐ .            │
                                                    │             .. ││ . │           │ . ├─┤ .            │
                                                    ├───────────┐ .. ││ . │           │ . │ │ . ┌──────────┤
                                                    ├───────────┘ .. └┘ . ├─┬───────┬─┤ . └─┘ . └──────────┤
                                                    │ ................... │ │       │ │ .................. │
                                                    │ .. ┌───────┐.. ┌────┤ │       │ ├────┐  . ┌──────┐ . │
                                                    │ .. │       │.. └────┴─┘       └─┴────┘  . │      │ . │
                                                    │ .. └───────┘............................. └──────┘ . │
                                                    │ .. ................................................. │
                                                    │ .. ┌───────┐..  ┌────┐ . ┌──┐ .  ┌───┐  . ┌──────┐ . │
                                                    │ .. │       │..  │    │ . │  │ .  │   │  . │      │ . │
                                                    │ .. └───────┘..  └────┘ . │  │ .  └───┘  . └──────┘ . │
                                                    │ ........................ │  │ ........... ..... .... │
                                                    └──────────────────────────┴──┴────────────────────────┘
"""

    x_len = len(
        '                ┌─────────────────────────┬──┬─────────────────────────┐')
    y_len = len(['│' for i in range(26)])
    stdscr.addstr(5, screen_x//2 - len('Pacman Game. Created by me ')//2,
                  'Pacman Game. Created by me \U0001F603', curses.color_pair(2))

    stdscr.addstr(screen_y//2 - y_len//2, screen_x//2 -
                  x_len // 2, base_map)

    stdscr.refresh()

    curses.napms(100)


def choose_dificulty(stdscr, screen_y, screen_x):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_YELLOW)

    stdscr.clear()
    stdscr.addstr(screen_y // 2, screen_x//2-8,
                  'Choose dificulty:\n', curses.color_pair(1))
    stdscr.addstr(screen_y // 2 + 1, screen_x//2-8,
                  '1. Easy \U0001F601\n', curses.color_pair(2))
    stdscr.addstr(screen_y // 2 + 2, screen_x//2-8,
                  '2. Medium \U0001F481\n', curses.color_pair(5))
    stdscr.addstr(screen_y // 2 + 3, screen_x//2-8,
                  '3. Hard \U0001F5FF \U0001F90C\n', curses.color_pair(4))
    stdscr.refresh()
    stdscr.move(screen_y // 2 + 5, screen_x//2-8)
    key = stdscr.getch()

    while key != ord('1') and key != ord('2') and key != ord('3'):
        stdscr.addstr(screen_y // 2 + 5, screen_x//2-25,
                      '\U000026A0 Wrong Input! Please enter either "1" or "2" or "3"', curses.color_pair(6))
        stdscr.refresh()
        stdscr.move(screen_y // 2 + 6, screen_x//2-8)
        key = stdscr.getch()

    if key == ord('1'):
        return 130
    elif key == ord('2'):
        return 90
    elif key == ord('3'):
        return 50


def game_over(stdscr, screen_y, screen_x):

    stdscr.refresh()
    stdscr.addstr(2, screen_x//2-10, 'Game Over! Press any key to back to menu',
                  curses.color_pair(5))
    stdscr.refresh()
    c = stdscr.getch()
    start_pacman(stdscr)


def win(stdscr, screen_y, screen_x):

    win_text = 'YOU WON. Congratulation \U0001F90C. press any key to back to menu'
    stdscr.addstr(screen_y//2, screen_x//2 -
                  len(win_text)//2, win_text, curses.color_pair(2))
    stdscr.refresh()
    c = stdscr.getch()
    start_pacman(stdscr)


def start_pacman(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_YELLOW)
    screen_y, screen_x = stdscr.getmaxyx()
    stdscr.addstr(screen_y//2, screen_x//2,
                  'What do you want to do? \U0001F914', curses.color_pair(5))
    stdscr.addstr(screen_y//2+1, screen_x//2,
                  '1. Start game \U0001F91D', curses.color_pair(2))
    stdscr.addstr(screen_y//2+2, screen_x//2,
                  '2. Exit \U0001F6AA (just use ctrl+z)', curses.color_pair(4))
    stdscr.refresh()
    key = stdscr.getch()
    while key != ord('1'):
        stdscr.addstr(screen_y//2+3, screen_x//2,
                      '\U000026A0 Wrong Input! Please enter either "1" or "ctrl+z"', curses.color_pair(6))
        stdscr.refresh()
        stdscr.move(screen_y//2+4, screen_x//2)
        key = stdscr.getch()
    if key == ord('1'):
        return main(stdscr, screen_y, screen_x)
    else:
        pass
    # end the curses session


curses.wrapper(start_pacman)
