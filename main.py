from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    top_left = Point(50, 50)
    bottom_right = Point(150, 150)

    cell = Cell(top_left, bottom_right, win)
    cell.draw()

    top_left_to = Point(200, 200)
    bottom_right_to = Point(250, 250)
    cell_to = Cell(top_left_to, bottom_right_to, win)
    cell_to.draw()

    cell.draw_move(cell_to)

    #l = Line(Point(50, 50), Point(400, 400))
    #win.draw_line(l, fill_color="blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()
