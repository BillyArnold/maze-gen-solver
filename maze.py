import random
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
        seed = None
    ):
        self.start_x = x1
        self.start_y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        if seed is not None:
            self.seed = random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self.__cells[i][j].draw()
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
