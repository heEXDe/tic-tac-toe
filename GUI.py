import logic
from tkinter import *


class App:
    def gui_build(self):
        global root
        root = Tk()
        root.title('Tic-tac-toe')
        root.resizable(0, 0)
        lbl_you_play_as = Label(root, text='You play as: ')
        lbl_you_play_as.grid(row=0, column=0, columnspan=3, pady=5)
        btn_1 = Button(root, text='', height=5, width=7)
        btn_1.grid(row=1, column=0)
        btn_2 = Button(root, text='', height=5, width=7)
        btn_2.grid(row=1, column=1)
        btn_3 = Button(root, text='', height=5, width=7)
        btn_3.grid(row=1, column=2)
        btn_4 = Button(root, text='', height=5, width=7)
        btn_4.grid(row=2, column=0)
        btn_5 = Button(root, text='', height=5, width=7)
        btn_5.grid(row=2, column=1)
        btn_6 = Button(root, text='', height=5, width=7)
        btn_6.grid(row=2, column=2)
        btn_7 = Button(root, text='', height=5, width=7)
        btn_7.grid(row=3, column=0)
        btn_8 = Button(root, text='', height=5, width=7)
        btn_8.grid(row=3, column=1)
        btn_9 = Button(root, text='', height=5, width=7)
        btn_9.grid(row=3, column=2)
        lbl_win_loose = Label(root, text='')
        lbl_win_loose.grid(row=4, column=0, columnspan=3, pady=5)
        btn_new_game = Button(root, text='New game', height=3, width=21)
        btn_new_game.grid(row=5, column=0, columnspan=3, padx=5)

    def gui_start(self):
        self.gui_build()
        root.mainloop()


that_app = App()

