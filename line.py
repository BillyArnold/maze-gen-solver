from tkinter import Tk, BOTH, Canvas

class Line:
    def __init__(self, start, end, fill_color=None):
        self.start = start
        self.end = end
        self.fill_color = fill_color

    def draw(self, canvas, fill_color="black"):
        if self.fill_color is not None:
            fill_color = self.fill_color
        canvas.create_line(
            self.start.x, 
            self.start.y, 
            self.end.x, 
            self.end.y, 
            fill=fill_color, 
            width=2
        )
