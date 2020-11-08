import logic
from tkinter import *


class App(Tk):

    def __init__(self, you_play_as, win_or_loose):
        super().__init__()
        self.title('Tic-tac-toe')
        self.resizable(0, 0)
        self.you_play_as = you_play_as
        self.win_or_loose = win_or_loose

    def gui_build(self):
        # global lbl_you_play_as
        lbl_you_play_as = Label(self, text='You play as: ' + self.you_play_as)
        lbl_you_play_as.grid(row=0, column=0, columnspan=3, pady=5)
        lbl_win_loose = Label(self, text=self.win_or_loose)
        lbl_win_loose.grid(row=4, column=0, columnspan=3, pady=5)
        btn_1 = Button(self, text='', height=5, width=7)
        btn_1.grid(row=1, column=0)
        btn_2 = Button(self, text='', height=5, width=7)
        btn_2.grid(row=1, column=1)
        btn_3 = Button(self, text='', height=5, width=7)
        btn_3.grid(row=1, column=2)
        btn_4 = Button(self, text='', height=5, width=7)
        btn_4.grid(row=2, column=0)
        btn_5 = Button(self, text='', height=5, width=7)
        btn_5.grid(row=2, column=1)
        btn_6 = Button(self, text='', height=5, width=7)
        btn_6.grid(row=2, column=2)
        btn_7 = Button(self, text='', height=5, width=7)
        btn_7.grid(row=3, column=0)
        btn_8 = Button(self, text='', height=5, width=7)
        btn_8.grid(row=3, column=1)
        btn_9 = Button(self, text='', height=5, width=7)
        btn_9.grid(row=3, column=2)
        btn_new_game = Button(self, text='New game', height=3, width=21)
        btn_new_game.grid(row=5, column=0, columnspan=3, padx=5)

    """
        def create_button(self, name, text, g_row, g_col, pad_x, pad_y, heig, widt):
        self.name = 
    """

    def gui_start(self):
        self.gui_build()
        self.mainloop()


that_app = App('', '')
