import GUI
import random
from tkinter import *


class Logic:
    def __init__(self, c_or_c):
        self.c_or_c = c_or_c

    def cross_or_circle(self):
        GUI.that_app.you_play_as = str(self.c_or_c)

    def display_sign_on_btn(self, btn):
        btn.config(text=self.c_or_c)
        self.ai_move()

    def ai_move(self):
        btext = GUI.that_app.btn1['text']
        self.add_p_to_lst_points(btext, 0)
        btext = GUI.that_app.btn2['text']
        self.add_p_to_lst_points(btext, 1)
        btext = GUI.that_app.btn3['text']
        self.add_p_to_lst_points(btext, 2)
        btext = GUI.that_app.btn4['text']
        self.add_p_to_lst_points(btext, 3)
        btext = GUI.that_app.btn5['text']
        self.add_p_to_lst_points(btext, 4)
        btext = GUI.that_app.btn6['text']
        self.add_p_to_lst_points(btext, 5)
        btext = GUI.that_app.btn7['text']
        self.add_p_to_lst_points(btext, 6)
        btext = GUI.that_app.btn8['text']
        self.add_p_to_lst_points(btext, 7)
        btext = GUI.that_app.btn9['text']
        self.add_p_to_lst_points(btext, 8)
        print(GUI.that_app.lst_points)

    def add_p_to_lst_points(self, bt, position):
        if bt == 'O':
            GUI.that_app.lst_points[position] = 2
        elif bt == 'X':
            GUI.that_app.lst_points[position] = 3
        else:
            GUI.that_app.lst_points[position] = 1

    def new_game(self):
        GUI.that_app.btn1.config(text="")
        GUI.that_app.btn2.config(text="")
        GUI.that_app.btn3.config(text="")
        GUI.that_app.btn4.config(text="")
        GUI.that_app.btn5.config(text="")
        GUI.that_app.btn6.config(text="")
        GUI.that_app.btn7.config(text="")
        GUI.that_app.btn8.config(text="")
        GUI.that_app.btn9.config(text="")
        GUI.that_app.lst_points = [1, 1, 1, 1, 1, 1, 1, 1, 1]


coc = random.choice(['X', 'O'])
logic1 = Logic(coc)
