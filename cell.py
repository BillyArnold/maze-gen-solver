from line import Line
from point import Point

class Cell:
    def __init__(
            self, 
            top_left_point, 
            bottom_right_point,
            window,
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
            lines.append(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            lines.append(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            lines.append(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            lines.append(bottom_wall)

        for line in lines:
            self.__win.draw_line(line)
