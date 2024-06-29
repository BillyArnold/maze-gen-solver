from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, fill_color="blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()
