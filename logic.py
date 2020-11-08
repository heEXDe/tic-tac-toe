import GUI
import random


class Logic:

    def cross_or_circle(self):
        global c_or_c
        c_or_c = random.choice(['X', 'O'])
        GUI.that_app.root.lbl_you_play_as.change(text='You play as: ' + str(c_or_c))


logic1 = Logic()
