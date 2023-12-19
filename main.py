from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(20, 20, 80, 80)
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(80, 20, 140, 80)

    win.wait_for_close()

main()
