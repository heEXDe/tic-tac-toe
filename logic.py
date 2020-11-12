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


coc = random.choice(['X', 'O'])
logic1 = Logic(coc)
