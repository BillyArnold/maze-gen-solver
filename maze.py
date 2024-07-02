from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

    def create_cells(self):
        for i in range(num_cols):
            self.cells[i] = []
            self.__cells[i].append(Cell(None, None, self.win))
            for j in range(num_rows):
                self.__cells[i].append(Cell(None, None, self.win))

        for k in range(num_cols):
            for l in range(num_rows):
                self.draw_cell(k, l)

    def draw_cell(self, col, row):
        if self.win is None:
            return
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)
        self.animate()

    def _animate(self):
        if self.win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
