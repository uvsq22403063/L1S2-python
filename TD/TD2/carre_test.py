import tkinter as tk

window = tk.Tk()
window.title("carre qui bouge")


def left(a):
    canva.move(carre, -20, 0)


def right(b):
    canva.move(carre, 20, 0)


def up(c):
    canva.move(carre, 0, -20)


def down(d):
    canva.move(carre, 0, 20)


x = 960
y = 540


canva = tk.Canvas(window, width=x*2, height=y*2, bg="red")
canva.pack(fill="both", expand='true')
carre = canva.create_rectangle(x, y, x+20, y+20, fill="blue", width=2)


window.bind("<KeyPress-q>", left)
window.bind("<KeyPress-d>", right)
window.bind("<KeyPress-z>", up)
window.bind("<KeyPress-s>", down)

canva.grid()
window.tk.mainloop()
