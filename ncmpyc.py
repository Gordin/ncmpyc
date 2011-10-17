import curses

class Window:
    def __init__(self, screen, height, width, begin_y, begin_x):
        self.win = curses.newwin(height, width, begin_y, begin_x)

    def draw(self):
        self.win.refresh()

    def show(self):
        self.draw()

class InfoWindow(Window):
    def __init__(self, screen):
        sY, sX = screen.getmaxyx()
        Window.__init__(self, screen, 10, sX, 0, 0)
        self.win.box()

def init(stdscr):
# Farben
    #curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, -1, -1)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLUE)

# Fenster und Hintergrundfarben
    stdscr.bkgd(curses.color_pair(1))
    stdscr.refresh()

    win = curses.newwin(5, 20, 5, 5)
    win.bkgd(curses.color_pair(2))
    win.box()
    win.addstr(2, 2, "Hallo, Welt!")
    win.refresh()

    win.bkgd(curses.color_pair(0))
    return stdscr, win

def main(stdscr):
    screen, win = init(stdscr)
    info = InfoWindow(screen)
    info.show()
    maxY, maxX = screen.getmaxyx()
    global maxY, maxX
    container = Window(screen, maxY - 10, maxX, 10, 0)
    container.win.box()
    container.show()
    curses.curs_set(0)
    while True:
        c = screen.getch()
        if c == ord('q'):
            break  # Exit the while()
        elif c == curses.KEY_HOME:
            x = y = 0
        elif c == ord('s'):
            maxY, maxX = screen.getmaxyx()
            container.win.resize(maxY - 10, maxX)
            info.win.resize(10, maxX)
            for x in (container, info):
                x.draw()
    return screen, win

if __name__ == "__main__":
    screen, win = curses.wrapper(main)

