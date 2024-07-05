from cell import Cell
from point import Point
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.start_x = x1
        self.start_y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        for i in range(0, self.num_cols):
            self.__cells.append([])
            for j in range(0, self.num_rows):
                x1 = self.start_x + self.cell_size_x * i 
                y1 = self.start_y + self.cell_size_y * j
                x2 = self.start_x + self.cell_size_x * i + self.cell_size_x
                y2 = self.start_y + self.cell_size_y * j + self.cell_size_y
                top_right = Point(x1, y1)
                bottom_left = Point(x2, y2)
                self.__cells[i].append(Cell(self.win, top_right, bottom_left))

        for k in range(0, self.num_cols):
            for l in range(0, self.num_rows):
                self.__cells[k][l].draw()

    def break_entrance_and_exit(self):
        for k in range(0, self.num_cols):
            for l in range(0, self.num_rows):
                if k == 0 and l == 0:
                    self.__cells[k][l].has_top_wall = False
                    self.__cells[k][l].draw()
                if k == (self.num_cols - 1) and l == (self.num_rows - 1):
                    self.__cells[k][l].has_bottom_wall = False
                    self.__cells[k][l].draw()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
