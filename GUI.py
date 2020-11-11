import logic
from tkinter import *


class App(Tk):

    def __init__(self, you_play_as, win_or_loose, btext1, btext2, btext3, btext4, btext5, btext6, btext7, btext8,
                 btext9):
        super().__init__()
        self.title('Tic-tac-toe')
        self.resizable(0, 0)
        self.you_play_as = you_play_as
        self.win_or_loose = win_or_loose
        self.btext1 = btext1
        self.btext2 = btext2
        self.btext3 = btext3
        self.btext4 = btext4
        self.btext5 = btext5
        self.btext6 = btext6
        self.btext7 = btext7
        self.btext8 = btext8
        self.btext9 = btext9

    # a function building the GUI
    def gui_build(self):
        # creation of labels
        lbl_you_play_as = Label(self, text='You play as: ' + self.you_play_as)
        lbl_you_play_as.grid(row=0, column=0, columnspan=3, pady=5)
        lbl_win_loose = Label(self, text=self.win_or_loose)
        lbl_win_loose.grid(row=4, column=0, columnspan=3, pady=5)
        # creation of buttons
        self.create_button(self.btext1, 1, 0)
        self.create_button(self.btext2, 1, 1)
        self.create_button(self.btext3, 1, 2)
        self.create_button(self.btext4, 2, 0)
        self.create_button(self.btext5, 2, 1)
        self.create_button(self.btext6, 2, 2)
        self.create_button(self.btext7, 3, 0)
        self.create_button(self.btext8, 3, 1)
        self.create_button(self.btext9, 3, 2)
        btn_new_game = Button(self, text='New game', height=3, width=21)
        btn_new_game.grid(row=5, column=0, columnspan=3, padx=5)

    # a function to create buttons
    def create_button(self, tex, g_row, g_col):
        Button(self, text=tex, height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(tex)).grid(
            row=g_row, column=g_col)

    # a function starting the GUI
    def gui_start(self):
        self.gui_build()
        self.mainloop()


that_app = App('', '', '', '', '', '', '', '', '', '', '')
