from tkinter import Tk, BOTH, Canvas
import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title('Maze Generator')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=tk.BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        self.__root.destroy()
        
