import GUI
import random
from tkinter import *


class Logic:
    def __init__(self, c_or_c):
        self.c_or_c = c_or_c

    def cross_or_circle(self):
        # global c_or_c
        # c_or_c = random.choice(['X', 'O'])
        GUI.that_app.you_play_as = str(self.c_or_c)

    def display_sign_on_btn(self, btext):
        btext = self.c_or_c
        print(btext)


coc = random.choice(['X', 'O'])
logic1 = Logic(coc)
