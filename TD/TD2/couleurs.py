import tkinter as tk
import random as rd

larg, haut = 256, 256
r, g, b = 0, 0, 0


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g,
      b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def gris():

    gris = 0

    for i in range(larg):

        gris += 1

        for j in range(haut):

            r, g, b = gris, gris, gris

            draw_pix(i, j, get_color(r, g, b))


def d2d():

    re, bl = 0, 0

    for i in range(larg):

        bl = 0

        for j in range(haut):

            draw_pix(i, j, get_color(re, 0, bl))

            bl += 1
        re += 1


def draw_pix(t, p, color):

    canva.create_rectangle(t, p, t, p, fill=color, width=0)


def ale():

    for i in range(larg):

        for j in range(haut):

            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)

            draw_pix(i, j, get_color(r, g, b))


window = tk.Tk()
window.config(bg="lightgray")
canva = tk.Canvas(window, width=larg, height=haut, bg="black")

b1 = tk.Button(window, text="Aléatoire",
                            padx=20, pady=1, command=ale, fg="blue")
b2 = tk.Button(window, text="Dégradé gris", padx=20, pady=1,
                            command=gris, fg="blue")
b3 = tk.Button(window, text="Dégradé 2d", padx=20, pady=1,
                            command=d2d, fg="blue")

b1.grid(row=0, column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
canva.grid(row=0, column=1, rowspan=3)

print(get_color(255, 255, 255))
draw_pix(larg/2, haut/2, "red")

window.mainloop()
