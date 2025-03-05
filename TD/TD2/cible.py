import tkinter as tk

larg, haut = 600, 600
couleur = ["blue", "green", "black", "yellow", "magenta", "red"]

x0 = 0
y0 = 0
x1 = larg
y1 = haut

window = tk.Tk()
canva = tk.Canvas(window, width=larg, height=haut, bg="black")

for i in range(5):

    for i in range(len(couleur)):
        canva.create_oval(x0, y0, x1, y1, fill=couleur[i])
        x0 += 10
        y0 += 10
        x1 -= 10
        y1 -= 10

canva.grid()
window.mainloop()
