import tkinter as tk
import random as rd

wd = 720
he = 420
color = "blue"

def cercle():
    x = rd.randint(20, wd - 20)
    y = rd.randint(20, he - 20)

    canva.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)


def carre():
    x = rd.randint(50, wd - 50)
    y = rd.randint(50, he - 50)
    canva.create_rectangle(x - 20, y - 20, x + 20, y + 20, fill=color)


def croix():
    x = rd.randint(50, wd - 50)
    y = rd.randint(50, he - 50)

    canva.create_line(x, y, x +20, y + 20, fill=color)
    canva.create_line(x + 20, y, x, y +20, fill=color)


def entrer():
    global 

    
def colo():
    global color
    color = tk.Entry()
    window.bind("KeyPress-enter", entrer)
    color.grid(row=0, column=1)


window = tk.Tk()
window.config(bg="cyan")
window.title("p'tit dessin")
canva = tk.Canvas(window, width=wd, height=he, bg="black")

b1 = tk.Button(window, text="choix couleur", padx=20, pady=1, command=colo, bg="lightgray")
b2 = tk.Button(window, text="cercle", padx=20, pady=1,
                            command=cercle, bg="lightgray")
b3 = tk.Button(window, text="carré", padx=20, pady=1,
                            command=carre, bg="lightgray")
b4 = tk.Button(window, text="croix", padx=20, pady=1,
                            command=croix, bg="lightgray")

b1 = b1.grid(column=0, row=0)
b2 = b2.grid(column=0, row=1)
b3 = b3.grid(column=0, row=2)
b4 = b4.grid(column=0, row=3)

canva.grid(row=1, column=1, rowspan=3)
window.mainloop()
