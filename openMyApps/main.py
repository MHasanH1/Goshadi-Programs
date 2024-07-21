from AppOpener import open
import tkinter as tk
from tkinter import *


def open_apps():
    if gameloop.get() == 1:
        apps.append("gameloop")
    if word.get() == 1:
        apps.append("word")
    if vsCode.get() == 1:
        apps.append("visual studio code")
    if pes.get() == 1:
        apps.append("pro evolution soccer 2017")
    for app in apps:
        open(app, match_closest=True)
    apps.clear()


window = tk.Tk()
w = 200
h = 150

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

tk.Label(
    text="Choose Your Apps:",
    fg="white",
    bg="black"
).pack()

gameloop = IntVar()
Checkbutton(text="gameloop", variable=gameloop).pack()

word = IntVar()
Checkbutton(text="word", variable=word).pack()

vsCode = IntVar()
Checkbutton(text="vs code", variable=vsCode).pack()

pes = IntVar()
Checkbutton(text="PES 2017", variable=pes).pack()

apps = []

tk.Button(
    text="Open",
    bg="blue",
    fg="yellow",
    command=open_apps
).pack()

window.mainloop()
