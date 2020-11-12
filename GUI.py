import logic
from tkinter import *


class Btn(Tk):

    def __init__(self, tex, g_row, g_col):
        super().__init__()
        self.tex = tex
        self.g_row = g_row
        self.g_col = g_col
        Button(self, text=tex, height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(tex)).grid(
            row=g_row, column=g_col)


class App(Tk):

    def __init__(self, you_play_as, win_or_loose, *args, **kwargs):
        super().__init__()
        self.title('Tic-tac-toe')
        self.resizable(0, 0)
        self.you_play_as = you_play_as
        self.win_or_loose = win_or_loose
        self.lst_points = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.btn1 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn1))
        self.btn2 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn2))
        self.btn3 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn3))
        self.btn4 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn4))
        self.btn5 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn5))
        self.btn6 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn6))
        self.btn7 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn7))
        self.btn8 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn8))
        self.btn9 = Button(text='', height=5, width=7, command=lambda: logic.logic1.display_sign_on_btn(self.btn9))

    # a function building the GUI
    def gui_build(self):
        # creation of labels
        lbl_you_play_as = Label(self, text='You play as: ' + self.you_play_as)
        lbl_you_play_as.grid(row=0, column=0, columnspan=3, pady=5)
        lbl_win_loose = Label(self, text=self.win_or_loose)
        lbl_win_loose.grid(row=4, column=0, columnspan=3, pady=5)
        # placing buttons
        self.btn1.grid(row=1, column=0)
        self.btn2.grid(row=1, column=1)
        self.btn3.grid(row=1, column=2)
        self.btn4.grid(row=2, column=0)
        self.btn5.grid(row=2, column=1)
        self.btn6.grid(row=2, column=2)
        self.btn7.grid(row=3, column=0)
        self.btn8.grid(row=3, column=1)
        self.btn9.grid(row=3, column=2)

        btn_new_game = Button(self, text='New game', height=3, width=21, command=lambda: logic.logic1.new_game())
        btn_new_game.grid(row=5, column=0, columnspan=3, padx=5)

    # a function starting the GUI
    def gui_start(self):
        self.gui_build()
        self.mainloop()


that_app = App('', '')
