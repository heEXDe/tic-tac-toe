import logic
from tkinter import *


class App:
    def gui_build(self):
        global root
        root = Tk()
        root.title('Tic-tac-toe')
        root.resizable(0, 0)

    def gui_start(self):
        self.gui_build()
        root.mainloop()


that_app = App()

