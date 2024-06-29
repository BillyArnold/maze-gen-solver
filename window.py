from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = 'Maze Generator'
        self.width = width
        self.height = height
        self.__root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    

        
