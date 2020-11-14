import GUI
import random
from tkinter import *


class Logic:
    def __init__(self, *args):
        self.c_or_c = random.choice(['X', 'O'])
        # self.move_done = 0

    def cross_or_circle(self):
        self.c_or_c = random.choice(['X', 'O'])
        GUI.that_app.lbl_you_play_as.config(text='You play as: ' + self.c_or_c)

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
        k1 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[1] + GUI.that_app.lst_points[2] + 0.1
        k2 = GUI.that_app.lst_points[3] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[5] + 0.2
        k3 = GUI.that_app.lst_points[6] + GUI.that_app.lst_points[7] + GUI.that_app.lst_points[8] + 0.3
        k4 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[3] + GUI.that_app.lst_points[6] + 0.4
        k5 = GUI.that_app.lst_points[1] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[7] + 0.5
        k6 = GUI.that_app.lst_points[2] + GUI.that_app.lst_points[5] + GUI.that_app.lst_points[8] + 0.6
        k7 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[8] + 0.7
        k8 = GUI.that_app.lst_points[3] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[6] + 0.8
        lst_k = [k1, k2, k3, k4, k5, k6, k7, k8]
        max_k = max(lst_k)
        print(max_k)

    def add_p_to_lst_points(self, bt, position):
        if self.c_or_c == 'X':
            if bt == 'O':
                GUI.that_app.lst_points[position] = 2
            elif bt == 'X':
                GUI.that_app.lst_points[position] = 3
            else:
                GUI.that_app.lst_points[position] = 1
        else:
            if bt == 'O':
                GUI.that_app.lst_points[position] = 3
            elif bt == 'X':
                GUI.that_app.lst_points[position] = 2
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
        self.cross_or_circle()
        # self.move_done = 0


logic1 = Logic()
