import tkinter as tk

window = tk.Tk()
window.title("carre qui bouge")
imag = tk.PhotoImage(file="C:\\app\\python\\L1S2-python\\L1S2-python\\TD\\TD2\\carre_qui_bouge\\isha.png")
coffre = tk.PhotoImage(file="C:\\app\\python\\L1S2-python\\L1S2-python\\TD\\TD2\\carre_qui_bouge\\coffre.png")
ptitimage = coffre.subsample(2, 2)


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


canva = tk.Canvas(window, width=x*2, height=y*2)
canva.pack(fill="both", expand='true')
canva.create_image(700, 400, image=ptitimage)
carre = canva.create_rectangle(x, y, x+20, y+20, fill="blue", width=2)
# coffr = canva.create_image()

window.bind("<KeyPress-q>", left)
window.bind("<KeyPress-d>", right)
window.bind("<KeyPress-z>", up)
window.bind("<KeyPress-s>", down)

canva.grid()
window.tk.mainloop()
