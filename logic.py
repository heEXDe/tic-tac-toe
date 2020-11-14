import GUI
import random
# from tkinter import *


class Logic:
    def __init__(self, *args):
        self.c_or_c = random.choice(['X', 'O'])
        self.ai_move_done = 0

    def cross_or_circle(self):
        self.c_or_c = random.choice(['X', 'O'])
        GUI.that_app.lbl_you_play_as.config(text='You play as: ' + self.c_or_c)

    def display_sign_on_btn(self, btn, p_lst_p):
        btn.config(text=self.c_or_c)
        self.ai_move(btn, p_lst_p)
        self.ai_move_done = 0

    def ai_move(self, buton, points_list_position):
        # add point to the points list - for a move done by player
        btext = buton['text']
        self.add_p_to_lst_points(btext, points_list_position)
        # calculate the sum of points in rows, columns and across
        k1 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[1] + GUI.that_app.lst_points[2]
        k2 = GUI.that_app.lst_points[3] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[5]
        k3 = GUI.that_app.lst_points[6] + GUI.that_app.lst_points[7] + GUI.that_app.lst_points[8]
        k4 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[3] + GUI.that_app.lst_points[6]
        k5 = GUI.that_app.lst_points[1] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[7]
        k6 = GUI.that_app.lst_points[2] + GUI.that_app.lst_points[5] + GUI.that_app.lst_points[8]
        k7 = GUI.that_app.lst_points[0] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[8]
        k8 = GUI.that_app.lst_points[3] + GUI.that_app.lst_points[4] + GUI.that_app.lst_points[6]
        # choose where the AI should put its mark
        self.ai_chooses_if_two_marks(k1, 0, 1, 2, GUI.that_app.btn1, GUI.that_app.btn2, GUI.that_app.btn3)
        self.ai_chooses_if_two_marks(k2, 3, 4, 5, GUI.that_app.btn4, GUI.that_app.btn5, GUI.that_app.btn6)
        self.ai_chooses_if_two_marks(k3, 6, 7, 8, GUI.that_app.btn7, GUI.that_app.btn8, GUI.that_app.btn9)
        self.ai_chooses_if_two_marks(k4, 0, 3, 6, GUI.that_app.btn1, GUI.that_app.btn4, GUI.that_app.btn7)
        self.ai_chooses_if_two_marks(k5, 1, 4, 7, GUI.that_app.btn2, GUI.that_app.btn5, GUI.that_app.btn8)
        self.ai_chooses_if_two_marks(k6, 2, 5, 8, GUI.that_app.btn3, GUI.that_app.btn6, GUI.that_app.btn9)
        self.ai_chooses_if_two_marks(k7, 0, 4, 8, GUI.that_app.btn1, GUI.that_app.btn5, GUI.that_app.btn9)
        self.ai_chooses_if_two_marks(k8, 3, 4, 6, GUI.that_app.btn2, GUI.that_app.btn5, GUI.that_app.btn7)
        self.ai_chooses_if_one_mark(k1, 0, 1, 2, GUI.that_app.btn1, GUI.that_app.btn2, GUI.that_app.btn3)
        self.ai_chooses_if_one_mark(k2, 3, 4, 5, GUI.that_app.btn4, GUI.that_app.btn5, GUI.that_app.btn6)
        self.ai_chooses_if_one_mark(k3, 6, 7, 8, GUI.that_app.btn7, GUI.that_app.btn8, GUI.that_app.btn9)
        self.ai_chooses_if_one_mark(k4, 0, 3, 6, GUI.that_app.btn1, GUI.that_app.btn4, GUI.that_app.btn7)
        self.ai_chooses_if_one_mark(k5, 1, 4, 7, GUI.that_app.btn2, GUI.that_app.btn5, GUI.that_app.btn8)
        self.ai_chooses_if_one_mark(k6, 2, 5, 8, GUI.that_app.btn3, GUI.that_app.btn6, GUI.that_app.btn9)
        self.ai_chooses_if_one_mark(k7, 0, 4, 8, GUI.that_app.btn1, GUI.that_app.btn5, GUI.that_app.btn9)
        self.ai_chooses_if_one_mark(k8, 3, 4, 6, GUI.that_app.btn2, GUI.that_app.btn5, GUI.that_app.btn7)

    def ai_chooses_if_two_marks(self, k, l1, l2, l3, b1, b2, b3):
        if self.ai_move_done == 0:
            if GUI.that_app.lst_points[l1] == 1 or GUI.that_app.lst_points[l2] == 1 or GUI.that_app.lst_points[l3] == 1:
                # if there are two player's marks in row, column or across
                if k == 7:
                    if GUI.that_app.lst_points[l1] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l1] = 2
                        if self.c_or_c == 'X':
                            b1.config(text='O')
                        else:
                            b1.config(text='X')
                        self.ai_move_done = 1
                    if GUI.that_app.lst_points[l2] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l2] = 2
                        if self.c_or_c == 'X':
                            b2.config(text='O')
                        else:
                            b2.config(text='X')
                        self.ai_move_done = 1
                    if GUI.that_app.lst_points[l3] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l3] = 2
                        if self.c_or_c == 'X':
                            b3.config(text='O')
                        else:
                            b3.config(text='X')
                        self.ai_move_done = 1

    def ai_chooses_if_one_mark(self, k, l1, l2, l3, b1, b2, b3):
        if self.ai_move_done == 0:
            if GUI.that_app.lst_points[l1] == 1 or GUI.that_app.lst_points[l2] == 1 or GUI.that_app.lst_points[l3] == 1:
                # if there is one player's mark in row, column or across
                if k == 5 and self.ai_move_done == 0:
                    if GUI.that_app.lst_points[l1] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l1] = 2
                        if self.c_or_c == 'X':
                            b1.config(text='O')
                        else:
                            b1.config(text='X')
                        self.ai_move_done = 1
                    if GUI.that_app.lst_points[l2] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l2] = 2
                        if self.c_or_c == 'X':
                            b2.config(text='O')
                        else:
                            b2.config(text='X')
                        self.ai_move_done = 1
                    if GUI.that_app.lst_points[l3] == 1 and self.ai_move_done == 0:
                        GUI.that_app.lst_points[l3] = 2
                        if self.c_or_c == 'X':
                            b3.config(text='O')
                        else:
                            b3.config(text='X')
                        self.ai_move_done = 1

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
        self.ai_move_done = 0


logic1 = Logic()
