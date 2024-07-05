from line import Line
from point import Point

class Cell:
    def __init__(
            self, 
            window,
            top_left_point, 
            bottom_right_point,
            has_left_wall = True, 
            has_right_wall = True, 
            has_top_wall = True, 
            has_bottom_wall = True, 
        ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = top_left_point.x
        self.y1 = top_left_point.y
        self.x2 = bottom_right_point.x
        self.y2 = bottom_right_point.y

        self.__win = window

    def draw(self):
        lines = []
        if self.has_left_wall:
            left_wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        else:
            left_wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2), 'white')
        lines.append(left_wall)

        if self.has_top_wall:
            top_wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        else:
            top_wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1), 'white')
        lines.append(top_wall)

        if self.has_right_wall:
            right_wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        else:
            right_wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2), 'white')
        lines.append(right_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        else:
            bottom_wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2), 'white')
        lines.append(bottom_wall)

        for line in lines:
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        from_x = (self.x1 + self.x2) / 2
        from_y = (self.y1 + self.y2) / 2
        to_x = (to_cell.x1 + to_cell.x2) / 2
        to_y = (to_cell.y1 + to_cell.y2) / 2

        line = Line(
            Point(from_x, from_y),
            Point(to_x, to_y)
        )
        self.__win.draw_line(line, color)

