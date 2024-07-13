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
        self.break_walls_r()

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

    def break_walls_r(self):
        i, j = 0, 0
        curr = self.__cells[i][j]
        
        while True:
            curr.visited = True
            possible_next = []

            down_cell = None
            up_cell = None
            left_cell = None
            right_cell = None

            if i + 1 < self.num_rows - 1: 
                down_cell = self.__cells[i + 1][j]
            if i - 1 >= 0: 
                up_cell = self.__cells[i - 1][j]
            if j - 1 >= 0: 
                left_cell = self.__cells[i][j - 1]
            if j + 1 < self.num_cols - 1: 
                right_cell = self.__cells[i][j + 1]

            if down_cell and down_cell.visited == False:
                possible_next.append('down')
            if up_cell and up_cell.visited == False:
                possible_next.append('up')
            if left_cell and left_cell.visited == False:
                possible_next.append('left')
            if right_cell and right_cell.visited == False:
                possible_next.append('right')

            print(possible_next)

            if len(possible_next) == 0:
                curr.draw()
                break

            if len(possible_next) == 1:
                next_dir_index = 0
            else:
                next_dir_index = random.randrange(0, len(possible_next) - 1)

            if possible_next[next_dir_index] == 'down':
                curr.has_bottom_wall = False
                curr.draw()
                down_cell.has_top_wall = False
                down_cell.draw()
                next_cell = down_cell
                next_i = i + 1
                next_j = j
            if possible_next[next_dir_index] == 'up':
                curr.has_bottom_wall = False
                curr.draw()
                up_cell.has_top_wall = False
                up_cell.draw()
                next_cell = up_cell
                next_i = i - 1
                next_j = j
            if possible_next[next_dir_index] == 'left':
                curr.has_bottom_wall = False
                curr.draw()
                left_cell.has_top_wall = False
                left_cell.draw()
                next_cell = left_cell
                next_i = i
                next_j = j - 1
            if possible_next[next_dir_index] == 'right':
                curr.has_bottom_wall = False
                curr.draw()
                right_cell.has_top_wall = False
                right_cell.draw()
                next_cell = right_cell
                next_i = i
                next_j = j + 1

            i = next_i
            j = next_j
            curr = next_cell
            continue
            

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
