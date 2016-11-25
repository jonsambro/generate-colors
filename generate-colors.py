import tkinter as tk
import random
import numpy
#from skimage import color
import csv
class Application(tk.Frame):

    keystrokes = {
        '1': "BROWN",
        '2': "RED",
        '3': "ORANGE",
        '4': "YELLOW",
        '5': "GREEN",
        '6': "BLUE",
        '7': "VIOLET",
        '8': "GREY",
        '9' : "WHITE",
        '0': "BLACK",
        'b': "BASE",
        'B': "BASE",
        'g': "GOLD",
        'G': "GOLD",
        's': "SILVER",
        'S': "SILVER"
    }

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.c = self.set_random_color()
        self.file = open('colors.csv', 'a')
        self.writer = csv.writer(self.file, delimiter=',')
        self.frame = tk.Frame(root, width=400, height=400)
        self.label = tk.Label(self.frame, width=100, height=50, text="Press a key to classify", bg=self.c)
        self.label.pack()
        self.frame.bind("<KeyPress>", self.keydown)
        self.frame.pack()
        self.frame.focus_set()


    def keydown(self, e):
        c = self.c
        print(c)
        print(type(c))
        r,g,b = c[1:3], c[3:5], c[5:7]
        print(r,g,b)
        r = str(int(r,16))
        g = str(int(g,16))
        b = str(int(b,16))
        try:
            color = self.keystrokes[e.char]
        except:
            color = None
        if (color is not None):
            row = [r,g,b,color]
            print(row)
            try:
                self.writer.writerow(row)
            except :
                print("Writer error")
        self.c = self.set_random_color()
        self.label.configure(bg=self.c)
        print('down', e.char)

    def set_random_color(self,lr=0,hr=255,lg=0,hg=255,lb=0,hb=255):
        rc = '#%02X%02X%02X' % (random.randint(lr, hr), random.randint(lg, hg), random.randint(lb, hb))
        return rc



root = tk.Tk()
app = Application(root)
app.mainloop()
