import tkinter as tk
from tkinter import *
import random

# create ui
win = tk.Tk()
win.geometry('750x750')
win.title('Guess?')

Entry(win, textvariable=guess, width=3, font=('ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50,font=('Courier', 15),relief=GROOVE,bg='orange').place(relx=0.5,rely=0.7,anchor=CENTER)
Entry(win,text=final_score, width=2,font=('ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

guess = IntVar