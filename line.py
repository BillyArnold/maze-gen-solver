from tkinter import Tk, BOTH, Canvas

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, 
            self.start.y, 
            self.end.x, 
            self.end.y, 
            fill=fill_color, 
            width=2
        )