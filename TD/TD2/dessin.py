import tkinter as tk
import random as rd

wd = 720
he = 420
color = "red"
objets = []


def cercle():
    x = rd.randint(20, wd - 20)
    y = rd.randint(20, he - 20)

    cercle = canva.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)
    objets.append(cercle)
    print(objets)


def carre():
    x = rd.randint(50, wd - 50)
    y = rd.randint(50, he - 50)
    carre = canva.create_rectangle(x - 20, y - 20, x + 20, y + 20, fill=color)
    objets.append(carre)
    print(objets)


def croix():
    x = rd.randint(50, wd - 50)
    y = rd.randint(50, he - 50)

    ligne1 = canva.create_line(x, y, x + 20, y + 20, fill=color)
    ligne2 = canva.create_line(x + 20, y, x, y + 20, fill=color)
    objets.append(ligne1)
    objets.append(ligne2)
    print(objets)


def colo():
    global color
    color = entree.get()


def undo():

    if len(objets) == 0:
        nul = canva.create_rectangle(0, 0, 0, 0, fill="black")
        objets.append(nul)

    if canva.type(objets[-1]) == "line":

        for i in range(2):
            canva.delete(objets[-1])
            objets.pop()
    else:
        canva.delete(objets[-1])
        objets.pop()


window = tk.Tk()
window.config(bg="cyan")
window.title("p'tit dessin")
canva = tk.Canvas(window, width=wd, height=he, bg="black")
entree = tk.Entry(window)
entree.grid(row=0, column=1)

b1 = tk.Button(window, text="choix couleur",
                            padx=20, pady=1, command=colo, bg="#14a675")
b2 = tk.Button(window, text="cercle", padx=20, pady=1,
                            command=cercle, bg="lightgray")
b3 = tk.Button(window, text="carré", padx=20, pady=1,
                            command=carre, bg="lightgray")
b4 = tk.Button(window, text="croix", padx=20, pady=1,
                            command=croix, bg="lightgray")
b5 = tk.Button(window, text="undo", padx=20, pady=1,
                            command=undo, bg="lightgray")

b1.grid(column=0, row=0)
b2.grid(column=0, row=1)
b3.grid(column=0, row=2)
b4.grid(column=0, row=3)
b5.grid(column=0, row=4)

canva.grid(row=1, column=1, rowspan=3)
window.mainloop()
